
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

country = ["USA", "UK", "Germany", "France"]
charitable_donations = [10, 8, 7, 9]
nonprofit_organizations = [200, 150, 180, 220]

ax.bar(country, charitable_donations, width=0.3, bottom=0, label="Charitable Donations (million)")
ax.bar(country, nonprofit_organizations, width=0.3, bottom=charitable_donations, label="Nonprofit Organizations")

# place the labels in the middle of the bars
for i, donation in enumerate(charitable_donations):
    ax.annotate(str(donation), xy=(i, donation/2))
for i, organization in enumerate(nonprofit_organizations):
    ax.annotate(str(organization), xy=(i, charitable_donations[i] + organization/2))

ax.set_xticks(range(len(country)))
ax.set_xticklabels(country)
ax.set_title("Charitable donations and number of nonprofit organizations in four countries in 2021")
ax.legend(loc="upper right")

fig.tight_layout()
plt.savefig("Bar Chart/png/127.png")

plt.clf()