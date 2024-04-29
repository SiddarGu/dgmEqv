
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.figure(figsize=(8, 4))
ax = plt.subplot()
ax.plot(['7th', '8th', '9th', '10th', '11th', '12th'], [3000, 3500, 4000, 4500, 5000, 5500], color='r', marker='o', linestyle='--')
ax.set_title('Student Enrollment in US High Schools in 2021')
ax.set_xlabel('Grade')
ax.set_ylabel('Number of Students')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(['7th', '8th', '9th', '10th', '11th', '12th']))
ax.annotate('3000', xy=(0.1, 3000), xytext=(0.1, 3000))
ax.annotate('3500', xy=(1.1, 3500), xytext=(1.1, 3500))
ax.annotate('4000', xy=(2.1, 4000), xytext=(2.1, 4000))
ax.annotate('4500', xy=(3.1, 4500), xytext=(3.1, 4500))
ax.annotate('5000', xy=(4.1, 5000), xytext=(4.1, 5000))
ax.annotate('5500', xy=(5.1, 5500), xytext=(5.1, 5500))
plt.tight_layout()
plt.savefig('line chart/png/150.png')
plt.clf()