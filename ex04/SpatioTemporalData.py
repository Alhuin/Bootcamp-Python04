import parent_import
import pandas as pd
from ex00.FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, data):
        self.data = data.filter(["Year", "City"])

    def when(self, location):
        return list(self.data.loc[self.data.City == location].Year.unique())

    def where(self, date):
        return list(self.data.loc[self.data.Year == date].City.unique())


def test_SpatioTemporalData():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.data)
    assert sp.where(1896) == ['Athina']
    assert sp.where(2016) == ['Rio de Janeiro']
    assert sp.when('Athina') == [2004, 1906, 1896]
    assert sp.when('Paris') == [1900, 1924]


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
