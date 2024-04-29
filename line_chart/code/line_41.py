
import matplotlib.pyplot as plt
import numpy as np

#Data
year = [2020, 2021, 2022, 2023, 2024]
downloads = [10, 20, 30, 50, 70]
uploads = [2, 4, 6, 8, 10]
data_usage = [4, 10, 15, 20, 25]

#Figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

#plot
ax.plot(year, downloads, label='Downloads(million)', marker='o', color='red')
ax.plot(year, uploads, label='Uploads(million)', marker='o', color='green')
ax.plot(year, data_usage, label='Data Usage(terabytes)', marker='o', color='blue')

#Legend and labels
ax.legend(loc='upper center', bbox_to_anchor=(1.15, 1.0))
ax.set_title("Internet Usage from 2020 to 2024")
ax.set_xlabel('Year')
ax.set_ylabel('Usage (million/terabytes)')
ax.set_xticks(year)

#Resize
plt.tight_layout()

#Save
plt.savefig('line chart/png/375.png', bbox_inches='tight')

#Clear current image state
plt.clf()