import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Education Level': ["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "PhD"],
    'Number of Employees': [70, 50, 200, 120, 30]
}

# Transform the given data into three variables
data_labels = list(data.keys())
line_labels = data['Education Level']
data = data['Number of Employees']

# Create a DataFrame
df = pd.DataFrame({'Number of Employees': data}, index=line_labels)

# Visualize the data as a histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Create histogram
df['Number of Employees'].plot(kind='bar', ax=ax, grid=True, rot=45)

# Add titles and labels
plt.title('Employee Educational Background Distribution in a Corporate Sector')
plt.xlabel('Education Level')
plt.ylabel('Number of Employees')

# Automatically resize the image
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/637.png'
plt.savefig(save_path)

# Clear the current image state at the end of the code
plt.clf()
