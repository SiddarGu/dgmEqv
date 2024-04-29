
import matplotlib.pyplot as plt
import matplotlib as mpl

# Create figure
fig = plt.figure(figsize=(8, 8))

# Pie chart
labels = ['Rail','Road','Air','Water']
sizes = [15, 45, 30, 10]
explode = [0, 0.1, 0, 0]

mpl.rcParams['font.size'] = 13.0

plt.pie(sizes, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
plt.title('Distribution of Transportation Modes in the US, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/525.png')

plt.clf()