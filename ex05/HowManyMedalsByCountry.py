import parent_import
from ex03.FileLoader import FileLoader


def count_medals(obj):
    medals = obj.value_counts().to_frame()["Medal"].to_dict()
    dic = {"Gold": 0, "Silver": 0, "Bronze": 0}
    dic.update(medals)
    dic["G"] = dic.pop("Gold")
    dic["S"] = dic.pop("Silver")
    dic["B"] = dic.pop("Bronze")
    return dic


def howManyMedalsByCountry(data, country_name):
    name_mask = (data.Team == country_name)
    by_name = data[name_mask] \
        .filter(items=["Year", "Medal", "Team", "City", "Event"])\
        .drop_duplicates(subset=['Team', 'City', 'Event'], keep='last')

    return by_name.pivot_table(
        index="Year",
        values="Medal",
        aggfunc=count_medals
    ).to_dict()["Medal"]


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    print(howManyMedalsByCountry(data, 'China'))
