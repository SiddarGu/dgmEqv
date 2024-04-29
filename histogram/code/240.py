import matplotlib.pyplot as plt

# Given data
data = """Energy Source, CO2 Emissions (million tons)
Coal, 1570
Oil, 1380
Natural Gas, 820
Biomass, 120
Nuclear, 60
Hydro, 30
Wind, 20
Solar, 10
Geothermal, 5"""

# Splitting the data into lines and then into labels and values
lines = data.split('\n')
data_labels = lines[0].split(', ')[1:]
line_labels = [line.split(', ')[0] for line in lines[1:]]
values = [int(line.split(', ')[1]) for line in lines[1:]]

# Create a figure and a horizontal bar chart
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Horizontal bar chart
ax.barh(line_labels, values, color=plt.cm.tab20.colors)

# Adding a grid
ax.grid(True, which='major', axis='x', linestyle='--', alpha=0.7)

# Adding titles and labels
plt.title('CO2 Emissions by Energy Source')
plt.xlabel(data_labels[0])
plt.ylabel('Energy Sources')

# Rotate or wrap labels if too long
ax.tick_params(axis='y', labelrotation=45)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Adjust layout to prevent the content from overlapping or being too tight
plt.autoscale(tight=True)

# Saving the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/240.png'
plt.savefig(save_path)

# Clear the current image state to prevent reuse
plt.clf()
