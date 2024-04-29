
import matplotlib.pyplot as plt
import numpy as np

# data
age_group = ["0-17", "18-45", "46-65", "65+"]
percentage = [20, 35, 30, 15]

# create figure
fig = plt.figure(figsize=(7,7)) 

# plot
plt.pie(percentage, labels=age_group, autopct='%1.1f%%')

# set title
plt.title("Percentage Distribution of Healthcare Spending by Age Group in the USA, 2023")

# rotate the labels
plt.xticks(rotation=45)

# resize the chart
plt.tight_layout()

# save image
plt.savefig("pie chart/png/266.png")

# clear current image state
plt.clf()