# import os
# from supabase import create_client, Client
import pandas as pd
import json

# url: str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")
# supabase: Client = create_client(url, key)


def load_data_db():
    products_df = pd.read_csv('./data/processed/amazon_data_transformed.csv')
    products_js = json.dumps(products_df.to_dict(orient="records"), ensure_ascii=False).replace("\\/", "/")
    
