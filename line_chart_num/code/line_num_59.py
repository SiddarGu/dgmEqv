
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(['2017', '2018', '2019', '2020'], [20, 25, 30, 35], label='Nuclear Energy(% of total energy)', marker='o')
plt.plot(['2017', '2018', '2019', '2020'], [5, 8, 9, 11], label='Wind Energy(% of total energy)', marker='o')
plt.plot(['2017', '2018', '2019', '2020'], [1, 3, 5, 7], label='Solar Energy(% of total energy)', marker='o')
plt.plot(['2017', '2018', '2019', '2020'], [10, 15, 20, 25], label='Hydroelectric Energy(% of total energy)', marker='o')

plt.title('Percentage of energy generated from different sources in Europe from 2017 to 2020', fontsize=20)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Percent of Total Energy', fontsize=15)

plt.xticks(['2017', '2018', '2019', '2020'], fontsize=12)
plt.yticks(fontsize=12)

for x, y in zip(['2017', '2018', '2019', '2020'], [20, 25, 30, 35]):
    label = "{:.0f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center', fontsize=12) # horizontal alignment can be left, right or center

for x, y in zip(['2017', '2018', '2019', '2020'], [5, 8, 9, 11]):
    label = "{:.0f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center', fontsize=12) # horizontal alignment can be left, right or center

for x, y in zip(['2017', '2018', '2019', '2020'], [1, 3, 5, 7]):
    label = "{:.0f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center', fontsize=12) # horizontal alignment can be left, right or center

for x, y in zip(['2017', '2018', '2019', '2020'], [10, 15, 20, 25]):
    label = "{:.0f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center', fontsize=12) # horizontal alignment can be left, right or center

plt.legend(loc='upper right')
plt.grid(linestyle='--')
plt.tight_layout()
plt.savefig("line chart/png/473.png")
plt.clf()