import pandas as pd

def extract_pl():
    head = pd.read_csv('../data/raw/amazon.csv', index_col=0)
    print(head)
    return head
