
import matplotlib.pyplot as plt
import numpy as np

# Set up data
Country = ['USA','UK','Germany','France']
Education = [90,80,85,75]
Healthcare = [90,95,85,90]
Social_Services = [80,85,90,95]

# Create figure
fig, ax = plt.subplots(figsize=(6,6))

# Plotting the data
bar1 = ax.bar(Country, Education, bottom=Healthcare, color='#1f77b4', label='Education')
bar2 = ax.bar(Country, Healthcare, bottom=Social_Services, color='#ff7f0e', label='Healthcare')
bar3 = ax.bar(Country, Social_Services, color='#2ca02c', label='Social Services')

# Set title and labels
ax.set_title('Percentage of government spending on Education, Healthcare and Social Services in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Percentage')

# Set legend
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left')

# Add labels
for i in range(len(Country)):
    ax.annotate(str(Education[i])+'%', xy=(bar1[i].get_xy()[0], bar1[i].get_height()/2+bar1[i].get_xy()[1]), 
                xytext=(bar1[i].get_xy()[0], bar1[i].get_height()/2+bar1[i].get_xy()[1]), 
                ha='center', va='center')
    ax.annotate(str(Healthcare[i])+'%', xy=(bar2[i].get_xy()[0], bar2[i].get_height()/2+bar2[i].get_xy()[1]), 
                xytext=(bar2[i].get_xy()[0], bar2[i].get_height()/2+bar2[i].get_xy()[1]), 
                ha='center', va='center')
    ax.annotate(str(Social_Services[i])+'%', xy=(bar3[i].get_xy()[0], bar3[i].get_height()/2+bar3[i].get_xy()[1]), 
                xytext=(bar3[i].get_xy()[0], bar3[i].get_height()/2+bar3[i].get_xy()[1]), 
                ha='center', va='center')

# Set x ticks
plt.xticks(Country)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('Bar Chart/png/13.png')

# Clear the current image state
plt.clf()