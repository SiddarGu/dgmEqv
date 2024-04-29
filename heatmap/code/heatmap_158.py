
           
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data
data = {"Country": ["USA", "Japan", "Germany", "France", "UK", "Canada"],
        "Number of Schools": [1000, 500, 300, 200, 400, 100],
        "Number of Students": [1000000, 500000, 300000, 200000, 400000, 100000],
        "Number of Teachers": [50000, 30000, 20000, 15000, 25000, 10000],
        "Student-Teacher Ratio": [20, 17, 15, 13, 16, 10],
        "Education Spending (Millions)": [20000, 15000, 10000, 8000, 12000, 5000]}

# Convert data into pandas dataframe
df = pd.DataFrame(data)

# Set figure size and font size
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["font.size"] = 12

# Create heatmap chart using seaborn
sns.heatmap(df.iloc[:, 1:], annot=True, cmap="Blues", fmt="g", cbar=False)

# Set x and y ticks and ticklabels
plt.xticks(np.arange(5)+0.5, df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
plt.yticks(np.arange(6)+0.5, df["Country"], rotation=0, ha="center")

# Add title
plt.title("Education Statistics by Country")

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-131639_83.png", bbox_inches="tight")

# Clear current image state
plt.clf()