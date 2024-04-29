
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Set the figure size
plt.figure(figsize=(8, 8))

#Set the font size
matplotlib.rcParams.update({'font.size': 14})

# Set the color 
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99', '#feb2a7']

# Set the label 
labels = ['Individual Donors','Charitable Foundations','Corporations','Government Grants','Fundraising Events','Other']

# Set the data
data = np.array([50,20,10,10,5,5])

# Set the subplot
plt.subplot(111)

# Set the pie chart
plt.pie(data, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)

# Set the title
plt.title("Distribution of Donations to Nonprofit Organizations in 2021")

# Set the legend
plt.legend(labels, loc='best', bbox_to_anchor=(1, 0.5))

# Set the tight layout
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/155.png')

# Clear the figure
plt.clf()