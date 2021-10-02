import pandas as pd

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    data = pd.read(csv_file_path)
    ret = []
    for x in range(len(data)):
        for y in range(len(data[0])):
            ret[x][y] = data[x][y]
    return ret