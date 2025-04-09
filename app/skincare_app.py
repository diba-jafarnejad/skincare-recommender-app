from utils.data_loaders import load_sephora_data, load_inci_mapping

# Load data for recommendation logic
df = load_sephora_data()
inci_df = load_inci_mapping()

# Use this data for filtering by skin concern, displaying product info, etc.