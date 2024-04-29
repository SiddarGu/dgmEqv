
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(13,8))
ax = fig.add_subplot()

# Set data
year = [2015, 2016, 2017, 2018, 2019, 2020] 
wheat_production = [200, 210, 220, 230, 240, 250] 
rice_production = [190, 200, 210, 220, 230, 240] 
corn_production = [180, 190, 200, 210, 220, 230] 
soybean_production = [170, 180, 190, 200, 210, 220] 

# Plot line chart
ax.plot(year, wheat_production, label="Wheat Production", marker="o")
ax.plot(year, rice_production, label="Rice Production", marker="o")
ax.plot(year, corn_production, label="Corn Production", marker="o")
ax.plot(year, soybean_production, label="Soybean Production", marker="o")

# Annotate value
for i,j in zip(year,wheat_production):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(year,rice_production):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(year,corn_production):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(year,soybean_production):
    ax.annotate(str(j),xy=(i,j))

# Set title & legend
plt.title("Global Cereal Production from 2015 to 2020", fontsize=20) 
ax.legend(loc='upper left', bbox_to_anchor=(1, 0.5))

# Set grid, x ticks
ax.grid()
plt.xticks(year)

# Resize image
fig.tight_layout()

# Save & Clear
plt.savefig('line chart/png/448.png')
plt.clf()