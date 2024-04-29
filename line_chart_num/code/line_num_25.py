
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

ax = plt.subplot()

ax.plot(['India', 'China', 'Brazil', 'South Africa','France', 'Japan', 'United States'],
        [90, 95, 85, 80, 99, 100, 98],
        color='#ff7f50',
        linestyle='solid',
        marker='o',
        linewidth=2,
        markersize=8)

ax.plot(['India', 'China', 'Brazil', 'South Africa','France', 'Japan', 'United States'],
        [1000, 1200, 900, 500, 3000, 3500, 4000],
        color='#87ceeb',
        linestyle='dashed',
        marker='o',
        linewidth=2,
        markersize=8)

plt.title('Literacy rate and GDP per capita of selected countries in 2020')
ax.legend(['Literacy rate (%)', 'GDP per capita (USD)'])

for x,y in zip(['India', 'China', 'Brazil', 'South Africa','France', 'Japan', 'United States'],
               [90, 95, 85, 80, 99, 100, 98]):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,2), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x,y in zip(['India', 'China', 'Brazil', 'South Africa','France', 'Japan', 'United States'],
               [1000, 1200, 900, 500, 3000, 3500, 4000]):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,2), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(color='gray', linestyle='-', linewidth=0.5)
plt.savefig('line chart/png/320.png')
plt.clf()