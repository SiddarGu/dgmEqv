
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Convert data into a dictionary
data = {"Country":["United States", "China", "Japan", "United Kingdom", "Germany", "France", "Brazil", "India", "Russia"],
        "Internet Speed (Mbps)":[150,100,200,120,130,140,90,80,110],
        "Mobile Data Usage (GB)":[10,15,8,12,9,11,5,4,6],
        "Smartphone Penetration (%)":[80,60,70,75,65,70,50,40,55],
        "E-commerce Sales (Billion USD)":[700,600,500,800,750,650,200,150,250],
        "Social Media Users (Millions)":[250,350,150,200,180,160,100,200,120]}

# Convert data into a dataframe
df = pd.DataFrame(data)
df = df.set_index('Country')

# Set figure size
plt.figure(figsize=(10,7))

# Plot the heatmap
heatmap = sns.heatmap(df, annot=True, cmap="YlGnBu", linewidths=.5)

# Make ticks and ticklabels in the center of rows and columns
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
heatmap.set_yticklabels(heatmap.get_yticklabels())

# Add title
plt.title('Technology and Internet Adoption by Country')

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('output/final/heatmap/png/20231228-134212_54.png', bbox_inches='tight')

# Clear the current image state
plt.clf()