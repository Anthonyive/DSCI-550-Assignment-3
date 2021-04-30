import pandas as pd
import json


def vis4ForTask5(csvPath: str) -> None:
    """
    csv to jsonl function for Task 5

    Parameters:
    csvPath (str): input csv path from the root dir

    Returns:
    None: output vis4data.jsonl in data/visualizations
    """
    df = pd.read_csv(csvPath)
    with open("data/visualizations/vis4data.jsonl", 'w') as outFile:
        for index, row in df.iterrows():
            json.dump({"index": {'_index':'vis4CalendarView', '_id': index}}, outFile)
            outFile.write('\n')
            json.dump(row.to_dict(), outFile)
            outFile.write('\n')

if __name__ == "__main__":
    vis4ForTask5('data/visualizations/vis4data.csv')