
import matplotlib.pyplot as plt
import numpy as np

#set data
country = ['USA', 'UK', 'Germany', 'France']
voters = np.array([200000, 400000, 300000, 500000])
votes_cast = np.array([180000, 390000, 290000, 490000])
votes_counted = np.array([180000, 390000, 290000, 490000])

#create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

#plot data
ax.bar(country, voters, label='Voters', color='lightblue', width=0.5)
ax.bar(country, votes_cast, bottom=voters, label='Votes Cast',
       color='yellowgreen', width=0.5)
ax.bar(country, votes_counted, bottom=voters + votes_cast,
       label='Votes Counted', color='red', width=0.5)

#set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

#annotate values
for x, y, z in zip(country, voters, votes_counted):
    ax.text(x, y+z/2, '{:.0f}'.format(z), ha='center')

#set title
plt.title('Number of Voters, Votes Cast and Votes Counted in Four Countries in 2021')

#set xticks
ax.set_xticks(country)

#resize image
plt.tight_layout()

#save figure
plt.savefig('Bar Chart/png/141.png')

#clear image state
plt.clf()