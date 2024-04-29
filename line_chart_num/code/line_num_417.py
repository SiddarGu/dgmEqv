
import matplotlib.pyplot as plt
import numpy as np

#Create figure before plotting
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot()

#Plotting data 
country = ['USA','China','India','Japan','France']
num_tourists = [80,90,50,70,30]
avg_spending = [500,400,200,300,400]
ax.plot(country, num_tourists, color='blue', label='Number of Tourists (millions)')
ax.plot(country, avg_spending, color='red', label='Average Tourist Spending')

#Labeling the value of each data point
for x,y in zip(country, num_tourists):
    label = "{:.1f}".format(y)
    ax.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')
for x,y in zip(country, avg_spending):
    label = "{:.1f}".format(y)
    ax.annotate(label, (x,y), textcoords="offset points", xytext=(0,10), ha='center')

#Rendering
plt.xticks(country)
plt.title('Global Tourism Trends in 2021')
plt.xlabel('Country')
plt.ylabel('Number of Tourists (millions) and Average Tourist Spending')
plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig('line chart/png/546.png')
plt.clf()