
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# create dictionary with data
data_dict = {
    "Department" : ['Sales', 'Marketing', 'Finance', 'IT', 'Human Resources'],
    "Number of Employees" : [250, 200, 180, 150, 100],
    "Total Compensation ($)" : [4.5, 3.8, 3.5, 4.0, 2.5],
    "Avg. Salary ($)" : [50, 45, 55, 65, 45],
    "Years of Experience" : [5.2, 4.8, 6.0, 7.2, 5.5],
    "Training Hours" : [32, 25, 28, 35, 40]
}

# convert dictionary to dataframe
df = pd.DataFrame(data_dict)

# set figure size
plt.figure(figsize=(10,6))

# plot heatmap chart using seaborn
ax = sns.heatmap(df.iloc[:,1:], annot=True, cmap="YlGnBu")

# set x and y axis ticks and tick labels
ax.set_xticks(np.arange(0.5, 5.5, 1))
ax.set_xticklabels(df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(np.arange(0.5, 5.5, 1))
ax.set_yticklabels(df.iloc[:,0], rotation=0, wrap=True)

# set ticks in the center of rows and columns
ax.set_xticks(np.arange(df.shape[1]), minor=True)
ax.set_yticks(np.arange(df.shape[0]), minor=True)
ax.tick_params(which="minor", bottom=False, left=False)
ax.grid(which="minor", color="gray", linestyle="-", linewidth=1)

# set title
plt.title("Employee Metrics by Department")

# resize image and save
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-134212_94.png", bbox_inches="tight")

# clear current image state
plt.clf()