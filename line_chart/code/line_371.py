
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6.5))
ax = plt.subplot()
ax.plot([2020, 2021, 2022, 2023, 2024], [90, 85, 87, 89, 91], label='Employee Satisfaction Score', color='red', linewidth=3)
ax.plot([2020, 2021, 2022, 2023, 2024], [60, 65, 63, 67, 68], label='Employee Retention Rate', color='blue', linewidth=3)
ax.set_title("Employee Satisfaction and Retention Rate Trends in the Past 5 Years")
ax.set_xticks([2020, 2021, 2022, 2023, 2024])
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/464.png')
plt.clf()