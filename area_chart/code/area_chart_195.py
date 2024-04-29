

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create dictionary with data
data = {"Year": [2015, 2016, 2017, 2018, 2019], "Healthcare Spending (in millions)": [3000, 3100, 3200, 3300, 3400], "Life Expectancy": [78, 79, 80, 81, 82]}

# convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# set figure size
plt.figure(figsize=(10, 6))

# set axes object
ax = plt.axes()

# calculate max total value and set y limit and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# plot area chart
ax.stackplot(df["Year"], df["Healthcare Spending (in millions)"], alpha=0.5, color="blue")
ax.stackplot(df["Year"], df["Life Expectancy"], alpha=0.5, color="green")

# set background grid lines
ax.grid(linestyle="--", linewidth=0.5, color="gray", alpha=0.3)

# set legend
ax.legend(["Healthcare Spending", "Life Expectancy"], loc="upper left")

# set x and y axis labels and title
ax.set_xlabel("Year")
ax.set_ylabel("Healthcare Spending (in millions), Life Expectancy")
ax.set_title("Healthcare Spending and Life Expectancy Trends")

# automatically resize image
plt.tight_layout()

# save figure
plt.savefig("output/final/area_chart/png/20231228-145339_29.png", bbox_inches="tight")

# clear current image state
plt.clf()