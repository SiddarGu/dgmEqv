
import matplotlib.pyplot as plt

country = ['USA', 'UK', 'Germany', 'France']
Literature = [200, 190, 150, 220]
History = [220, 190, 180, 200]
Philosophy = [190, 150, 220, 180]

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 6))

# Add x-axis and y-axis
ax.bar(country, Literature, color='blue', label='Literature')
ax.bar(country, History, bottom=Literature, color='red', label='History')
ax.bar(country, Philosophy, bottom=[Literature[i] + History[i] for i in range(len(country))], color='green', label='Philosophy')

# Set title and labels for axes
ax.set(xlabel="Country",
       ylabel="Number of Courses Taken",
       title="Number of social science and humanities courses taken by students in four countries in 2021")

# Add legend
ax.legend()

# Annotate each bar with the value of each data point
for i in ax.patches:
    ax.annotate(str(i.get_height()), (i.get_x() + 0.2, i.get_height() + 5))

# Resize the figure
plt.tight_layout()

# Prevent Interpolation
plt.xticks(country)

# Save the figure
plt.savefig('Bar Chart/png/316.png')

# Clear the current image state
plt.clf()