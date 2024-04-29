
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 6))
ax = plt.subplot()
year = np.array([2000, 2001, 2002, 2003, 2004])
earnings = np.array([10, 15, 20, 12, 18])
athlete_endorsement = np.array([5, 7, 9, 6, 8])
event_sponsorship = np.array([2, 3, 4, 2, 3])

plt.plot(year, earnings, label='Earnings (million dollars)', color='#1f77b4', marker='s')
plt.plot(year, athlete_endorsement, label='Athlete Endorsement (million dollars)', color='#2ca02c', marker='o')
plt.plot(year, event_sponsorship, label='Event Sponsorship (million dollars)', color='#d62728', marker='v')

plt.title('Revenue of Sports and Entertainment Industry in 2000-2004')
ax.set_xticks(year)
ax.set_xlabel('Year')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

for a, b, c, d in zip(year, earnings, athlete_endorsement, event_sponsorship):
    plt.annotate(f'{b}', xy=(a, b), xytext=(a+0.2, b+1))
    plt.annotate(f'{c}', xy=(a, c), xytext=(a+0.2, c+1))
    plt.annotate(f'{d}', xy=(a, d), xytext=(a+0.2, d+1))

plt.tight_layout()
plt.savefig('line chart/png/104.png')
plt.clf()