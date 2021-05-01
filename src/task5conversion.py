import pandas as pd
import json


def vis4ForTask5(csvPath: str, outJsonlPath: str, _index: str) -> None:
    """
    csv to jsonl conversion function for Task 5

    Parameters:
    csvPath (str): input csv path from the root dir
    outJsonlPath (str): output jsonl path
    _index (str): index name

    Returns:
    None: output jsonl
    """
    df = pd.read_csv(csvPath)
    with open(outJsonlPath, 'w') as outFile:
        for index, row in df.iterrows():
            json.dump({"index": {'_index':_index, '_id': index}}, outFile)
            outFile.write('\n')
            json.dump(row.to_dict(), outFile)
            outFile.write('\n')

def assignmentForTask5(jsonPath: str, outJsonlPath: str, _index: str) -> None:
    """
    json to jsonl conversion function for Task 5

    Parameters:
    jsonPath (str): input json path from the root dir
    outJsonlPath (str): output jsonl path
    _index (str): index name

    Returns:
    None: output jsonl
    """
    with open(jsonPath) as f:
        j = json.load(f)
        df = pd.DataFrame(j['Email'])
        df = df[[c for c in df.columns if c != '']]

    with open(outJsonlPath, 'w') as outFile:
        for index, row in df.iterrows():
            json.dump({"index": {'_index':_index, '_id': index}}, outFile)
            outFile.write('\n')
            json.dump(row.to_dict(), outFile)
            outFile.write('\n')

if __name__ == "__main__":
    vis4ForTask5('data/visualizations/vis4data.csv', "data/visualizations/vis4data.jsonl", "calendar")
    assignmentForTask5('data/json-converted/assignment-1/1-tsv-to-json.json', 'data/json-converted/assignment-1/1-for-task-5.jsonl', 'assignment1')
    assignmentForTask5('data/json-converted/assignment-2/2-tsv-to-json.json', 'data/json-converted/assignment-2/2-for-task-5.jsonl', 'assignment2')