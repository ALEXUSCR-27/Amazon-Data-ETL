import pandas as pd

def extract_pl():
    print("EXTRACTING DATA FROM CSV")
    products_df = pd.read_csv('./data/raw/amazon.csv', index_col=0)
    columns = (
        'product_name', 
        'category', 
        'discounted_price', 
        'actual_price', 
        'discount_percentage', 
        'rating', 
        'rating_count',
        'review_title',
        'img_link'
    )
    selected_columns = products_df.loc[:, columns]
    try:
        selected_columns.to_csv("./data/extracted/amazon_data_extracted.csv", index=True)
        return True
    except:
        return False
        