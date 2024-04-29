

import matplotlib.pyplot as plt
import numpy as np

Country = np.array (['USA', 'UK', 'Germany', 'France'])
Housing_Starts = np.array([1.5, 1.2, 1.4, 1.6])
Housing_Completions = np.array([2.3, 2.1, 2.2, 2.5])

# create figure
fig = plt.figure()
ax = fig.add_subplot(111)

# create bar chart
ax.bar(Country, Housing_Starts, label='Housing Starts (thousands)', color='b')
ax.bar(Country, Housing_Completions, bottom=Housing_Starts, label='Housing Completions (thousands)', color='r')

# add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)

# add title
plt.title("Housing Starts and Completions in four countries in 2021", fontsize=15)

# label the data points
for i in range(len(Country)):
    x_pos = Country[i]
    plt.annotate(Housing_Starts[i], xy=(x_pos, Housing_Starts[i]), ha='center', rotation=0, va='bottom')
    plt.annotate(Housing_Completions[i], xy=(x_pos, Housing_Completions[i]+Housing_Starts[i]), ha='center', rotation=0, va='bottom')

# use xticks to prevent interpolation
plt.xticks(Country)

# resize the figure
plt.tight_layout()

# save the figure
plt.savefig("Bar Chart/png/533.png")

# clear the current image state
plt.clf()