
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(15,6))
x = np.array([25,30,35,40])
y1 = np.array([25,27,30,35])
y2 = np.array([170,180,160,175])
y3 = np.array([60,80,70,90])
plt.plot(x,y1,label='BMI (kg/m2)')
plt.plot(x,y2,label='Height (cm)')
plt.plot(x,y3,label='Weight (kg)')
plt.xticks(x)
plt.xlabel('Age(years)')
plt.title('Height and Weight Changes in Adults between 25 and 40 Years Old')
plt.legend(loc='upper left')
for xy in zip(x,y1):
    plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
for xy in zip(x,y2):
    plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
for xy in zip(x,y3):
    plt.annotate('(%s, %s)' % xy, xy=xy, textcoords='data')
plt.tight_layout()
plt.savefig('line chart/png/175.png')
plt.clf()