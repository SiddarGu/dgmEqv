import matplotlib.pyplot as plt
import numpy as np

labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
          'August', 'September', 'October', 'November', 'December']

Truck_Shipments = np.array([19000, 20000, 20800, 21500, 22000, 22500, 
                            23000, 23500, 24000, 24500, 25000, 25500]) 
Freight_Car_Loadings = np.array([25000, 26000, 27000, 27500,28000, 28500, 
                                 29000, 29500, 30000, 30500, 31000, 31500])
Air_Freight = np.array([6000, 6200, 6400, 6700, 7000, 7300, 7600, 7900, 
                        8200, 8500, 8800, 9100])
Cargo_Throughput = np.array([22000, 23000, 24000, 25000, 26000, 27000, 
                             28000, 29000, 30000, 31000, 32000, 33000])
Revenues = np.array([170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280])

fig = plt.figure(figsize=(15,10)) 
ax1 = fig.add_subplot(111)

ax1.plot(labels, Truck_Shipments, color='b', label="Truck Shipments")
ax2 = ax1.twinx()
ax2.plot(labels, Freight_Car_Loadings, color='g', label="Freight Car Loadings")
ax3 = ax1.twinx()
ax3.plot(labels, Air_Freight, color='r', label="Air Freight")
ax4 = ax1.twinx()
ax4.bar(labels, Cargo_Throughput, color='c', label="Cargo Throughput", alpha=0.5)
ax5 = ax1.twinx()
ax5.fill_between(labels, Revenues, color='m', alpha=0.3, label="Revenues")

# Label Axes
ax1.set_ylabel('Truck Shipments (Units)', color='b')
ax2.set_ylabel('Freight Car Loadings (Units)', color='g')
ax3.set_ylabel('Air Freight (Tons)', color='r')
ax4.set_ylabel('Cargo Throughput (Tons)', color='c')
ax5.set_ylabel('Revenues (Millions of Dollars)', color='m')

ax3.spines['right'].set_position(('outward', 60))  
ax4.spines['right'].set_position(('outward', 120))  
ax5.spines['right'].set_position(('outward', 180))

# Create Legends 
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')
ax4.legend(loc='lower left')
ax5.legend(loc='lower right')

plt.title('Monthly Overview of Transportation and Logistics in Numbers')
plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/148_202312310108.png')
plt.clf()
