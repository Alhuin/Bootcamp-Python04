import sys
import pandas as pd


class FileLoader:
    @staticmethod
    def load(path):
        pandas_df = pd.read_csv(path, sep=",", index_col=0)
        features = pandas_df.columns
        height, width = len(pandas_df), len(features)
        print(f"Loading dataset of dimensions {height} x {width}")
        return pandas_df

    @staticmethod
    def display(df, n):
        print(df.head(n) if n >= 0 else df.tail(-n))


if __name__ == "__main__":
    fl = FileLoader()
    try:
        dataSet = fl.load("https://raw.githubusercontent.com/42-AI"
                          "/bootcamp_python/master/day04/resources"
                          "/athlete_events.csv")
    except ValueError as e:
        sys.exit("ValueError: " + str(e))
    except FileNotFoundError as e:
        sys.exit("FileNotFoundError: " + str(e))
    # fl.display(dataSet, 5)
    fl.display(dataSet, -5)
    # fl.display(dataSet, 0)
