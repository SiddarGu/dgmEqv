
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Set the figure size, without overlapping and cutting
plt.figure(figsize=(8, 6))

# set the data
labels = ['Google', 'Apple', 'Amazon', 'Microsoft', 'Facebook', 'Other']
sizes = [25, 20, 20, 15, 10, 10]

# Set the colors
colors = ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#ffffcc']

# draw and save the pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title("Market Share of Leading Tech Platforms in 2023")
plt.tight_layout()
for i, l in enumerate(labels):
    plt.text(-0.5, -0.1+i*0.05, l, rotation=45, wrap=True)
plt.xticks(())
plt.savefig('pie chart/png/478.png')
plt.clf()