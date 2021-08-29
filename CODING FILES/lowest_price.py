# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd

data = pd.read_csv("C:\\Users\\HP\\Desktop\\filteredCountry.csv", usecols=["SKU","PRICE"])
df = data.groupby('SKU').min()["PRICE"]
print(df)
df.to_csv("C:\\Users\\HP\\Desktop\\Lowest_Price.csv")


