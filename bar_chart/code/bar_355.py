
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot()

country = ['USA', 'UK', 'Germany', 'France']
number_of_cases = [30, 20, 18, 25]
avg_duration = [14, 11, 12, 13]

plt.bar(country, number_of_cases, width=0.3, label='Number of Cases(hundred)')
plt.bar(country, avg_duration, width=0.3, bottom=number_of_cases, label='Average Case Duration (days)')

ax.set_xticklabels(country, rotation=45, ha='right')
ax.set_title('Number of cases and average case duration in four countries in 2021')
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig('bar_355.png')
plt.clf()