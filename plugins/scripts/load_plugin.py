import os
from supabase import create_client, Client
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

def load_data_db():
    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    products_df = pd.read_csv('./data/processed/amazon_data_transformed.csv')
    products_js = products_df.to_dict(orient="records")
    try:
        response = (
            supabase.table("amazon_products_etl")
            .insert(products_js, returning='minimal')
            .execute()
        )
        return response
    except Exception as exception:
        return exception



    
