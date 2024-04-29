
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(111)

labels = ['Revenue','Expense','Profit']

year = [2001, 2002, 2003, 2004]
Revenue = [1000, 1200, 800, 1500]
Expense = [800, 900, 1100, 1200]
Profit = [200, 300, -300, 300]

ax1.plot(year, Revenue, label='Revenue', color='green')
ax1.plot(year, Expense, label='Expense', color='red')
ax1.plot(year, Profit, label='Profit', color='blue')

plt.xticks(year)

ax1.set_title('Financial Performance of Company XYZ in 2001-2004')
ax1.set_xlabel('Year')
ax1.set_ylabel('Costs in Billion Dollars')

ax1.legend(labels, loc='upper left', fontsize='small')

for x, y in zip(year, Revenue):
    label = '{}'.format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center', wrap=True) # horizontal alignment can be left, right or center

for x, y in zip(year, Expense):
    label = '{}'.format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center', wrap=True) # horizontal alignment can be left, right or center

for x, y in zip(year, Profit):
    label = '{}'.format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center', wrap=True) # horizontal alignment can be left, right or center
    
plt.tight_layout()
fig.savefig('line chart/png/399.png')
plt.cla()