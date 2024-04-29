
import matplotlib.pyplot as plt
x_data = ['January','February','March','April','May','June','July','August','September','October','November','December']
Vacation_days = [8,7,10,10,7,8,10,9,8,9,7,9]
Sick_days = [2,3,3,2,2,3,2,3,2,3,2,3]
Work_hours = [40,42,41,40,41,42,41,40,42,41,40,42]

fig = plt.figure(figsize=(14,7))
ax1 = fig.add_subplot(111)
ax1.plot(x_data, Vacation_days, color="red", marker="o", linestyle="-", label='Vacation days')
ax1.plot(x_data, Sick_days, color="blue", marker="o", linestyle="-", label='Sick days')
ax1.plot(x_data, Work_hours, color="green", marker="o", linestyle="-", label='Work hours')

for x,y1,y2,y3 in zip(x_data,Vacation_days,Sick_days,Work_hours):
    plt.annotate(str(y1)+','+str(y2)+','+str(y3), xy=(x,y1), xytext=(-20,10), textcoords='offset points')

plt.title('Average employee work hours and leave days in 2020')
plt.legend(loc='upper left')
plt.xticks(x_data)
plt.tight_layout()
plt.savefig('line chart/png/456.png')
plt.clf()