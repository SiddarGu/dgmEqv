import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Data preparation
data_labels = ['Cinema Screenings', 'Box Office Revenue (Million)']
line_labels = ['Comedy', 'Action', 'Drama', 'Horror', 'Romantic', 'Sci-fi', 'Documentary', 'Animated']
data = [215.5, 325.4, 188.2, 140.3, 121.5, 298.7, 58.4, 234.6]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Plotting
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Horizontal bar plot
sns.barplot(x=data, y=line_labels, palette="viridis", ax=ax)

# Add grids for better readability
ax.xaxis.grid(True)

# Set long label to wrap or rotate
ax.set_yticklabels(line_labels, rotation=45, ha='right', wrap=True)

# Title of the figure
plt.title('Box Office Earnings by Film Genre')

# Resize image by tight_layout() before savefig()
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/183.png')

# Clear the current image state
plt.clf()
