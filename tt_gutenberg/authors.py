import pandas as pd
from .utils import sort_by_translations

def list_authors(by_languages=True, alias=True):
    """
    Returns a list of author aliases ordered by number of translations.
    """
    #load dataset
    df = pd.read_csv("gutenberg_authors.csv")

    #keep only valid alias rows
    df = df[df["alias"].notnull()]

    #count translations
    counts = df.groupby("alias").size().reset_index(name="translation_count")

    #sort using utils function
    sorted_df = sort_by_translations(counts)

    return sorted_df["alias"].tolist()
