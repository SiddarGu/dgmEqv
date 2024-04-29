
import matplotlib.pyplot as plt
# Set the size of the figure
plt.figure(figsize=(10,6))

# Set the labels and values of the chart
labels = ['K-12','Undergraduate','Graduate','Professional','Vocational']
values = [36,24,20,15,5]

# Plot the pie chart
plt.pie(values, labels=labels, autopct='%1.1f%%',
        startangle=90, shadow=True)
        
# Title of the figure
plt.title('Academic Level Distribution in the USA, 2023')

# Resize the image
plt.tight_layout()

# Set the rotation of the labels
plt.xticks(rotation=45)

# Save the figure
plt.savefig('pie chart/png/339.png')

# Clear the current image state
plt.clf()