
import matplotlib.pyplot as plt
import numpy as np

Month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
Average_Electricity_Usage = [200,210,220,230,240,250,260,270,280,290,300,310]

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(Month, Average_Electricity_Usage, marker='o', markersize=8, color="green")
ax.set_title("Average monthly electricity usage in a household in 2021")
ax.set_xlabel('Month')
ax.set_ylabel('Average Electricity Usage (kWh)')
ax.tick_params(axis='x', rotation=90, labelsize=10)
ax.set_xticklabels(Month, rotation=45, ha="right", rotation_mode="anchor")
plt.tight_layout()
plt.savefig('line chart/png/296.png')
plt.clf()