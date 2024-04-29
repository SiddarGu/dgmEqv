
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 8))
ax = plt.subplot()

data = [[2001, 25, 20, 30, 25], 
        [2002, 26, 19, 31, 24], 
        [2003, 25, 20, 32, 23], 
        [2004, 24, 21, 31, 24]]

years = [x[0] for x in data]

ax.plot(years, [x[1] for x in data], label='Public Education')
ax.plot(years, [x[2] for x in data], label='Military')
ax.plot(years, [x[3] for x in data], label='Health Care')
ax.plot(years, [x[4] for x in data], label='Social Security')

plt.title('Government Spending on Key Sectors in the US from 2001 to 2004')
plt.ylabel('Percentage of Budget (%)')
plt.xlabel('Year')

ax.xaxis.set_ticks(years)

for x, y in zip(years, [x[1] for x in data]):
    label = "{:.0f}".format(y)
    ax.annotate(label, # this is the text
                (x,y), # this is the point to label
                textcoords="offset points", # how to position the text
                xytext=(0,2), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center

for x, y in zip(years, [x[2] for x in data]):
    label = "{:.0f}".format(y)
    ax.annotate(label, # this is the text
                (x,y), # this is the point to label
                textcoords="offset points", # how to position the text
                xytext=(0,2), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center

for x, y in zip(years, [x[3] for x in data]):
    label = "{:.0f}".format(y)
    ax.annotate(label, # this is the text
                (x,y), # this is the point to label
                textcoords="offset points", # how to position the text
                xytext=(0,2), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center

for x, y in zip(years, [x[4] for x in data]):
    label = "{:.0f}".format(y)
    ax.annotate(label, # this is the text
                (x,y), # this is the point to label
                textcoords="offset points", # how to position the text
                xytext=(0,2), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center

plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/532.png')
plt.clf()