
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

labels = ['USA', 'UK', 'Germany', 'France']
Political_Parties = [4, 6, 5, 7]
Voters = [20000000, 30000000, 25000000, 27000000]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

ax.bar(x - width/2, Political_Parties, width, label='Political Parties', align='edge')
ax.bar(x + width/2, Voters, width, label='Voters', align='edge')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Parties and Voters')
ax.set_title('Number of Political Parties and Voters in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=45, ha="right", wrap=True)
ax.grid(linewidth=0.5)
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/239.png')
plt.clf()