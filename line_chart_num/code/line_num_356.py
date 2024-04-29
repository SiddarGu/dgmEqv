
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)

# Set data
year = [2001, 2002, 2003, 2004]
techA = [50, 55, 60, 65]
techB = [20, 25, 30, 35]
techC = [30, 20, 10, 0]

# Plot
ax.plot(year, techA, color='#0078d4', linestyle='-', label='Technology A')
ax.plot(year, techB, color='#f14a24', linestyle='-', label='Technology B')
ax.plot(year, techC, color='#585858', linestyle='-', label='Technology C')

# Set labels and title
ax.set_xticks(year)
ax.set_xlabel('Year')
ax.set_ylabel('Adoption Rate(%)')
ax.set_title('Adoption rate of three technologies in the past four years')

# Annotate
for i, j in zip(year, techA):
    ax.annotate(str(j), xy=(i-0.1, j+1), size=10)
for i, j in zip(year, techB):
    ax.annotate(str(j), xy=(i-0.1, j+1), size=10)
for i, j in zip(year, techC):
    ax.annotate(str(j), xy=(i-0.1, j+1), size=10)

# Add legend
plt.legend(loc='upper right')

# Adjust the picture
plt.tight_layout()

# Save
plt.savefig('line chart/png/147.png')

# Clear
plt.clf()