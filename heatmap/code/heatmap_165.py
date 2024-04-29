
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data processing
data = {"Organization": ["Red Cross", "Salvation Army", "United Way", "Habitat for Humanity"],
        "Donations (Millions)": [100, 75, 50, 25],
        "Volunteers (Thousands)": [50, 30, 25, 10],
        "Program Expenses (%)": [80, 85, 90, 80],
        "Fundraising Expenses (%)": [15, 10, 7, 10],
        "Administrative Expenses (%)": [5, 5, 3, 10]}

df = pd.DataFrame(data)
df.set_index("Organization", inplace=True)

# Setting figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Creating heatmap plot using ax
im = ax.imshow(df, cmap="coolwarm")

# Adding ticks and ticklabels
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor", wrap=True)
ax.set_yticklabels(df.index, rotation=0, ha="right", rotation_mode="anchor", wrap=True)

# Looping through data to show values in each cell
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        text = ax.text(j, i, df.iloc[i, j], ha="center", va="center", color="black")

# Setting title
ax.set_title("Charity and Nonprofit Data Overview")

# Adding colorbar
plt.colorbar(im)

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-131639_92.png", bbox_inches="tight")