import matplotlib.pyplot as plt

# Preparing data
categories = ['Electronics', 'Apparel', 'Beauty Products', 'Food and Beverage', 'Books']
sales_data = [[50,70,90,120,150], [45,80,105,130,160], [20,40,60,80,100], [35,60,85,110,140], [30,50,70,90,110]] 
outliers = [[], [250], [15,18], [5,12,170,190], [20,25,120]]

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111)

# Creating box plot
bplot = ax1.boxplot(sales_data, vert=True, patch_artist=True, labels=categories, whis=1.5)

colors = ['pink', 'lightblue', 'lightgreen', 'red', 'purple']
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# Plotting outliers
for i, outlier in enumerate(outliers): 
    if outlier:  # check if outlier list is not empty
        ax1.plot([i + 1] * len(outlier), outlier, "ko")

ax1.yaxis.grid(True)
ax1.xaxis.grid(False)
ax1.set_title('Sales Distribution in Different Product Categories in Retail and E-commerce Industry (2022)')
ax1.set_ylabel('Sales (in Thousands)')
plt.xticks(rotation=45) # Rotating the x axis labels if they are too long
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/115_202312270030.png')
plt.clf() # Clearing the current figure
