
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Online_Users = [350,400,320,400]
Online_Searches = [600,650,550,800]

fig, ax = plt.subplots(figsize=(10,5))
ax.bar(Country,Online_Users, label='Online Users(million)', color='blue')
ax.bar(Country,Online_Searches, bottom=Online_Users, label='Online Searches', color='orange')
ax.set_xticklabels(Country, rotation=0, wrap=True)
ax.set_title('Number of online users and searches in four countries in 2021')
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('bar chart/png/207.png')
plt.clf()