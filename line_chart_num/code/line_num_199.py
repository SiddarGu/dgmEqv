
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)
ax.plot( [2018,2019,2020,2021,2022], [20,25,30,35,40],label="Donations A(million dollars)")
ax.plot( [2018,2019,2020,2021,2022], [30,35,40,45,50],label="Donations B(million dollars)")
ax.plot( [2018,2019,2020,2021,2022], [25,30,35,40,45],label="Donations C(million dollars)")
ax.legend(loc='upper right')
ax.set_xticks([2018,2019,2020,2021,2022])
ax.set_title("Donations of three charity organizations in the past five years")
for a,b in zip([2018,2019,2020,2021,2022], [20,25,30,35,40]):
    ax.annotate(str(b),xy=(a,b),xytext=(a,b+5))
for a,b in zip([2018,2019,2020,2021,2022], [30,35,40,45,50]):
    ax.annotate(str(b),xy=(a,b),xytext=(a,b+5))
for a,b in zip([2018,2019,2020,2021,2022], [25,30,35,40,45]):
    ax.annotate(str(b),xy=(a,b),xytext=(a,b+5))
plt.tight_layout()
fig.savefig('line chart/png/184.png')
plt.clf()