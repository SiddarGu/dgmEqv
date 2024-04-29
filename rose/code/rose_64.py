
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Civil Litigation', 'Criminal Law', 'Corporate Law', 'Family Law', 'Labor Law', 'Immigration Law', 'Intellectual Property', 'Environmental Law', 'Tax Law', 'International Law']
data = [450, 350, 300, 250, 200, 150, 100, 80, 60, 40]
line_labels = ['Legal Category', 'Number of Cases']

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], alpha=1, color=plt.cm.tab10(i))
ax.set_title("Number of Cases Filed by Legal Category in 2021")
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories + 1)[:-1])
ax.set_xticklabels(data_labels, fontsize=8, rotation=60, wrap=True)
ax.legend(bbox_to_anchor=(1.2, 0.9))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_27.png')
plt.clf()