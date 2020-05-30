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


def howManyMedalsByCountry(data, country_name):
    by_country = data[data.Team == country_name] \
        .filter(items=["Year", "Medal", "Team", "City", "Event"])\
        .drop_duplicates(subset=['Team', 'City', 'Event'], keep='last')

    if len(by_country) > 0:
        return by_country.pivot_table(
            index="Year",
            values="Medal",
            aggfunc=count_medals
        ).to_dict()["Medal"]
    return {}


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    print(howManyMedalsByCountry(data, 'China'))
