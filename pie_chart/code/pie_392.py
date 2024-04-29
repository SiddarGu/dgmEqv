
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(7,7))

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Credit Cards','Debit Cards','PayPal','Cash','Apple Pay']
sizes = [35,25,20,15,5]
explode = (0, 0, 0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Cash')

ax = fig.add_subplot()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'fontsize': 14})
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Popular Payment Methods for Retail Shopping in 2023', fontsize=18)
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/128.png')
plt.clf()