
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig = plt.figure(figsize = (15, 8))
ax = fig.add_subplot(1,1,1)

ages = [25,30,35,40,45,50,55,60]
salary = [50,60,65,75,85,90,80,70]

ax.plot(ages,salary, marker='o', color='blue', label='Average Salary')

ax.set_title('Average Salary Earned by Age in the US in 2021')
ax.set_xlabel('Age')
ax.set_ylabel('Average Salary (thousands of dollars)')
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.legend()

plt.tight_layout()
plt.savefig('line chart/png/538.png')

plt.cla()