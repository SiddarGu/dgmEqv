
import matplotlib.pyplot as plt
plt.figure(figsize=(15,8))
ax = plt.subplot()
plt.bar(x=['2020', '2021', '2022', '2023'], height=[1000, 1100, 1200, 1300], width=0.5, label='Fossil Fuels(TWh)', tick_label=['2020', '2021', '2022', '2023'], bottom=[1100, 1300, 1400, 1500])
plt.bar(x=['2020', '2021', '2022', '2023'], height=[1100, 1300, 1400, 1500], width=0.5, label='Renewables(TWh)', tick_label=['2020', '2021', '2022', '2023'], bottom=0)
plt.title('Fossil Fuels and Renewables Energy Consumption from 2020 to 2023')
plt.legend()
plt.xticks(rotation=45, fontsize=10, wrap=True)
ax.grid(axis='y')
plt.tight_layout()
plt.savefig('bar chart/png/379.png')
plt.clf()