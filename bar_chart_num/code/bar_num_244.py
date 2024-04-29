
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig, ax = plt.subplots(figsize=(8,6))

#Create Bars
ax.bar(["USA","UK","Germany","France"],[400,200,300,350],width=0.4,label="Food and Beverage Expenditure")
ax.bar(["USA","UK","Germany","France"],[100,90,80,70],width=0.4,label="Restaurant Revenue",bottom=[400,200,300,350])

#Label and Title
ax.set_title("Food and Beverage Expenditure and Restaurant Revenue in four countries in 2021")
ax.set_xlabel('Country')
ax.set_ylabel('Amount (billion)')
ax.legend()

#Adjust tick and Labels
ax.xaxis.set_major_locator(ticker.FixedLocator([0,1,2,3]))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(["USA","UK","Germany","France"]))
ax.set_xticks(ax.get_xticks())
labels = [400,100,200,90,300,80,350,70]
for a,b in zip(ax.patches,labels):
    ax.annotate(b,xy=(a.get_x(),a.get_height()+2))

# Adjust the figure
fig.tight_layout()

# Save the figure
plt.savefig("Bar Chart/png/422.png")

# Clear the current image state
plt.clf()