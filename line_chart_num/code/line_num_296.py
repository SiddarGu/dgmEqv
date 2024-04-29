
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
x = ["January", "February", "March", "April", "May", "June"]
y1 = [1000, 1200, 800, 1500, 1100, 1400]
y2 = [800, 900, 1100, 1200, 1300, 800]
plt.plot(x, y1, color='red', label='Online Sales(million dollars)')
plt.plot(x, y2, color='blue', label='Store Sales(million dollars)')
plt.title('Comparison of Online and Store sales in 2021')
plt.xlabel('Month')
plt.ylabel('million dollars')
plt.xticks(x)
plt.legend(loc='upper left')
for x, y in zip(x, y1):
    plt.annotate(y, xy=(x, y), xytext=(0, -10), textcoords='offset points', horizontalalignment='center', verticalalignment='top')
for x, y in zip(x, y2):
    plt.annotate(y, xy=(x, y), xytext=(0, 10), textcoords='offset points', horizontalalignment='center', verticalalignment='bottom')
plt.tight_layout()
plt.savefig('line chart/png/123.png')
plt.clf()