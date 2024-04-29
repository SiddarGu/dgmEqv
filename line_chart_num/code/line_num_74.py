
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1000000, 2000000, 1800000, 2200000, 1900000, 2100000], 
                 [25, 45, 30, 50, 40, 55]])

# set figure size
plt.figure(figsize=(10,5))

# add subplot
ax = plt.subplot()

# set labels and title
plt.title('Donations and Projects completed by a Nonprofit Organization in 2021')
plt.xlabel('Month')
plt.ylabel('Donations received (dollars) and Projects completed')

# set the x axis and y axis value
x_value = ['January', 'February', 'March', 'April', 'May', 'June']
y_value_1 = data[0]
y_value_2 = data[1]

# plot
ax.plot(x_value, y_value_1, label="Donations received (dollars)")
ax.plot(x_value, y_value_2, label="Projects completed")

# add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.2,1))

# use xticks to prevent interpolation
plt.xticks(rotation=45)

# label the value of each data point directly on the figure
for a, b in zip(x_value, y_value_1):
    plt.text(a, b, str(b), rotation=45, ha="center", va="bottom", fontsize=9)

for a, b in zip(x_value, y_value_2):
    plt.text(a, b, str(b), rotation=45, ha="center", va="bottom", fontsize=9)

# draw background grid
plt.grid(axis='y', linestyle='--')

# automatically resize the image by tight_layout
plt.tight_layout()

# save the chart
plt.savefig('line chart/png/402.png')

# clear the current image state
plt.clf()