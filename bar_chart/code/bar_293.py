
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 50, 60, 40],
        ['UK', 60, 70, 50],
        ['Germany', 40, 80, 60],
        ['France', 50, 90, 70]]

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()
x_pos = np.arange(len(data))

# Set title and labels
plt.title('Manufacturing output in three categories in four countries in 2021')
plt.ylabel('Quantity (million)')
plt.xticks(x_pos, [country[0] for country in data])

# Set bars
bars = plt.bar(x_pos, [country[1] for country in data], label='Manufacturing A', width=0.25)
plt.bar(x_pos + 0.25, [country[2] for country in data], label='Manufacturing B', width=0.25)
plt.bar(x_pos + 0.5, [country[3] for country in data], label='Manufacturing C', width=0.25)

# Draw legend
plt.legend(loc='upper right')

# Adjust margins and display
plt.tight_layout()
plt.savefig('bar chart/png/292.png')
plt.clf()