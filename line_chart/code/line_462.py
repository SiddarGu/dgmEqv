
import matplotlib.pyplot as plt
x_axis = [2001, 2002, 2003, 2004, 2005, 2006]
gdp = [13000,13500,14000,14500,15000,15500]
unemployment = [4.6,5.2,4.7,5.1,4.9,4.8]

plt.figure(figsize=(8,8))
ax1 = plt.subplot(111)
ax1.plot(x_axis, gdp, label='GDP')
ax1.plot(x_axis, unemployment, label='Unemployment Rate')
ax1.set_title('US GDP and Unemployment Rate from 2001 to 2006')
ax1.set_xlabel('Year')
ax1.set_ylabel('Value')
ax1.legend()
ax1.grid()
plt.xticks(x_axis)
plt.tight_layout()
plt.savefig('line chart/png/409.png')
plt.clf()