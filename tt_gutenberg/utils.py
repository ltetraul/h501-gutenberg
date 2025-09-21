import pandas as pd

def sort_by_translations(df):
    #sort dataframe of authors by translation_count in descending order
    return df.sort_values(by="translation_count", ascending=False)