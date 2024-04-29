
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

month = ['January','February','March','April','May']
coffee = [200,300,500,400,600]
tea = [300,400,600,500,700]
milk = [400,500,700,600,800]
soda = [500,600,800,700,900]

ax.plot(month, coffee, color='green',label='Coffee')
ax.plot(month, tea, color='blue',label='Tea')
ax.plot(month, milk, color='red',label='Milk')
ax.plot(month, soda, color='orange',label='Soda')

ax.set_title('Monthly Consumption of Selected Beverages in 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Cups')

for x,y in zip(month,coffee):
    label = "{:.0f}".format(y)
    ax.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

for x,y in zip(month,tea):
    label = "{:.0f}".format(y)
    ax.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

for x,y in zip(month,milk):
    label = "{:.0f}".format(y)
    ax.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

for x,y in zip(month,soda):
    label = "{:.0f}".format(y)
    ax.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

ax.legend(loc='upper left', bbox_to_anchor=(1,1))
ax.grid()

plt.xticks(month)
fig.tight_layout()

plt.savefig('line chart/png/119.png')
plt.clf()