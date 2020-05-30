import parent_import
from ex00.FileLoader import FileLoader
from pprint import pprint


def howManyMedals(data, name):
    ret = dict()
    name_mask = (data.Name == name)
    by_name = data[name_mask] \
        .filter(items=["Year", "Medal"])

    for idx, da in by_name.iterrows():
        if da.Year not in ret:
            ret[da.Year] = dict({'Gold': 0, 'Silver': 0, 'Bronze': 0})
        if da.Medal in ["Gold", "Silver", "Bronze"]:
            ret[da.Year][da.Medal] += 1
    return ret


def test_howManyMedals():
    loader = FileLoader()
    data = loader.load("https://raw.githubusercontent.com/42-AI"
                       "/bootcamp_python/master/day04/resources"
                       "/athlete_events.csv")

    assert howManyMedals(data, 'Kjetil Andr Aamodt') == dict({
        1992: {'Gold': 1, 'Silver': 0, 'Bronze': 1},
        1994: {'Gold': 0, 'Silver': 2, 'Bronze': 1},
        1998: {'Gold': 0, 'Silver': 0, 'Bronze': 0},
        2002: {'Gold': 2, 'Silver': 0, 'Bronze': 0},
        2006: {'Gold': 1, 'Silver': 0, 'Bronze': 0}
    })


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("https://raw.githubusercontent.com/42-AI"
                       "/bootcamp_python/master/day04/resources"
                       "/athlete_events.csv")
    pprint(howManyMedals(data, 'Kjetil Andr Aamodt'))
