
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# define data as dict
data = {"Organization": ["Red Cross", "Salvation Army", "Habitat for Humanity", "Doctors Without Borders", "World Wildlife Fund"],
        "Donations (USD)": [10000000, 5000000, 3000000, 8000000, 6000000],
        "Volunteers": [500, 250, 100, 200, 150],
        "Programs": [1000000, 750000, 500000, 1500000, 1000000],
        "Fundraising Expenses (USD)": [1000000, 750000, 500000, 1500000, 1000000],
        "Administrative Expenses (USD)": [250000, 200000, 150000, 300000, 250000]}

# convert data to pandas dataframe
df = pd.DataFrame(data)

# set index as organization
df = df.set_index("Organization")

# plot heatmap chart using seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap="Blues", cbar=False)

# set x and y ticks labels
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.index, rotation=0, ha="right", rotation_mode="anchor")

# set ticks and ticklabels in the center of rows and columns
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)

# add title
plt.title("Charitable Contributions and Expenses")

# automatically resize image
plt.tight_layout()

# save figure
plt.savefig("output/final/heatmap/png/20231228-155147_46.png", bbox_inches="tight")

# clear current image state
plt.clf()