from utils.data_formatter import data_formatter
import pandas as pd
import json

def transform_data():
    print("TRANSFORMING AND PREPARING DATA")
    products_df = pd.read_csv('./data/extracted/amazon_data_extracted.csv')
    
    products_df.drop_duplicates(inplace=True)
    products_df.dropna(inplace=True)

    products_df['discounted_price'] = (products_df['discounted_price'].apply(data_formatter.clean_prices).astype('float'))
    products_df['actual_price'] = (products_df['actual_price'].apply(data_formatter.clean_prices).astype('float'))
    products_df['discount_percentage'] = (products_df['discount_percentage'].apply(data_formatter.clean_percentages).astype('float'))
    products_df['rating'] = products_df['rating'].apply(data_formatter.clean_ratings).astype(float)
    products_df['rating_count'] = products_df['rating_count'].apply(data_formatter.clean_rating_count).astype(float)

    # print(products_df['rating_count'].apply(type).value_counts())
    # print(products_df['rating_count'])
    
    return store_csv_backup(products_df)

def store_csv_backup(products_df):
    print("SAVING CSV DATA BACKUP")
    try:
        products_df.to_csv("./data/processed/amazon_data_transformed.csv", index=True)
        return True
    except:
        return False

# def manager(products_df):
#     result = clean_data(products_df=products_df)
#     json_data = json.dumps(result.to_dict(orient="records"), ensure_ascii=False).replace("\\/", "/")
#     print(json_data)
#     return store_csv_backup(result)