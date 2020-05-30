import parent_import
from ex00.FileLoader import FileLoader


def count_medals(obj):
    medals = obj.value_counts().to_frame()["Medal"].to_dict()
    dic = {"Gold": 0, "Silver": 0, "Bronze": 0}
    dic.update(medals)
    dic["G"] = dic.pop("Gold")
    dic["S"] = dic.pop("Silver")
    dic["B"] = dic.pop("Bronze")
    return dic


def howManyMedals(data, name):
    by_name = data[data.Name == name]

    if len(by_name) > 0:
        return by_name.pivot_table(
            index="Year",
            values="Medal",
            aggfunc=count_medals
        ).to_dict()["Medal"]
    return {}


def test_howManyMedals():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    assert howManyMedals(data, 'Kjetil Andr Aamodt') == dict({
        1992: {'G': 1, 'S': 0, 'B': 1},
        1994: {'G': 0, 'S': 2, 'B': 1},
        1998: {'G': 0, 'S': 0, 'B': 0},
        2002: {'G': 2, 'S': 0, 'B': 0},
        2006: {'G': 1, 'S': 0, 'B': 0}
    })


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    print(howManyMedals(data, 'Kjetil Andr Aamodt'))
