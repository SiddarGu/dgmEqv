
import matplotlib.pyplot as plt

country = ['USA', 'UK', 'Germany', 'France']
musical_events = [100, 120, 90, 110]
museums_visits = [200, 230, 210, 220]
theatres_visits = [150, 170, 140, 160]

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

ax.bar(country, musical_events, label='Musical Events', bottom=museums_visits)
ax.bar(country, museums_visits, label='Museums Visits', bottom=theatres_visits)
ax.bar(country, theatres_visits, label='Theatres Visits')

ax.set_title('Arts and Culture activities in four countries in 2021')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar chart/png/229.png')
plt.clf()