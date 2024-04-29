
import matplotlib.pyplot as plt
# set figure size
plt.figure(figsize=(12,6))
# set xticks
x_axis = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# draw the line chart
plt.plot(x_axis, [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95], label="Renewable Energy Production (TWh)", marker='o', linestyle='--')
plt.plot(x_axis, [50, 52, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100], label="Non-Renewable Energy Production (TWh)", marker='o', linestyle='--')
# add labels
for x, y in zip(x_axis, [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]):
    label = "{:.2f}".format(y)
    plt.annotate(label,  # this is the text
                 (x,y),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0,10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center
for x, y in zip(x_axis, [50, 52, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]):
    label = "{:.2f}".format(y)
    plt.annotate(label,  # this is the text
                 (x,y),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0,10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center
# set title
plt.title("Energy Production in the US in 2024", fontsize=16)
# set legend
plt.legend(bbox_to_anchor=(1,1), loc=2, borderaxespad=0.)
# adjust the layout
plt.tight_layout()
# save the figure
plt.savefig('line chart/png/498.png')
# clear the figure
plt.clf()