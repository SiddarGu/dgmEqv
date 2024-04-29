
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
x=['2020','2021','2022','2023','2024','2025','2026']
y1=[2.5,2.4,2.2,2.1,2.0,1.9,1.8]
y2=[0.8,0.6,0.5,0.4,0.3,0.2,0.1]
plt.plot(x,y1,color='blue',linewidth=1.0,marker='o',label='Fuel Consumption(kg/km)')
plt.plot(x,y2,color='red',linewidth=1.0,marker='o',label='CO2 Emissions(kg/km)')
plt.xticks(x)
plt.grid(linestyle='--')
plt.xlabel('Year')
plt.ylabel('kg/km')
plt.title('The Changes in Fuel Consumption and CO2 Emissions of Automobiles from 2020 to 2026')
plt.legend()
plt.tight_layout()
for a,b,c in zip(x,y1,y2):
    plt.annotate(str(b),xy=(a,b*1.02),rotation=45)
    plt.annotate(str(c),xy=(a,c*1.02),rotation=45)
plt.savefig('line chart/png/477.png')
plt.clf()