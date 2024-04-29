
import matplotlib.pyplot as plt
import numpy as np

# Get data
country = ['USA','UK','Germany','France']
lawyers = [85000,40000,70000,30000]
judges = [1600,900,1100,1000]

# Create figure
fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot()

# Set x,y values
x = np.arange(len(country))
width = 0.35

# Plot data
ax.bar(x-width/2, lawyers, width, label='Lawyers')
ax.bar(x+width/2, judges, width, label='Judges')

# Set title and labels
ax.set_title('Number of lawyers and judges in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(country)
ax.set_ylabel('Number of people')

# Annotate value of each data point
ax.annotate(lawyers[0], xy=(x[0]-width/2, lawyers[0]), xytext=(-11, 5), textcoords="offset points")
ax.annotate(lawyers[1], xy=(x[1]-width/2, lawyers[1]), xytext=(-11, 5), textcoords="offset points")
ax.annotate(lawyers[2], xy=(x[2]-width/2, lawyers[2]), xytext=(-11, 5), textcoords="offset points")
ax.annotate(lawyers[3], xy=(x[3]-width/2, lawyers[3]), xytext=(-11, 5), textcoords="offset points")
ax.annotate(judges[0], xy=(x[0]+width/2, judges[0]), xytext=(11, 5), textcoords="offset points")
ax.annotate(judges[1], xy=(x[1]+width/2, judges[1]), xytext=(11, 5), textcoords="offset points")
ax.annotate(judges[2], xy=(x[2]+width/2, judges[2]), xytext=(11, 5), textcoords="offset points")
ax.annotate(judges[3], xy=(x[3]+width/2, judges[3]), xytext=(11, 5), textcoords="offset points")

# Add legend
ax.legend()

# Resize figure
fig.tight_layout()

# Save figure 
plt.savefig('Bar Chart/png/92.png')

# Clear current figure
plt.clf()