
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

data_labels = ["Crop Yield", "Livestock Breeding", "Pest Control", "Resource Management", "Conservation"]
data = [35, 20, 17, 10, 18]
line_labels = ["Category", "ratio"]

fig, ax = plt.subplots(figsize=(9, 6))

ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%1.0f%%')
ax.axis('equal')

centre_circle = plt.Circle((0, 0), 0.5, color='white')
ax.add_artist(centre_circle)

ax.legend(data_labels, loc="upper right")
plt.title('Agriculture and Food Production Trends - 2023')
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_41.png")
plt.clf()