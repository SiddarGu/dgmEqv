
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 6))
plt.title('Attendance to Theater and Art Museums from 2010 to 2017')
Years = [2010,2011,2012,2013,2014,2015,2016,2017]
Theater_attendees = [20,18,16,20,21,22,24,23]
Art_museum_attendees = [15,17,19,21,20,18,19,20]
plt.plot(Years, Theater_attendees, label = 'Theater Attendees', color = 'b', marker = 'o', markerfacecolor = 'blue', markersize = 5)
plt.plot(Years, Art_museum_attendees, label = 'Art Museum Attendees', color = 'r', marker = 'o', markerfacecolor = 'red', markersize = 5)
plt.xlabel('Years')
plt.ylabel('Attendees(million people)')
plt.xticks(Years, rotation=45, wrap=True)
plt.legend(loc='upper left')
plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/523.png')
plt.clf()