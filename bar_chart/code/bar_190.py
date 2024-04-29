
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
ax = plt.subplot()
ax.bar(["2020", "2021", "2022", "2023"], [10,13,15,18], width=0.2, label="Renewable Energy(%)")
ax.bar(["2020", "2021", "2022", "2023"], [30,28,26,24], width=0.2, bottom=[10,13,15,18], label="Air Pollution(ppm)")
ax.bar(["2020", "2021", "2022", "2023"], [50,45,40,35], width=0.2, bottom=[40,41,41,42], label="Water Pollution(ppm)")
ax.set_xticklabels(["2020", "2021", "2022", "2023"], rotation=0)
ax.set_title('Environment and Sustainability indicators from 2020 to 2023')
ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()
plt.savefig('bar chart/png/502.png')
plt.clf()