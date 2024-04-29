
import matplotlib.pyplot as plt
import numpy as np
 
# Data
Month= ['January', 'February', 'March', 'April', 'May']
Air_Freight = [100, 150, 120, 190, 130]
Rail_Freight = [200, 180, 220, 210, 250]
Truck_Freight = [300, 320, 280, 330, 310]
Ship_Freight = [400, 350, 390, 420, 450]
 
# Plot
fig, ax = plt.subplots(figsize=(10,6))
ax.plot(Month, Air_Freight, label='Air Freight', color='#FFD700')
ax.plot(Month, Rail_Freight, label='Rail Freight', color='#00FFFF')
ax.plot(Month, Truck_Freight, label='Truck Freight', color='#F08080')
ax.plot(Month, Ship_Freight, label='Ship Freight', color='#006400')

# Change the tick labels of x-axis
plt.xticks(np.arange(len(Month)), Month, rotation=90)

# Add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)

# Title & Axis
ax.set_title('Freight transportation by different means in 2021', fontsize=20)
ax.set_xlabel('Month', fontsize=16)
ax.set_ylabel('Tonnes', fontsize=16)

# Grid
ax.grid(linestyle='--', linewidth=0.5, color='gray')

# Tight Layout
fig.tight_layout()

# Save
fig.savefig('line chart/png/163.png')

# Clear
plt.clf()