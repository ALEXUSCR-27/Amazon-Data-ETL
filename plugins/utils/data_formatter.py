class data_formatter:

    def __init__(self) -> None:
        pass
    
    def clean_prices(
    price_value: object
    ):
        if (isinstance(price_value, str)):
            return (price_value.replace('₹', '').replace(',',''))
        return price_value

    def clean_percentages(
        percentage: object
    ):
        if (isinstance(percentage, str)):
            temp = (percentage.replace('%', '').replace(',',''))
            return float(temp)/100
        return percentage

    def clean_ratings(rating):
        try:
            return float(rating)
        except:
            return '0'
    
    def clean_rating_count(rating_count):
        if (isinstance(rating_count, str)):
            return (rating_count.replace(',',''))
        return rating_count
    
        