
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(1, 1, 1)

# Set data
x_data = [2001, 2002, 2003, 2004] 
museums_data = [100, 110, 120, 130] 
art_galleries_data = [80, 90, 80, 85]
performance_halls_data = [50, 45, 55, 60]
libraries_data = [60, 65, 60, 70]

# Plot line chart
ax.plot(x_data, museums_data, label = "Number of Museums", marker = 'o')
ax.plot(x_data, art_galleries_data, label = "Number of Art Galleries", marker = 'o')
ax.plot(x_data, performance_halls_data, label = "Number of Performance Halls", marker = 'o')
ax.plot(x_data, libraries_data, label = "Number of Libraries", marker = 'o')

# Set legend
ax.legend()

# Set labels
plt.xlabel('Year', fontsize = 14) 
plt.ylabel('Number of Facilities', fontsize = 14)

# Set title
plt.title('Development of Cultural Facilities in the U.S. from 2001 to 2004', fontsize = 18)

# Annotate
for x_val, y_val in zip(x_data, museums_data):
    ax.annotate(str(y_val), xy = (x_val, y_val), xytext = (x_val + 0.2, y_val + 7), fontsize = 12)

for x_val, y_val in zip(x_data, art_galleries_data):
    ax.annotate(str(y_val), xy = (x_val, y_val), xytext = (x_val + 0.2, y_val + 7), fontsize = 12)

for x_val, y_val in zip(x_data, performance_halls_data):
    ax.annotate(str(y_val), xy = (x_val, y_val), xytext = (x_val + 0.2, y_val + 7), fontsize = 12)

for x_val, y_val in zip(x_data, libraries_data):
    ax.annotate(str(y_val), xy = (x_val, y_val), xytext = (x_val + 0.2, y_val + 7), fontsize = 12)

# Set xticks
plt.xticks(x_data, fontsize = 12)

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('line chart/png/173.png')

# Clear the current image state
plt.clf()