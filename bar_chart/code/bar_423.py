
import matplotlib.pyplot as plt
import numpy as np

# Set data
x = np.arange(4)
Country = ('USA','UK','Germany','France')
Criminal_Cases = (50,60,45,55)
Civil_Cases = (200,220,180,190)

# Create figure
fig = plt.figure(figsize=(8,6))

# Plot data
ax = fig.add_subplot(1,1,1)
ax.bar(x-0.2, Criminal_Cases, label='Criminal Cases',color='b',width=0.4)
ax.bar(x+0.2, Civil_Cases, label='Civil Cases',color='r',width=0.4)

# Setup labels
ax.set_ylabel('Number')
ax.set_title("Number of criminal and civil cases in four countries in 2021")
ax.set_xticks(x)
ax.set_xticklabels(Country,rotation=45,ha='right',va='top',wrap=True)
ax.legend(loc='best')

# Resize
fig.tight_layout()

# Save
plt.savefig('bar chart/png/434.png')

# Clear
plt.clf()