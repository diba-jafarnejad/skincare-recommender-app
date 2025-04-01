# skincare-recommender-app
A machine learning-powered web app that recommends skincare products based on your skin concerns (like acne, dryness, or sensitivity), grouped by product category (cleanser, moisturizer, etc).
## Features
- Ingredient-based predictions using TF-IDF + ML
- Grouped recommendations by product type
- Streamlit-powered user interface

## Tech Stack
- Python, Pandas, Scikit-learn, Streamlit, TF-IDF, Multilabel Classification

## Datasets
This project uses and references the following skincare and beauty datasets:

- [Amazon - Ratings (Beauty Products)](https://www.kaggle.com/datasets/skillsmuggler/amazon-ratings)  
  Includes product ratings and reviews from Amazon's beauty category—great for NLP sentiment analysis and popularity-based filtering.

- [INCI Decoder (Ingredient Database)](https://incidecoder.com/)  
  A science-backed skincare ingredient database offering detailed explanations of ingredient purposes and effects.

- [Paula's Choice Ingredient Dictionary](https://www.paulaschoice.com/ingredient-dictionary?srsltid=AfmBOopqE0NuYpqNbK48mRBKHcA1etCBzoUTXcbpbt0cnKSIf7XyjvtD)  
  An educational ingredient reference library that explains the function and safety of skincare ingredients.

- [Sephora Products and Skincare Reviews dataset](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews)  
  Contains product names, categories, ingredients, reviews, and skin concerns—ideal for ingredient-based modeling and building recommender systems.
