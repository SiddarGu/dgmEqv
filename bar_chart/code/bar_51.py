
import matplotlib.pyplot as plt
import numpy as np

orgs = ["Red Cross", "Habitat for Humanity", "UNICEF", "World Vision"]
donations = [500, 600, 450, 550]
volunteers = [2000, 3000, 2500, 2700]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

w = 0.25
x = np.arange(len(orgs))

ax.bar(x - w/2, donations, width=w, color="blue", label="Donations (1000s)")
ax.bar(x + w/2, volunteers, width=w, color="orange", label="Volunteers")

ax.set_title("Donation and volunteer numbers for four charity and nonprofit organizations in 2021")
ax.set_xticks(x)
ax.set_xticklabels(orgs, rotation=45, ha="right", wrap=True)
ax.set_ylabel("Numbers")
ax.legend(loc=1)

fig.tight_layout()

plt.savefig("bar chart/png/148.png")
plt.clf()