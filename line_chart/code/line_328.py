
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(10,6))

data = [[2001,10,80,90],[2002,8,85,93],[2003,7,90,95],[2004,4,92,97]]
col_name = ["Year","Dropout rate(%)","Graduation rate(%)","Enrollment rate(%)"]

df = pd.DataFrame(data, columns=col_name)

plt.plot(df["Year"], df["Dropout rate(%)"], label="Dropout rate(%)", marker="o")
plt.plot(df["Year"], df["Graduation rate(%)"], label="Graduation rate(%)", marker="o")
plt.plot(df["Year"], df["Enrollment rate(%)"], label="Enrollment rate(%)", marker="o")

plt.xticks(df["Year"], rotation=90)
plt.title("Changes in Education Indicators in the United States from 2001 to 2004")
plt.xlabel("Years")
plt.ylabel("Rate(%)")
plt.legend(loc="best", ncol=2, frameon=True)

plt.tight_layout()
plt.savefig('line chart/png/273.png')
plt.clf()