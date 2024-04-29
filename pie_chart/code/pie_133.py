
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.figure(figsize=(10,7))
plt.title("Distribution of Sports and Entertainment Segments in the US, 2023")

segments = ["Professional Sports", "Amateur Sports", "Music", "Television and Film", "Other"]
percentage = [35, 25, 20, 15, 5]

plt.pie(percentage, labels=segments, autopct='%.2f%%', textprops={'fontsize': 12})

plt.tight_layout()
plt.savefig("pie chart/png/264.png")
plt.clf()