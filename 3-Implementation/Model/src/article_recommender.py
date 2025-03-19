"""
Article recommendation module for NutriGenius.

This module implements recommendation algorithms for nutrition articles
based on user profiles, food items, and health status.
"""

import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from typing import Dict, List, Tuple, Union, Optional, Any

# Import common utilities
from utils.common import (
    load_config,
    create_directory,
    save_model,
    load_model
)

class ArticleRecommender:
    """Recommender system for nutrition and health articles."""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the article recommender system.
        
        Args:
            config_path: Optional path to configuration file
        """
        self.config = {}
        if config_path and os.path.exists(config_path):
            self.config = load_config(config_path)
        
        # Set default configurations
        self.articles_path = self.config.get('articles_path', None)
        self.model_path = self.config.get('model_path', None)
        self.top_n = self.config.get('top_n', 5)
        
        # Initialize article data
        self.articles_df = None
        if self.articles_path and os.path.exists(self.articles_path):
            self.load_articles(self.articles_path)
        
        # Initialize vectorizer and article vectors
        self.vectorizer = None
        self.article_vectors = None
        
        # Download NLTK resources if needed
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
    
    def load_articles(self, articles_path: str) -> None:
        """
        Load articles from a CSV file.
        
        Args:
            articles_path: Path to the articles CSV file
        """
        try:
            self.articles_df = pd.read_csv(articles_path)
            print(f"Loaded {len(self.articles_df)} articles from {articles_path}")
            
            # Ensure required columns exist
            required_cols = ['title', 'content', 'tags', 'category']
            for col in required_cols:
                if col not in self.articles_df.columns:
                    self.articles_df[col] = ""
                    print(f"Warning: '{col}' column not found, creating empty column")
        except Exception as e:
            print(f"Error loading articles: {e}")
            # Create empty dataframe with required columns
            self.articles_df = pd.DataFrame(columns=[
                'article_id', 'title', 'content', 'tags', 'category', 'author', 'date'
            ])
    
    def preprocess_text(self, text: str) -> str:
        """
        Preprocess text for feature extraction.
        
        Args:
            text: Input text
            
        Returns:
            Preprocessed text
        """
        # Tokenize
        tokens = nltk.word_tokenize(text.lower())
        
        # Remove stopwords
        stopwords = set(nltk.corpus.stopwords.words('english'))
        tokens = [token for token in tokens if token not in stopwords]
        
        # Join tokens back into string
        return ' '.join(tokens)
    
    def build_article_vectors(self) -> None:
        """
        Build TF-IDF vectors for all articles.
        """
        if self.articles_df is None or self.articles_df.empty:
            print("No articles available. Please load articles first.")
            return
        
        # Combine article text fields
        self.articles_df['combined_text'] = (
            self.articles_df['title'] + ' ' + 
            self.articles_df['content'] + ' ' + 
            self.articles_df['tags'] + ' ' + 
            self.articles_df['category']
        )
        
        # Preprocess text
        self.articles_df['processed_text'] = self.articles_df['combined_text'].apply(
            self.preprocess_text
        )
        
        # Initialize vectorizer
        self.vectorizer = TfidfVectorizer(max_features=5000)
        
        # Build article vectors
        self.article_vectors = self.vectorizer.fit_transform(
            self.articles_df['processed_text']
        )
        
        print(f"Built TF-IDF vectors for {len(self.articles_df)} articles with {self.article_vectors.shape[1]} features")
    
    def find_similar_articles(self, query: str, top_n: int = None) -> pd.DataFrame:
        """
        Find articles similar to a query.
        
        Args:
            query: Query text
            top_n: Number of top articles to return (default from config)
            
        Returns:
            DataFrame with top matching articles
        """
        if self.vectorizer is None or self.article_vectors is None:
            self.build_article_vectors()
        
        if self.articles_df is None or self.articles_df.empty:
            print("No articles available. Please load articles first.")
            return pd.DataFrame()
        
        # Use config top_n if not specified
        if top_n is None:
            top_n = self.top_n
        
        # Preprocess query
        processed_query = self.preprocess_text(query)
        
        # Transform query to TF-IDF vector
        query_vector = self.vectorizer.transform([processed_query])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(query_vector, self.article_vectors).flatten()
        
        # Get top similar articles
        top_indices = similarities.argsort()[-top_n:][::-1]
        
        # Create result dataframe
        results = self.articles_df.iloc[top_indices].copy()
        results['similarity'] = similarities[top_indices]
        
        return results[['article_id', 'title', 'category', 'tags', 'similarity']]
    
    def recommend_for_user(
        self, 
        user_profile: Dict[str, Any],
        food_items: List[str] = None,
        health_status: Dict[str, Any] = None,
        top_n: int = None
    ) -> pd.DataFrame:
        """
        Recommend articles based on user profile, food items, and health status.
        
        Args:
            user_profile: User profile data (age, gender, etc.)
            food_items: List of food items user is interested in
            health_status: Health status metrics
            top_n: Number of top articles to return
            
        Returns:
            DataFrame with recommended articles
        """
        if self.vectorizer is None or self.article_vectors is None:
            self.build_article_vectors()
        
        # Use config top_n if not specified
        if top_n is None:
            top_n = self.top_n
        
        # Build query from user profile and interests
        query_parts = []
        
        # Add age-related terms
        if 'age' in user_profile:
            age = user_profile['age']
            if age < 18:
                query_parts.append("nutrition for children teenagers")
            elif age < 30:
                query_parts.append("nutrition for young adults")
            elif age < 50:
                query_parts.append("nutrition for adults")
            else:
                query_parts.append("nutrition for seniors elderly")
        
        # Add gender-related terms
        if 'gender' in user_profile:
            gender = user_profile['gender'].lower()
            if gender == 'male':
                query_parts.append("men's nutrition")
            elif gender == 'female':
                query_parts.append("women's nutrition")
        
        # Add food items
        if food_items:
            food_query = " ".join(food_items)
            query_parts.append(f"nutrition {food_query}")
        
        # Add health status terms
        if health_status:
            # BMI-related recommendations
            if 'bmi' in health_status:
                bmi = health_status['bmi']
                if bmi < 18.5:
                    query_parts.append("underweight nutrition gain weight healthy")
                elif bmi < 25:
                    query_parts.append("healthy weight maintenance")
                elif bmi < 30:
                    query_parts.append("overweight nutrition weight management")
                else:
                    query_parts.append("obesity nutrition weight loss")
            
            # Add other health conditions
            if 'conditions' in health_status:
                conditions = " ".join(health_status['conditions'])
                query_parts.append(f"nutrition for {conditions}")
        
        # Combine all query parts
        combined_query = " ".join(query_parts)
        
        # Find similar articles
        return self.find_similar_articles(combined_query, top_n)
    
    def save(self, model_path: str = None) -> None:
        """
        Save the recommender model.
        
        Args:
            model_path: Path to save the model
        """
        if model_path is None:
            model_path = self.model_path
        
        if model_path is None:
            raise ValueError("Model path not specified")
        
        # Create model directory if it doesn't exist
        create_directory(os.path.dirname(model_path))
        
        # Save model components
        model_data = {
            'vectorizer': self.vectorizer,
            'article_vectors': self.article_vectors,
            'articles_df': self.articles_df
        }
        
        # Save using pickle
        import pickle
        with open(model_path, 'wb') as f:
            pickle.dump(model_data, f)
        
        print(f"Recommender model saved to {model_path}")
    
    def load(self, model_path: str = None) -> None:
        """
        Load the recommender model.
        
        Args:
            model_path: Path to the saved model
        """
        if model_path is None:
            model_path = self.model_path
        
        if model_path is None or not os.path.exists(model_path):
            raise ValueError(f"Model path not specified or doesn't exist: {model_path}")
        
        # Load model components
        import pickle
        with open(model_path, 'rb') as f:
            model_data = pickle.load(f)
        
        self.vectorizer = model_data['vectorizer']
        self.article_vectors = model_data['article_vectors']
        self.articles_df = model_data['articles_df']
        
        print(f"Recommender model loaded from {model_path}")

def create_sample_article_dataset(output_path: str, num_articles: int = 100) -> None:
    """
    Create a sample dataset of nutrition articles for testing.
    
    Args:
        output_path: Path to save the sample dataset
        num_articles: Number of sample articles to generate
    """
    # Define sample categories and tags
    categories = [
        'Nutrition Basics', 'Weight Management', 'Healthy Recipes',
        'Dietary Supplements', 'Disease Prevention', 'Sports Nutrition',
        'Age-specific Nutrition', 'Food Science'
    ]
    
    tags = [
        'protein', 'carbohydrates', 'fats', 'vitamins', 'minerals',
        'weight loss', 'weight gain', 'muscle building', 'diabetes',
        'heart health', 'gut health', 'immune system', 'energy',
        'metabolism', 'vegetarian', 'vegan', 'keto', 'paleo',
        'mediterranean', 'children', 'teenagers', 'adults', 'seniors'
    ]
    
    # Sample titles and content snippets
    titles = [
        "The Role of Protein in Muscle Development",
        "Understanding Carbohydrates: Good vs. Bad",
        "Healthy Fats for Heart Health",
        "Vitamins and Minerals: Your Complete Guide",
        "Weight Loss Strategies That Actually Work",
        "Nutrition for Muscle Gain",
        "Dietary Approaches to Managing Diabetes",
        "Heart-Healthy Eating Patterns",
        "Boosting Your Immune System Through Diet",
        "Nutrition for Energy and Performance",
        "Understanding Your Metabolism",
        "Plant-Based Nutrition Guide",
        "Keto Diet: Benefits and Risks",
        "The Mediterranean Diet and Longevity",
        "Nutrition for Children: Building Healthy Habits",
        "Teenage Nutrition: Supporting Growth and Development",
        "Adult Nutrition: Maintaining Health Through Middle Age",
        "Senior Nutrition: Dietary Needs for Aging Well"
    ]
    
    content_snippets = [
        "Protein is an essential macronutrient that plays a crucial role in muscle development and repair.",
        "Carbohydrates are the body's main source of energy, but choosing the right types is important.",
        "Not all fats are created equal. Healthy fats are essential for hormone production and cell health.",
        "Vitamins and minerals are micronutrients that support numerous bodily functions.",
        "Sustainable weight loss requires a combination of dietary changes, physical activity, and lifestyle adjustments.",
        "Building muscle requires adequate protein intake, caloric surplus, and resistance training.",
        "Managing diabetes through diet involves monitoring carbohydrate intake and choosing foods with a low glycemic index.",
        "A heart-healthy diet emphasizes fruits, vegetables, whole grains, and limits saturated fats and sodium.",
        "Certain nutrients like vitamin C, vitamin D, and zinc play important roles in immune function.",
        "Proper nutrition can significantly impact your energy levels and athletic performance.",
        "Metabolism refers to all chemical processes in the body that convert food into energy.",
        "Plant-based diets can provide all necessary nutrients when properly planned.",
        "The ketogenic diet is a high-fat, low-carbohydrate diet that can help with weight loss.",
        "The Mediterranean diet is associated with reduced risk of heart disease and longer lifespan.",
        "Children need nutrients to support growth, brain development, and establish healthy eating habits.",
        "Teenage years are characterized by rapid growth and development, requiring increased caloric and nutrient intake.",
        "Adult nutrition focuses on maintaining health and preventing chronic diseases.",
        "As we age, our nutritional needs change, often requiring increased protein and certain vitamins."
    ]
    
    # Generate sample articles
    articles = []
    for i in range(num_articles):
        # Select random title and content
        title_idx = np.random.randint(0, len(titles))
        content_idx = np.random.randint(0, len(content_snippets))
        
        # Add some randomization to titles
        title = titles[title_idx]
        if np.random.random() > 0.5:
            title += f": Part {np.random.randint(1, 5)}"
        
        # Generate longer content
        content = content_snippets[content_idx]
        for _ in range(np.random.randint(3, 8)):
            content += " " + content_snippets[np.random.randint(0, len(content_snippets))]
        
        # Select random category and tags
        category = np.random.choice(categories)
        num_tags = np.random.randint(2, 6)
        article_tags = ", ".join(np.random.choice(tags, size=num_tags, replace=False))
        
        # Generate random date in the last 2 years
        year = np.random.randint(2022, 2024)
        month = np.random.randint(1, 13)
        day = np.random.randint(1, 29)
        date = f"{year}-{month:02d}-{day:02d}"
        
        # Create article object
        article = {
            'article_id': i + 1,
            'title': title,
            'content': content,
            'category': category,
            'tags': article_tags,
            'author': f"Author {np.random.randint(1, 10)}",
            'date': date
        }
        
        articles.append(article)
    
    # Create DataFrame and save to CSV
    articles_df = pd.DataFrame(articles)
    
    # Create directory if it doesn't exist
    create_directory(os.path.dirname(output_path))
    
    # Save to CSV
    articles_df.to_csv(output_path, index=False)
    print(f"Sample article dataset with {num_articles} articles saved to {output_path}")

# Sample usage demonstration
if __name__ == "__main__":
    # Example of how to use the article recommender module
    print("Article recommender module for NutriGenius")
    
    # Create and save sample article dataset
    sample_data_path = "../data/processed/sample_articles.csv"
    create_sample_article_dataset(sample_data_path, num_articles=100)
    
    # Create recommender
    recommender = ArticleRecommender()
    
    # Load sample articles
    recommender.load_articles(sample_data_path)
    
    # Build article vectors
    recommender.build_article_vectors()
    
    # Example: Find articles related to protein
    print("\nExample: Articles about protein")
    protein_articles = recommender.find_similar_articles("protein for muscle building", top_n=3)
    print(protein_articles)
    
    # Example: Recommendations for a user
    print("\nExample: Recommendations for a 45-year-old male interested in weight loss")
    user_profile = {
        'age': 45,
        'gender': 'male'
    }
    food_items = ['chicken', 'broccoli', 'rice']
    health_status = {
        'bmi': 28.5,
        'conditions': ['high blood pressure', 'pre-diabetes']
    }
    
    recommendations = recommender.recommend_for_user(
        user_profile, food_items, health_status, top_n=3
    )
    print(recommendations) 