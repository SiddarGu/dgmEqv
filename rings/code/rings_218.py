
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_labels = ["Vaccination Coverage", "Nutrition Education", "Mental Health Support", "Healthcare Accessibility", "Disease Prevention"]
data = [17, 15, 25, 25, 18]
line_labels = ["Category", "ratio"]

fig, ax = plt.subplots(figsize=(10, 8))
ax.pie(data, startangle=90, counterclock=False, labels=data_labels, autopct='%1.1f%%')
ax.set_title("Health and Wellbeing in 2023")

c = plt.Circle((0, 0), 0.7, color='white')
ax.add_artist(c)

ax.legend(data_labels, bbox_to_anchor=(1, 0.8))

plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_75.png', bbox_inches='tight')
plt.clf()