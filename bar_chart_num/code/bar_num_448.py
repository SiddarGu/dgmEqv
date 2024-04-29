
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8)) 
ax = fig.add_subplot()

# data
country = ['USA', 'UK', 'Germany', 'France']
literacy_rate = [98, 95, 99, 97]
population = [330, 67, 83, 67]

# plot
bar_width = 0.4
ax.bar(country, literacy_rate, bar_width, color='#FFA500', label='Literacy Rate')
ax.bar(country, population, bar_width, bottom=literacy_rate, color='#87CEFA', label='Population')

# legend
plt.legend(loc='upper left')

# annotate
for a, b in zip(country, literacy_rate):
    plt.text(a, b + 0.5, '%.0f' % b, ha='center', va='bottom', fontsize=12)
for a, b in zip(country, population):
    plt.text(a, b + 0.5, '%.0f' % b, ha='center', va='bottom', fontsize=12)

# axis
plt.xticks(country)
plt.yticks(np.arange(0, 400, 50))
plt.xlabel('Country')
plt.ylabel('Percentage')

# title
plt.title('Literacy Rate and Population of four countries in 2021')

# adjust the layout
plt.tight_layout()

# save the image
plt.savefig('Bar Chart/png/201.png')

# clear the current image state
plt.clf()