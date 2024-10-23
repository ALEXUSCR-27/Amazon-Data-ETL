import pandas as pd

def extract_f():
    head = pd.read_csv('./data/raw/amazon.csv')
    print(head.head())