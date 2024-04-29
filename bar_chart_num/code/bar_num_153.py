
import matplotlib.pyplot as plt

x = [0,1,2,3] 
windpower = [200,250,150,175]
solarpower = [400,500,450,425]
hydropower = [600,650,700,625]

plt.figure(figsize=(10,5))
ax = plt.subplot()
ax.bar(x,windpower,bottom=solarpower,label='Wind Power(GWh)')
ax.bar(x,solarpower,bottom=hydropower,label='Solar Power(GWh)')
ax.bar(x,hydropower,label='Hydro Power(GWh)')
ax.set_xticks(x)
ax.set_xticklabels(['North','South','East','West'])
ax.set_ylabel('Energy Production(GWh)')
ax.legend()
ax.set_title('Energy production from Wind, Solar, and Hydro sources in four regions in 2021')
for i, v in enumerate(windpower):
    ax.text(i-0.15, v/2+solarpower[i], str(v), color='white', fontweight='bold', fontsize=12)
for i, v in enumerate(solarpower):
    ax.text(i-0.15, v/2+hydropower[i], str(v), color='white', fontweight='bold', fontsize=12)
for i, v in enumerate(hydropower):
    ax.text(i-0.15, v/2, str(v), color='white', fontweight='bold', fontsize=12)
plt.tight_layout()
plt.savefig('Bar Chart/png/259.png')
plt.clf()