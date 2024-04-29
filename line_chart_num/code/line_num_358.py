
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Get data
data = [[2020, 20.5, 2.5, 4.2, 21.2],
        [2021, 21.5, 3.2, 3.5, 22.4],
        [2022, 22.2, 3.5, 3.0, 23.5],
        [2023, 23.3, 3.7, 2.8, 24.6]]

# Set figure size
plt.figure(figsize=(12, 8))

# Set the labels of x-axis
x_axis = [i[0] for i in data]

# Set the labels of y-axis
y_axis_GDP = [i[1] for i in data]
y_axis_Inflation = [i[2] for i in data]
y_axis_Unemployment = [i[3] for i in data]
y_axis_Debt = [i[4] for i in data]

# Add subplot, use linestyle to draw lines
ax1 = plt.subplot(2,2,1)
plt.plot(x_axis, y_axis_GDP, linestyle = '-', marker = 'o', color = 'darkorange', label = 'GDP')
# Add annotation
for gdp in data:
    ax1.annotate('$'+str(gdp[1])+'T', xy=(gdp[0], gdp[1]), xytext=(gdp[0], gdp[1]), fontsize = 12, rotation = 90)

ax2 = plt.subplot(2,2,2)
plt.plot(x_axis, y_axis_Inflation, linestyle = '-', marker = 's', color = 'pink', label = 'Inflation Rate')
# Add annotation
for inflation in data:
    ax2.annotate(str(inflation[2])+'%', xy=(inflation[0], inflation[2]), xytext=(inflation[0], inflation[2]), fontsize = 12, rotation = 90)

ax3 = plt.subplot(2,2,3)
plt.plot(x_axis, y_axis_Unemployment, linestyle = '-', marker = '^', color = 'green', label = 'Unemployment Rate')
# Add annotation
for unemployment in data:
    ax3.annotate(str(unemployment[3])+'%', xy=(unemployment[0], unemployment[3]), xytext=(unemployment[0], unemployment[3]), fontsize = 12, rotation = 90)

ax4 = plt.subplot(2,2,4)
plt.plot(x_axis, y_axis_Debt, linestyle = '-', marker = 'v', color = 'red', label = 'Debt')
# Add annotation
for debt in data:
    ax4.annotate('$'+str(debt[4])+'T', xy=(debt[0], debt[4]), xytext=(debt[0], debt[4]), fontsize = 12, rotation = 90)

# Set the title of the figure
plt.suptitle('Economic indicators in the United States from 2020 to 2023')

# Set the label of x-axis
plt.xticks(x_axis)

# Set the label of y-axis
ax1.set_ylabel('GDP(trillion dollars)')
ax2.set_ylabel('Inflation Rate(%)')
ax3.set_ylabel('Unemployment Rate(%)')
ax4.set_ylabel('Debt(trillion dollars)')

# Set the ticker
ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax2.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax3.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax4.xaxis.set_major_locator(ticker.MultipleLocator(1))

# Set the legend
ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/525.png')

# Clear the current image state
plt.clf()