import pandas as pd
import numpy as np
import json

def vis4conversion(tsvToJsonPath: str) -> None:
    """
    Converts a data json file to a csv file for visualization 4 using d3: Calendar view
    Run this file in the root directory.
    See details for the d3 notebook: https://observablehq.com/@anthonyive/dsci-550-assignment-3-vis4
    """

    with open(tsvToJsonPath) as f:
        j = json.load(f)

    df = pd.DataFrame(j['Email'])
    
    df_new = df[['date', 'stock_close']].copy()
    df_new.columns = ['Date', "Close"]

    # replce empty strings with nan and drop them
    df_new['Close'].replace('', np.nan, inplace=True)
    df_new = df_new.dropna()

    # parse date to the right format and sort
    df_new['Date'] = pd.to_datetime(df_new['Date'])
    df_new = df_new.sort_values(by=['Date'])

    # make unique dates
    df_new['Close'] = df_new['Close'].astype(float)
    df_new = df_new.groupby(['Date']).mean()

    df_new.to_csv("data/visualizations/vis4/data.csv")


if __name__ == "__main__":
    vis4conversion("data/json-converted/assignment-1/1-tsv-to-json.json")