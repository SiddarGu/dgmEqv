
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

year = [2001, 2002, 2003, 2004, 2005]
criminal_cases = [500000, 400000, 450000, 480000, 510000]
civil_cases = [100000, 200000, 180000, 150000, 170000]

ax.plot(year, criminal_cases, label="Criminal Cases Filed", color="red", marker="o")
ax.plot(year, civil_cases, label="Civil Cases Filed", color="green", marker="o")

ax.set_xlabel("Year")
ax.set_ylabel("Number of Cases Filed")
ax.set_title("Cases filed in US courts from 2001-2005")
ax.set_xticks(year)
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig("line chart/png/463.png")
plt.clf()