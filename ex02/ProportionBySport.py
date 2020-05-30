import parent_import
from ex00.FileLoader import FileLoader


def proportionBySport(data, year, sport, gender):
    year_gender_mask = (data.Year == year) & (data.Sex == gender)
    by_year_gender = data[year_gender_mask].drop_duplicates("Name")

    sport_mask = by_year_gender.Sport == sport
    by_sport_year_gender = by_year_gender[sport_mask]

    if len(by_year_gender) != 0:
        return len(by_sport_year_gender) / len(by_year_gender)
    raise ZeroDivisionError


def test_proportionBySport():
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    assert 0.01935634328358209 == proportionBySport(data, 2004, 'Tennis', 'F')


