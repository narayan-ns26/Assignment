#importing libraries
import pandas  as pd
import numpy as np


#collecting dataset
city_dataset = pd.read_csv("cities.csv")

#slicing city name from the city_dataset
city_column = city_dataset.name_of_city

#slicing population from the city_dataset
population_column = city_dataset.population_total

#concating two columns
dataset = pd.concat([city_column,population_column], axis=1, ignore_index=True)
dataset

#renaming the columns
dataset.columns = ['City', 'Population']
dataset

#traversing the dataframe and list out the cities of population greater than 5lakhs
for i in range(len(dataset)):
    if(dataset.iloc[i, 1]>500000):
        print(dataset.iloc[i, 0],dataset.iloc[i, 1])

print(" ")