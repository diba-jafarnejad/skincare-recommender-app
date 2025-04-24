# skincare-recommender-app
BetterSkin is a machine learning-powered web app that recommends personalized skincare products tailored to your unique skin type (dry, oily, sensitive, acne-prone, mature, or dull). It ranks products using a combination of ingredient intelligence and user ratings.
## Features
- Ingredient-based skin match using mapped function tags (e.g., hydrating, anti-aging)

- Custom-trained logistic regression models per skin type

- Ranked recommendations by relevance + rating

- Filter by category, price range, and affordability

- Real-time product and brand name search

- Streamlit-powered UI with a girly aesthetic

## Tech Stack
- Python, Pandas, NumPy

- Scikit-learn (Logistic Regression, Scaling)

- Streamlit for frontend interface

- Google Colab and VS Code for development

- Custom Feature Engineering: ingredient parsing, function tag matching, relevance scoring

## Datasets
This project uses and references the following skincare and beauty datasets:

- [INCI Dataset on Hugging Face](https://huggingface.co/datasets/yavuzyilmaz/cosmetic-ingredients)  
  A science-backed skincare ingredient database offering detailed explanations of ingredient purposes and effects.

- [Sephora Products and Skincare Reviews dataset](https://www.kaggle.com/datasets/nadyinky/sephora-products-and-skincare-reviews)  
  Contains product names, categories, ingredients, reviews, and skin concerns—ideal for ingredient-based modeling and building recommender systems.


