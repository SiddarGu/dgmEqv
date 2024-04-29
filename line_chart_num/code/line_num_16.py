
import matplotlib.pyplot as plt 

month = ['January','February','March','April','May','June','July','August','September','October','November','December']
solar_panel = [100,150,120,140,170,120,150,140,100,110,150,130]
wind_turbine = [90,115,105,115,130,100,115,125,95,100,110,115]

fig = plt.figure(figsize=(10,6)) 

ax = fig.add_subplot() 

ax.plot(month, solar_panel, label="Solar Panel Output(kWh)", marker='o', linewidth=2, color='green')
ax.plot(month, wind_turbine, label="Wind Turbine Output(kWh)", marker='^', linewidth=2, color='blue')

ax.set_title("Renewable Energy Output in 2021", fontsize=20)
ax.set_xlabel("Month", fontsize=18)
ax.set_ylabel("Output(kWh)", fontsize=18)

ax.set_xticks(month)
ax.set_xticklabels(month, rotation=45, fontsize=14)

ax.legend(loc="best", fontsize=14, bbox_to_anchor=(1.0,1.0))

for a,b,c in zip(month, solar_panel, wind_turbine):
    ax.annotate(str(b)+","+str(c), xy=(a, b), xytext=(-5,5),textcoords='offset points', fontsize=14)

plt.tight_layout()
plt.grid()
plt.savefig('line chart/png/441.png')
plt.clf()