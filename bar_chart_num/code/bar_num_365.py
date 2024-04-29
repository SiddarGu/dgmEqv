
import matplotlib.pyplot as plt
import numpy as np

region = [ 'North America', 'South America', 'Europe', 'Asia']
ele_con = [1150, 630, 2500, 7000]
renew_share = [19, 25, 30, 27]

fig, ax = plt.subplots(figsize=(8,6))

ax.bar(region, ele_con, label='Electricity Consumption (TWh)', width=0.7, edgecolor='black')
ax.bar(region, renew_share, bottom=ele_con, label='Renewables Share (%)', width=0.7, edgecolor='black')

ax.set_title('Electricity consumption and renewables share by region in 2021')
ax.set_xticklabels(region)
ax.set_xlabel('Region')

ax.annotate("{}".format(ele_con[0]), (0.2, ele_con[0]/2), 
            fontsize=10, ha='center', va='center', rotation='vertical')
ax.annotate("{}".format(renew_share[0]), (0.2, ele_con[0]+renew_share[0]/2), 
            fontsize=10, ha='center', va='center', rotation='vertical')
ax.annotate("{}".format(ele_con[1]), (1.2, ele_con[1]/2), 
            fontsize=10, ha='center', va='center', rotation='vertical')
ax.annotate("{}".format(renew_share[1]), (1.2, ele_con[1]+renew_share[1]/2), 
            fontsize=10, ha='center', va='center', rotation='vertical')
ax.annotate("{}".format(ele_con[2]), (2.2, ele_con[2]/2), 
            fontsize=10, ha='center', va='center', rotation='vertical')
ax.annotate("{}".format(renew_share[2]), (2.2, ele_con[2]+renew_share[2]/2), 
            fontsize=10, ha='center', va='center', rotation='vertical')
ax.annotate("{}".format(ele_con[3]), (3.2, ele_con[3]/2), 
            fontsize=10, ha='center', va='center', rotation='vertical')
ax.annotate("{}".format(renew_share[3]), (3.2, ele_con[3]+renew_share[3]/2), 
            fontsize=10, ha='center', va='center', rotation='vertical')

ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

fig.tight_layout()

plt.savefig('Bar Chart/png/623.png')
plt.gcf().clear()