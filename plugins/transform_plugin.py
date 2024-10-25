from utils.data_formatter import data_formatter

def clean_data(products_df):
    columns = (
        'product_name', 
        'category', 
        'discounted_price', 
        'actual_price', 
        'discount_percentage', 
        'rating', 
        'rating_count',
        'user_name',
        'review_title',
        'img_link'
    )
    selected_columns = products_df.loc[:, columns]
    selected_columns.drop_duplicates(inplace=True)
    selected_columns.dropna(inplace=True)

    selected_columns['discounted_price'] = (selected_columns['discounted_price'].apply(data_formatter.clean_prices).astype('float'))
    selected_columns['actual_price'] = (selected_columns['actual_price'].apply(data_formatter.clean_prices).astype('float'))
    selected_columns['discount_percentage'] = (selected_columns['discount_percentage'].apply(data_formatter.clean_percentages).astype('float'))
    selected_columns['rating'] = selected_columns['rating'].apply(data_formatter.clean_ratings).astype(float)
    selected_columns['rating_count'] = selected_columns['rating_count'].apply(data_formatter.clean_rating_count).astype(float)


    print(selected_columns['rating_count'].apply(type).value_counts())
    print(selected_columns['rating_count'])



def manager(products_df):
    clean_data(products_df=products_df)