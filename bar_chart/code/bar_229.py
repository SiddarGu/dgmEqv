
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
ax = plt.subplot()

Country = ['USA', 'UK', 'Germany', 'France']
Sports_Teams = [50, 40, 35, 30]
Fans = [2.5, 2, 1.8, 1.6]

ax.bar(Country, Sports_Teams, label="Sports Teams", bottom=0)
ax.bar(Country, Fans, label="Fans", bottom=Sports_Teams)
ax.set_title("Number of Sports Teams and Fans in Four Countries in 2021")
ax.set_xticklabels(Country, rotation=45, ha='right', wrap=True)
ax.legend(loc="upper right")
plt.tight_layout()
plt.savefig("bar chart/png/274.png")
plt.clf()