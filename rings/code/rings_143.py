
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib

data_labels = ['Statutory Regulation', 'Case Law', 'Legal Practice', 'Judicial Precedent', 'Civil Procedure']
data = [26, 24, 10, 20, 20]
line_labels = ['Area', 'ratio']

plt.figure(figsize=(10, 10))

ax = plt.subplot()

ax.pie(data, labels=data_labels, startangle=90, counterclock=False)

inner_circle = mpatches.Circle((0, 0), 0.7, color="white")
ax.add_patch(inner_circle)

ax.legend(data_labels, loc="upper right")
ax.set_title("Law and Legal Affairs - Overview 2023")
ax.axis("equal")

plt.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_103.png', bbox_inches='tight')
plt.clf()