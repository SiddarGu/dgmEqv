
import matplotlib.pyplot as plt
import matplotlib as mpl

#set font size
mpl.rcParams['font.size'] = 12

# Create figure
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1,1,1)

#get the data
year = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
carbon_dioxide_level = [400, 425, 450, 475, 500, 525, 550]
nitrous_oxide_level = [200, 225, 250, 275, 300, 325, 350]

#plot the data
ax.plot(year, carbon_dioxide_level, label='Carbon Dioxide Level')
ax.plot(year, nitrous_oxide_level, label='Nitrous Oxide Level')

#set x axis
ax.set_xticks(year)

#add label
ax.set_title('Air Pollution Levels in the United States from 2000 to 2006')
ax.set_xlabel('Year')
ax.set_ylabel('Level')

#add legend
ax.legend(loc='best', fontsize='medium')

#resize
plt.tight_layout()

#save the figure
plt.savefig('line chart/png/3.png')

#clear
plt.clf()