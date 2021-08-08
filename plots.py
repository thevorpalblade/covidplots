import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#covid deaths dataset
cd_dataset = pd.read_csv("Provisional_COVID-19_Deaths_by_Week__Sex__and_Age.csv")
cd_unisex = cd_dataset[cd_dataset["Sex"] == "All Sex"]
cd_usa = cd_unisex[cd_unisex["State"] == "United States"]

#excess deaths dataset
ed_dataset = pd.read_csv("Excess_Deaths_Associated_with_COVID-19.csv")


age_groups = [#'All Ages',
#               'Under 1 year',
#               '1-4 Years',
#               '5-14 Years',
#               '15-24 Years',
#               '25-34 Years',
              '35-44 Years'
              # '45-54 Years',
              # '55-64 Years',
              # '65-74 Years',
              # '75-84 Years',
              # '85 Years and Over'
              ]
cd_usa["End Week"] = pd.to_datetime(cd_usa["End Week"], format='%m/%d/%Y')
weeks = cd_usa["End Week"].unique()

for age in age_groups:
    df = cd_usa[cd_usa["Age Group"] == age]
    df.set_index(['End Week'], inplace=True)
    plt.plot(df.index, df["Total Deaths"], label="Total Deaths " + age)
    plt.plot(df.index, df["COVID-19 Deaths"], label='COVID Deaths ' + age)
    
plt.legend()

