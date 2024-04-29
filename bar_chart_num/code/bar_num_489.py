
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA", "UK", "Germany", "France"]
Broadband_Speed = [50, 70, 60, 65]
User_Penetration_Rate = [78, 80, 83, 79]

x = np.arange(len(Country))
width = 0.35

fig = plt.figure(figsize=(15,7))
ax = fig.add_subplot()
ax.bar(x, Broadband_Speed, width, label='Broadband Speed (Mbps)')
ax.bar(x + width, User_Penetration_Rate, width, label='User Penetration Rate (%)')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(Country)
ax.legend(loc='best')
ax.set_title("Broadband speed and user penetration rate in four countries in 2021")
for i in range(len(Country)):
    ax.annotate(str(Broadband_Speed[i]), (x[i] , Broadband_Speed[i] + 2))
    ax.annotate(str(User_Penetration_Rate[i]), (x[i] + width, User_Penetration_Rate[i] + 2))
plt.tight_layout()
plt.savefig("Bar Chart/png/455.png")
plt.clf()