
import matplotlib.pyplot as plt

sports = ['Football', 'Baseball', 'Basketball', 'Hockey']
average_attendance = [60, 50, 40, 30]
average_ticket_price = [45, 40, 30, 20]

fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(sports, average_attendance, label='Average Attendance', color='red', bottom=0)
ax.bar(sports, average_ticket_price, label='Average Ticket Price', color='blue', bottom=average_attendance)
ax.set_title('Average attendance and ticket prices for four sports in 2021', fontsize=14)
ax.set_xlabel('Sport')
ax.set_ylabel('Attendance & Ticket Price')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/464.png')
plt.clf()