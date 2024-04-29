
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,6))

# Set data
data = [['USA', 20000, 60000],
        ['UK', 30000, 70000],
        ['Germany', 18000, 40000],
        ['France', 23000, 47000]]

# Create bar
x = np.arange(len(data))
bar_width = 0.35
rects1 = plt.bar(x, [i[1] for i in data], bar_width, color='b', label='Criminal Cases')
rects2 = plt.bar(x + bar_width, [i[2] for i in data], bar_width, color='r', label='Civil Cases')

# Labels
plt.xticks(x + bar_width / 2, [i[0] for i in data], rotation=45, wrap=True)
plt.ylabel('Cases number')
plt.title('Number of criminal and civil cases in four countries in 2021')
plt.legend()

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/386.png')

# Clear current image state
plt.clf()