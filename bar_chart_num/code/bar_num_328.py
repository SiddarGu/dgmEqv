
import matplotlib.pyplot as plt

dpts = ['Finance', 'IT', 'Human Resources', 'Sales'] 
full_time = [120, 90, 80, 140] 
part_time = [40, 60, 50, 70]

# Create figure
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

# Create Bar Chart
ax.bar(dpts, full_time, label='Full Time', bottom = part_time)
ax.bar(dpts, part_time, label='Part Time')

# Add Labels
for x, y in zip(dpts, full_time):
    ax.annotate('{}'.format(y), xy=(x, y/2 + part_time[dpts.index(x)]/2), ha='center') 
for x, y in zip(dpts, part_time):
    ax.annotate('{}'.format(y), xy=(x, y/2), ha='center') 
    
# Set Properties
plt.title('Number of full-time and part-time employees in four departments in 2021')
ax.xaxis.set_ticks(dpts)
plt.legend()
plt.tight_layout()

# Save Image
fig.savefig('Bar Chart/png/539.png')

# Clear Current Figure
plt.clf()