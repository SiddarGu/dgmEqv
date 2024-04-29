
import matplotlib.pyplot as plt
import numpy as np

types = ["Automotive", "Aerospace", "Electronics", "Food and Beverage", "Pharmaceuticals", "Metals", "Textiles", "Plastics", "Other"]
percentage = [18, 17, 19, 15, 12, 12, 8, 7, 2]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

ax.pie(percentage, labels=types, autopct='%1.1f%%', startangle=90, rotatelabels=True, textprops={'fontsize': 10})
ax.set_title("Global Distribution of Manufacturing Industries in 2023")
ax.legend(loc="upper left", bbox_to_anchor=(1,1))

plt.tight_layout()
plt.savefig('pie chart/png/161.png')
plt.clf()