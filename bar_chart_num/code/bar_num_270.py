
import matplotlib.pyplot as plt
import numpy as np

#create figure
fig = plt.figure(figsize=(8, 6))

#set up data
data = [['USA', 325, 350], 
        ['UK', 90, 160],
        ['Germany', 80, 120],
        ['France', 66, 115]]

#create bar chart
x_positions = np.arange(len(data))
bar_width = 0.25

#plot bar
plt.bar(x_positions, [i[1] for i in data], width=bar_width, label='Internet Users')
plt.bar(x_positions + bar_width, [i[2] for i in data], width=bar_width, label='Smartphones')

#set x-axis
plt.xticks(x_positions + bar_width/2, [i[0] for i in data])

#set title
plt.title('Number of Internet Users and Smartphones in four countries in 2021')

#display legend
plt.legend(loc='best')

#display value
for x, y, z in zip(x_positions, [i[1] for i in data], [i[2] for i in data]):
    plt.annotate(str(y)+'\n'+str(z), xy=(x, y), xytext=(0, 5), 
                 textcoords='offset points',
                 ha='center', va='bottom')

#resize the image
plt.tight_layout()

#save the figure
plt.savefig('Bar Chart/png/197.png')

#clear the current image state
plt.clf()