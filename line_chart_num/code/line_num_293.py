
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.subplot(1,1,1)
x = [2001, 2002, 2003, 2004, 2005]
y1 = [1000, 4000, 8000, 12000, 15000]
y2 = [200, 400, 800, 1200, 1400]
y3 = [5, 10, 15, 20, 25]
plt.plot(x, y1, '-o', color='blue', label='Number of Users')
plt.plot(x, y2, '-o', color='red', label='Number of Connections')
plt.plot(x, y3, '-o', color='green', label='Average Connection Speed(Mbps)')
plt.xticks(x)
plt.xlabel('Year')
plt.ylabel('Number of Users/Connections/Speed')
plt.title('Growth of Technology Usage and Connection Speed in the US from 2001 to 2005')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
for x, y1, y2, y3 in zip(x, y1, y2, y3):
    plt.annotate(f'{y1}/{y2}/{y3}', (x, y1), xytext=(x-0.1, y1+400))
plt.tight_layout()
plt.savefig('line chart/png/189.png')
plt.clf()