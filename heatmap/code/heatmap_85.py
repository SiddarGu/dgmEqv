

            

# import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# create the data dictionary
data = {"Category": ["Clothing", "Electronics", "Beauty", "Books", "Home Goods"], 
        "Conversions (%)": [4, 6, 8, 7, 5], 
        "Click-through Rate (%)": [2, 4, 6, 5, 3], 
        "Average Order Value ($)": [65, 120, 80, 90, 100], 
        "Cart Abandonment Rate (%)": [20, 15, 18, 17, 19], 
        "Customer Retention Rate (%)": [50, 60, 55, 57, 52]
       }

# convert the data into a pandas dataframe
df = pd.DataFrame(data)

# set the figure size
plt.figure(figsize=(10, 8))

# plot the heatmap using seaborn
sns.heatmap(df.iloc[:, 1:], annot=True, cmap='Blues')

# set the ticks and ticklabels for x and y axis
plt.xticks(np.arange(5) + 0.5, labels=df.columns[1:], rotation=45, ha="right", rotation_mode="anchor")
plt.yticks(np.arange(5) + 0.5, labels=df["Category"], rotation=0, ha="right", rotation_mode="anchor")

# add a title
plt.title("E-commerce Metrics by Product Category")

# automatically resize the image
plt.tight_layout()

# save the image
plt.savefig("output/final/heatmap/png/20231228-124154_8.png", bbox_inches='tight')

# clear the current image state
plt.clf()