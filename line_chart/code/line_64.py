
import matplotlib.pyplot as plt
import numpy as np

#data
Month= ['January','February','March','April','May','June','July','August','September','October','November','December']
Solar_Panel_Output=[8000,9000,10000,11000,13000,14000,15000,16000,17000,15000,13000,11000]
Wind_Turbine_Output=[3000,4000,5000,6000,7000,8000,9000,10000,8000,7000,6000,5000]

#Create figure
fig = plt.figure(figsize=(10,7))

#plot
plt.plot(Month, Solar_Panel_Output, label="Solar Panel Output", color='b')
plt.plot(Month, Wind_Turbine_Output, label="Wind Turbine Output", color='r')

#set xticks
plt.xticks(Month, rotation=90, ha='center')

#title and legend
plt.title('Monthly Output Comparison between Solar Panel and Wind Turbine in 2021', fontsize=16, fontweight='bold', wrap=True)
plt.legend(loc='upper right')

#tight layout
plt.tight_layout()

#save
plt.savefig('line chart/png/87.png')

#clear
plt.clf()