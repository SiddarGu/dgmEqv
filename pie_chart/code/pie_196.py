
import matplotlib.pyplot as plt
import numpy as np

labels = ["0-17","18-34","35-49","50-64","65+"]
sizes = [17,25,23,24,11]

plt.figure(figsize=(10,10))
plt.subplot()

plt.pie(sizes, labels=labels, autopct='%1.1f%%',startangle=90,pctdistance=0.85)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.tight_layout()
plt.title("Healthcare Usage Distribution by Age Group in the USA, 2023")

plt.savefig("pie chart/png/444.png",bbox_inches="tight")
plt.clf()