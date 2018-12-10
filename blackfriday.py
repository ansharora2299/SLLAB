import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

black_df = pd.read_csv("BlackFriday.csv")

print("======Data Headers=======")
black_df.head()

print("=====Data Decription=====")
black_df.info()
black_df.describe()

black_df = black_df.drop(['User_ID', 'Product_ID', 'Stay_In_Current_City_Years'], axis=1)
black_df.head()

black_df["City_Category"] = black_df["City_Category"].fillna("B")
print(black_df["City_Category"])

black_df["City_Category"] = black_df['City_Category'].map({
    "A": "Metro Cities",
    "B": "Small Towns",
    "C": "Villages"
})

print(black_df.head(10))

black_df["Marital_Status"] = black_df['Marital_Status'].map({
    1: "Married",
    0: "Un-married"
})

print(black_df.head(10))
ax = sns.countplot(x="City_Category", hue="Gender", palette="Set1", data=black_df)
ax.set(title="City Category", xlabel="Categories", ylabel="Total")
plt.show()