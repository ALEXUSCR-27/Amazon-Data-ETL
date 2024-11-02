from utils.data_formatter import data_formatter
import pandas as pd

def transform_data():
    print("TRANSFORMING AND PREPARING DATA")
    products_df = pd.read_csv('./data/extracted/amazon_data_extracted.csv')
    
    products_df.drop_duplicates(inplace=True)
    products_df.dropna(inplace=True)

    products_df['discounted_price'] = (products_df['discounted_price'].apply(data_formatter.clean_prices).astype('float'))
    products_df['actual_price'] = (products_df['actual_price'].apply(data_formatter.clean_prices).astype('float'))
    products_df['discount_percentage'] = (products_df['discount_percentage'].apply(data_formatter.clean_percentages).astype('float'))
    products_df['rating'] = products_df['rating'].apply(data_formatter.clean_ratings).astype(float)
    products_df['rating_count'] = products_df['rating_count'].apply(data_formatter.clean_rating_count).astype(int)

    products_df[['temp_cat', 'sub_category']] = products_df['category'].apply(data_formatter.clean_category).apply(pd.Series)
    products_df.drop(columns='category', inplace=True)
    products_df.rename(columns={'temp_cat':'category'}, inplace=True)

    products_df.drop_duplicates(inplace=True, subset=['product_id'])

    return store_csv_backup(products_df)

def store_csv_backup(products_df):
    print("SAVING CSV DATA BACKUP")
    try:
        products_df.to_csv("./data/processed/amazon_data_transformed.csv", index=False)
        return True
    except:
        return False
