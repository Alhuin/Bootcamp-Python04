import parent_import
import numpy as np
from ex00.FileLoader import FileLoader


def youngestFellah(data, year):
    return data[data.Year == year].pivot_table(
        index="Sex",
        values="Age",
        aggfunc=np.min
    ).to_dict()["Age"]


def test_youngestFellah():
    fl = FileLoader()
    data = fl.load('../data/athlete_events.csv')
    assert dict({'F': 13.0, 'M': 14.0}) == youngestFellah(data, 2004)
