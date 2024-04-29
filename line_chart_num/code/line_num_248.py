

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
plt.figure(figsize=(10,5))
plt.subplot()
plt.plot(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug'],[150,200,250,180,220,240,200,190], marker='o', markerfacecolor='#1f77b4', markersize=12, color='#1f77b4', linewidth=2)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Number of Flights', fontsize=15)
plt.title('Domestic Flight Performance in 2021', fontsize=15)
plt.gca().xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.0f}'))
plt.xticks(rotation=90)
for x,y in zip(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug'],[150,200,250,180,220,240,200,190]):
    label = "{:.1f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,-15), # distance from text to points (x,y)
                 ha='center', # horizontal alignment can be left, right or center
                 fontsize=12)
plt.tight_layout()
plt.savefig('line chart/png/263.png')
plt.clf()