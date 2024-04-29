
import matplotlib.pyplot as plt 
import numpy as np

#Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

#Data
Year = np.array([2001, 2002, 2003, 2004, 2005])
Football_Attendance = np.array([20, 22, 19, 23, 21])
Baseball_Attendance = np.array([16, 18, 17, 20, 19])
Basketball_Attendance = np.array([14, 15, 16, 17, 18])

#Plot line chart
ax.plot(Year, Football_Attendance, color = 'blue', label = 'Football Attendance')
ax.plot(Year, Baseball_Attendance, color = 'red', label = 'Baseball Attendance')
ax.plot(Year, Basketball_Attendance, color = 'green', label = 'Basketball Attendance')
plt.xticks(Year)

#Label
ax.set_title('Sports Attendance in the United States in the Early 2000s')
ax.set_xlabel('Year')
ax.set_ylabel('Attendance (millions)')
ax.legend()

#Adjust figure
plt.tight_layout()

#Save figure
fig.savefig('line chart/png/230.png')

#Clear figure
plt.clf()