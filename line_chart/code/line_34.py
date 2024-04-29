
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))

x = [2001, 2002, 2003, 2004]
y1 = [1000, 1100, 900, 1200]
y2 = [800, 900, 1000, 1100]
y3 = [1200, 1400, 1100, 1200]

plt.plot(x, y1, color='r', marker='o', label='Crime Rate (per 100,000 people)')
plt.plot(x, y2, color='g', marker='o', label='Violent Crime Rate (per 100,000 people)')
plt.plot(x, y3, color='b', marker='o', label='Property Crime Rate (per 100,000 people)')
plt.xticks(x, (2001, 2002, 2003, 2004))
plt.title('Crime Rates in the United States in the 21st Century')
plt.xlabel('Year')
plt.ylabel('Crime Rate (per 100,000 people)')
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1, 
           fancybox=True, shadow=True)
plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/484.png')
plt.clf()