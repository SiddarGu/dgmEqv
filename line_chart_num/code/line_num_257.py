
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
ax = plt.subplot()

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
temp = [25, 27, 30, 32, 34, 35, 37, 38, 37, 36, 31, 28]
humidity = [60, 65, 70, 75, 80, 85, 88, 90, 87, 85, 75, 68]

ax.plot(month, temp, color='b', label='Temperature')
ax.plot(month, humidity, color='r', label='Humidity')

ax.set_title('Average temperature and humidity in Tokyo, Japan in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Average temperature/humidity')

ax.legend()

for a,b in zip(month, temp):
    ax.annotate(str(b), xy=(a, b), xytext=(0,5), textcoords='offset points')
for c,d in zip(month, humidity):
    ax.annotate(str(d), xy=(c, d), xytext=(0,5), textcoords='offset points')

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('line chart/png/45.png')
plt.clf()