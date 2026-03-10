import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("vnv1.xlsx", header=2)
df = df.dropna(axis=1, how="all")


print(df.head())
print(df["FINAL STATUS"].value_counts())
print(df["REJECT REASON"].value_counts())
print(df["EXE NAME"].value_counts())
print(df["PRODUCT"].value_counts())
print(df["PRICE"].value_counts().sort_values())
print(df["DATE"].value_counts())


sns.countplot(x= "FINAL STATUS", data=df)
plt.title("approvel vs reject")
plt.show()

sns.countplot(x= "REJECT REASON", data=df)
plt.title("reject reason")
plt.show()

sns.countplot(x="EXE NAME", data=df)
plt.title("exe performance")
plt.show()

sns.countplot(x="PRODUCT", data=df)
plt.title("hiegh sale product")
plt.show()

sns.countplot(x="PRICE", data=df)
plt.title("hiegh prices no of sale")
plt.show()
