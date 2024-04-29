
import matplotlib.pyplot as plt

country = ['USA', 'UK', 'Germany', 'France']
ch_donations = [100, 83, 90, 77]
vol_hours = [450, 500, 400, 470]

fig, ax = plt.subplots(figsize=(8,5))
ax.bar(country, ch_donations, label="Charitable Donations (million)", bottom=vol_hours)
ax.bar(country, vol_hours, label="Volunteer Hours (million)")
ax.set_title("Charitable donations and volunteer hours in four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Amount")
ax.legend(loc="upper left")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('./bar chart/png/1.png')
plt.clf()