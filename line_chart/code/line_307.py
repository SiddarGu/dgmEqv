
import matplotlib.pyplot as plt 
import numpy as np 

plt.figure(figsize=(8,5)) 

month = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug']) 
attendance = np.array([500,600,700,800,900,1000,1200,1100]) 

plt.plot(month, attendance, color='blue', marker='o', linestyle='solid',  linewidth=2, markersize=6) 

plt.title('Attendance at NBA games in 2021') 
plt.xlabel('Month') 
plt.ylabel('Attendance') 

plt.xticks(np.arange(0, 8, step=1), month, rotation=30) 

plt.tight_layout() 

plt.savefig('line chart/png/92.png') 
plt.clf()