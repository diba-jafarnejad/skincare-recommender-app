import ast
import pandas as pd

def safe_list_parse(val):
    """
    Safely parse a stringified list into an actual list of cleaned strings.
    """
    if isinstance(val, str) and val.strip().startswith("["):
        try:
            parsed = ast.literal_eval(val)
            return [item.strip() for item in parsed if isinstance(item, str) and item.strip()]
        except:
            return []
    return []

def tag_functions(text):
    """
    Tags a string description with standardized skincare function labels.
    """
    function_keywords = {
    "hydrating": ["hydrate", "moisturize", "humectant", "water-binding", "emollient"],
    "acne-fighting": ["acne", "blemish", "breakout", "oil control", "antibacterial", "anti-inflammatory"],
    "anti-aging": ["wrinkle", "fine lines", "collagen", "elasticity", "firming", "rejuvenate"],
    "brightening": ["brighten", "radiance", "pigment", "dark spots", "whitening", "tone-evening"],
    "soothing": ["soothe", "calm", "anti-inflammatory", "redness-reducing", "sensitive skin"],
    "exfoliating": ["exfoliate", "renew", "cell turnover", "peel", "resurfacing"],
    "oil-control": ["oil control", "mattify", "sebum-regulating", "pore-minimizing"],
    "antioxidant": ["antioxidant", "free radical", "environmental protection", "pollution defense"],
    "barrier-repair": ["barrier repair", "strengthen", "protective", "ceramides", "lipid-replenishing"],
    "anti-redness": ["anti-redness", "couperose", "vascular support", "calming"],
    "firming": ["firming", "lifting", "tightening", "sagging skin"],
    "uv-protection": ["UV protection", "sunscreen", "SPF", "sunblock"],
    "anti-pollution": ["anti-pollution", "detoxifying", "environmental shield"],
    "healing": ["healing", "repairing", "regenerative", "wound-healing"],
    "anti-inflammatory": ["anti-inflammatory", "calming", "soothing"]
}

    tags = set()
    if isinstance(text, str):
        text = text.lower()
        for label, keywords in function_keywords.items():
            if any(k in text for k in keywords):
                tags.add(label)
    return list(tags)

def clean_list_or_text(val):
    """
    If a list is empty or not valid, return a friendly default string.
    """
    if isinstance(val, list) and val:
        return val
    return "No specific recommendation"

def clean_inci_dataframe(df):
    """
    Cleans and enriches an INCI skincare ingredient DataFrame.
    """
    # Keep only necessary columns
    df = df[[
        "name",
        "what_does_it_do",
        "who_is_it_good_for",
        "who_should_avoid",
        "short_description",
        "url"
    ]].copy()

    # Fill missing values
    df.fillna({
        "name": "",
        "what_does_it_do": "",
        "short_description": "",
        "who_is_it_good_for": "[]",
        "who_should_avoid": "[]",
        "url": ""
    }, inplace=True)

    # Drop rows with empty critical fields
    df.dropna(subset=["name", "what_does_it_do"], inplace=True)
    df = df[df["name"].str.strip() != ""]
    df = df[df["what_does_it_do"].str.strip() != ""]

    # Clean and normalize text
    df["name"] = df["name"].str.strip().str.lower()
    df["what_does_it_do"] = df["what_does_it_do"].str.replace(r"\r\n|\r|\n", " ", regex=True).str.strip()
    df["short_description"] = df["short_description"].str.replace(r"\r\n|\r|\n", " ", regex=True).str.strip()

    # Parse and clean list-like strings
    df["who_is_it_good_for"] = df["who_is_it_good_for"].apply(safe_list_parse)
    df["who_should_avoid"] = df["who_should_avoid"].apply(safe_list_parse)

    # Replace empty or invalid lists with friendly string
    df["who_is_it_good_for"] = df["who_is_it_good_for"].apply(clean_list_or_text)
    df["who_should_avoid"] = df["who_should_avoid"].apply(clean_list_or_text)

    # Add standardized function tags
    df["function_tags"] = df["what_does_it_do"].apply(tag_functions)

    return df

def clean_sephora_dataframe(df):
    """
    Cleans the Sephora dataset:
    - Filters to skincare products only
    - Cleans and standardizes ingredient lists by removing asterisks
    - Drops rows with missing or empty key data
    - Retains all relevant columns
    """

    # Filter to skincare products only (case-insensitive)
    df = df[df["primary_category"].str.lower() == "skincare"]

    # Drop rows with critical missing values
    df.dropna(subset=["product_id", "product_name", "brand_name", "ingredients"], inplace=True)

    # Drop rows where ingredient list ended up empty
    df = df[df["ingredients"].apply(lambda x: len(x) > 0)]

    return df

import re

def clean_ingredient_list(ingredient_str):
    """
    Parses and cleans an ingredient string:
    - Removes asterisks, colons, semicolons, and periods.
    - Splits ingredients based on commas and spaces.
    - Strips whitespace and converts to lowercase.
    """
    if pd.isnull(ingredient_str):
        return []
    
    # Remove specific punctuation
    cleaned_str = re.sub(r'[\*\:\;\.]', '', ingredient_str)
    
    # Split by commas and spaces
    ingredients = re.split(r'[,\s]+', cleaned_str)
    
    # Remove empty strings and standardize case
    return [ingredient.strip().lower() for ingredient in ingredients if ingredient.strip()]

def clean_ingredient_input(input):
    """
    Takes either a comma-separated string or a list of ingredients,
    and returns a cleaned list (lowercase, stripped, and without \ / " ' *).
    Does not explode rows or affect product-level structure.
    """
    if pd.isna(input) or input == '' or input == []:
        return []

    # If input is a string, split by commas
    if isinstance(input, str):
        input = input.split(',')

    # Define unwanted characters to remove
    pattern = r'[\\/*"\'`]'

    # Clean each ingredient
    cleaned = [
        re.sub(pattern, '', ing).strip().lower()
        for ing in input
        if isinstance(ing, str) and ing.strip()
    ]
    
    return cleaned

import re

def clean_review_list(review_list):
    """
    Cleans a single review string.
    - Removes unwanted characters (\ / * " ' `)
    - Lowercases
    - Strips whitespace
    """
    if isinstance(review_list, str) and review_list.strip():
        pattern = r'[\\/*"\'`]'
        return re.sub(pattern, '', review_list).strip().lower()
    return ''


def convert_to_list(val):
    try:
        return ast.literal_eval(val)
    except (ValueError, SyntaxError):
        return []  # Return an empty list if parsing fails