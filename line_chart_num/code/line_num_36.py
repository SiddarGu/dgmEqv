
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# set font
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# set figure size
plt.figure(figsize=(10, 6))

# add subplot
ax = plt.subplot()

# set x axis
x_data = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90', '91-100']

# set y axis
y_data = [200, 400, 600, 800, 1000, 900, 700, 500, 300, 100]

# draw line chart
plt.plot(x_data, y_data, color='b', linestyle='-', marker='o', markersize=10)

# set x ticks
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

# set y ticks
ax.yaxis.set_major_locator(ticker.MultipleLocator(200))

# set title
plt.title('Number of people in different age groups in the US in 2021')

# add label
for a, b in zip(x_data, y_data):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

# set legend
plt.legend(['Number of People'], loc='upper right', shadow=True)

# automatically resize the image
plt.tight_layout()

# save the figure
plt.savefig('line chart/png/318.png', dpi=300)

# clear the current image state
plt.clf()