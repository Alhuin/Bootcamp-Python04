import pandas as pd
import numpy as np

famille_panda = [
    [100, 5, 20, 80],
    [50, 2.5, 10, 40],
    [110, 6, 22, 80],
]

print("\n---------RAW FAMILY---------\n")
print(famille_panda)
famille_panda_numpy = np.array(famille_panda)
print("\n---------NUMPY FAMILY---------\n")
print(famille_panda_numpy)
famille_panda_df = pd.DataFrame(
    famille_panda,
    index=["maman", "bebe", "papa"],
    columns=["pattes", "poil", "cheveux", "ventre"]
)
print("\n---------PANDAS FAMILY---------\n")
print(famille_panda_df)
print("\n---------Get Ventre\n")
print(famille_panda_df.ventre)
print("\n---------As np array\n")
print(famille_panda_df.ventre.values)
print("\n---------Iter rows\n")
for row_idx, row_data in famille_panda_df.iterrows():
    print(f"Voici le panda {row_idx} :")  # as str
    print(row_data)
    print("--------------------")
print("\n---------Get Maman\n")
print(famille_panda_df.loc["maman"])
print("\n---------For each, check Panda.ventre == 80 ?\n")
print(famille_panda_df.ventre == 80)
print("\n---------Filter pandas from mask (ventre == 80)\n")
mask = famille_panda_df.ventre == 80
pandas_ventre_80 = famille_panda_df[mask]
print(pandas_ventre_80)
print("\n---------Filter pandas from reversed mask (~ventre == 80)\n")
not_pandas_ventre_80 = famille_panda_df[~mask]
print(not_pandas_ventre_80)
print("\n---------Append DataFrames\n")
quelques_pandas = pd.DataFrame([[105, 4, 19, 80], [100, 5, 20, 80]],
                               columns=famille_panda_df.columns)
print("To append to Pandas Family with same columns:")
print(quelques_pandas)
tous_les_pandas = famille_panda_df.append(quelques_pandas)
print("New DataFrame:")
print(tous_les_pandas)
print("\n---------Drop duplicates\n")
without_dups = tous_les_pandas.drop_duplicates()  # new DataFrame
print("DF copy without dups:")
print(without_dups)
print('Original DF:')
print(tous_les_pandas)
print("\n---------Get Header\n")
print(famille_panda_df.columns)
print("\n---------Add column from list\n")
column_to_add = ["f", "f", "m"]
print("Column to add : sex ")
print(column_to_add)
famille_panda_df["sexe"] = column_to_add
print("With new column:")
print(famille_panda_df)
print("\n---------Get nb_rows\n")
print(len(famille_panda_df))
print("\n---------Get unique values in column: \n")
print("ventre uniques :")
print(famille_panda_df.ventre.unique())
print("sexe uniques :")
print(famille_panda_df.sexe.unique())

print("\n---------READ CSV---------: \n")
athletes_data = pd.read_csv("https://raw.githubusercontent.com/42-AI"
                            "/bootcamp_python/master/day04/resources"
                            "/athlete_events.csv", sep=",")
print("---------Atheletes.csv data from url")
print(athletes_data)

print("\n---------Get 5 first rows: \n")
print(athletes_data.head())
print("\n---------Get 5 last rows: \n")
print(athletes_data.tail())
print("\n---------Describe Athletes stats: \n")
print(athletes_data.describe(include="all"))
print("\n---------Rename Age to vieilesse: fixed \n")
print(athletes_data.rename(columns={"Age": "Vielliesse"}))
print("\n---------Change line index: lambda \n")
f = lambda x: x + 1
print(athletes_data.rename(index=f).head())
print("\n---------Drop row: index O \n")
print(athletes_data.head().drop(0))
print("\n---------Drop column: Age \n")
print(athletes_data.head().drop(columns=["Age"]))

print("\n---------Nan handling---------: \n")

print("\n---------Column head with Nan: Weight = \n")
print(athletes_data.Weight.head())
print("\n---------Head with Weight Nan replaced by 0:\n")
print(athletes_data.fillna(value={"Weight": 0}).head())
print("\n---------Head with all Nan replaced by prev value:\n")
print(athletes_data.fillna(method="pad").head())
print("\n---------Head with lines with Nan dropped: \n")
print(athletes_data.dropna().head())
print("\n---------Head with column with with Nan dropped: \n")
print(athletes_data.dropna(axis="columns").head())

print("\n---------Crossed dynamic tables---------: \n")
print(athletes_data.pivot_table(index="Sex", columns='Sport', aggfunc="count"))
