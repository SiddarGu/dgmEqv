
import matplotlib.pyplot as plt
import numpy as np 

# set data 
Country = ['USA', 'UK', 'Germany', 'France']
GDP = [20000, 17000, 21000, 19000]
Public_Spending = [4000, 4500, 5000, 4700]
Tax_Revenue = [6000, 5500, 6500, 5700]

# set parameters
x = np.arange(len(Country))  # the label locations
width = 0.25  # the width of the bars

# initial figure
fig, ax = plt.subplots(figsize=(10, 7))

# create bar chart
rects1 = ax.bar(x - width, GDP, width, label='GDP')
rects2 = ax.bar(x, Public_Spending, width, label='Public Spending')
rects3 = ax.bar(x + width, Tax_Revenue, width, label='Tax Revenue')

# add labels
ax.set_ylabel('Amount (billion)')
ax.set_title('GDP, Public Spending, and Tax Revenue in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend(loc='best')

# add text labels
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        if height == max(GDP):
            ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
        else:
            ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, -15),  # -15 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# adjust figure
fig.tight_layout()

# save figure
plt.savefig('Bar Chart/png/490.png')

# clear figure
plt.clf()