
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
x = [9,10,11,12]
y1 = [3.1,3.2,3.4,3.6]
y2 = [90,91,92,94]
plt.plot(x,y1,color='red',label='Average GPA')
plt.plot(x,y2,color='blue',label='Percentage of students who passed')
plt.xticks(x)
plt.title('Average GPA and Pass Rate in High School Grades',fontsize=15)
plt.xlabel('Grade',fontsize=12,wrap=True)
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('line chart/png/362.png')
plt.clf()