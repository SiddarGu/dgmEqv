
import matplotlib.pyplot as plt
import numpy as np

data_labels = ['Price', 'Location', 'Size', 'Amenities', 'Facilities']
line_labels = ['Category']
data = np.array([[18, 24, 18, 22, 18]])

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

ax.pie(data[0], radius=1, startangle=90, counterclock=False, colors=['#FFA500', '#00FF00', '#FFD700', '#FFFF00', '#FFC0CB'])

circle = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(circle)

ax.set_title("Real Estate and Housing Market Overview - 2023")
ax.legend(data_labels, loc="upper right", bbox_to_anchor=(1.2, 0.8))
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_25.png')
plt.clf()