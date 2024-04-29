
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
ax = plt.subplot()
ax.bar(x=[2019,2020,2021,2022], height=[10,12,14,16], width=0.4, label='Research Grants(billion)', color='pink')
ax.bar(x=[2019.5,2020.5,2021.5,2022.5], height=[5,7,9,11], width=0.4, label='Cost of Equipment(billion)', color='green')
ax.set_xticks([2019.5, 2020.5, 2021.5, 2022.5])
ax.set_xlabel("Year")
ax.set_ylabel("Amount(billion)")
plt.title("Research Grants and Cost of Equipment in science and engineering from 2019 to 2022", fontsize=20)
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig('bar chart/png/95.png')
plt.clf()