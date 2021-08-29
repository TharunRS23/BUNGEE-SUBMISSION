
import pandas as pd
data = pd.read_csv("C:\\Users\\HP\\Desktop\\input.csv")
data = data[data['COUNTRY'].str.contains("USA")]
print(data)
data.to_csv("C:\\Users\\HP\\Desktop\\filteredcountry.csv")


