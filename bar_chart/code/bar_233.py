
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(x=['K-2','3-5','6-8','9-12'], height=[80,85,90,95], width=0.5, label='Average Score')
ax.bar(x=['K-2','3-5','6-8','9-12'], height=[400,350,300,250], width=0.5, bottom=[80,85,90,95], label='Student Count')
ax.set_title('Average scores and student count for four grades in 2021')
plt.xticks(rotation=45, ha='right')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/324.png')
plt.clf()