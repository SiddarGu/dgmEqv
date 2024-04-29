
import numpy as np
import matplotlib.pyplot as plt

#Prepare data
data_labels = ["Eastern Asia","Southeast Asia","Southern Asia","Northern America","South America","Central & Western Europe","Western Asia","Southern Europe","Eastern Europe","Northern Africa","Western Africa","Eastern Africa","Central America","Southern Africa","Northern Europe","Australia & Oceania","Caribbean","Central Asia","Central Africa"]
data_values_susan = [5.78,4.71,6.09,2.62,3.82,7.41,10.0,4.32,5.36,9.84,6.78,4.21,2.37,2.45,3.25,2.41,2.12,4.68,2.93]
data_values_bob = [4.51,4.14,3.76,3.97,4.61,5.34,6.89,8.36,10.0,10.0,8.02,7.46,5.89,5.56,4.83,3.48,3.76,2.69,4.12]

#Draw Chart
#Create figure
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, polar=True)

#Set angles
angles = np.linspace(0, 2 * np.pi, len(data_labels) + 1, endpoint=True)

#Plot data
ax.plot(angles, [*data_values_susan, data_values_susan[0]], 'o-', label='Susan')
ax.fill(angles, [*data_values_susan, data_values_susan[0]], alpha=0.25)
ax.plot(angles, [*data_values_bob, data_values_bob[0]], 'o-', label='Bob')
ax.fill(angles, [*data_values_bob, data_values_bob[0]], alpha=0.25)

#Set axis label
ax.set_thetagrids(angles[:-1] * 180/np.pi, data_labels)

#Set radial limits
ax.set_ylim(0, 10)

#Set background grids
ax.grid(True)

#Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=2)

ax.set_title('Friendliness Scores for Different Regions Among Susan and Bob')
#Adjust figure size
plt.tight_layout()

#Save figure
plt.savefig("/cpfs01/user/yehancheng/workspace/StructChart/simulated_data_corner_cases/radar/png/two_col_3646.png")

#Clear figure state
plt.clf()