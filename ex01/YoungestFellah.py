import parent_import
from ex00.FileLoader import FileLoader


def youngestFellah(pandas_df, year):
    year_mask = pandas_df.Year == year
    by_year = pandas_df[year_mask]
    male_mask = by_year.Sex == "M"

    return {
        'f': by_year[~male_mask].Age.min(),
        'm': by_year[male_mask].Age.min(),
    }


def test_youngestFellah():
    fl = FileLoader()
    data = fl.load("https://raw.githubusercontent.com/42-AI"
                   "/bootcamp_python/master/day04/resources"
                   "/athlete_events.csv")

    assert dict({'f': 13.0, 'm': 14.0}) == youngestFellah(data, 2004)


