
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

Country = ['USA', 'UK', 'Germany', 'France']
Online_Shopping = [100, 110, 120, 130]
In_store_Shopping = [200, 220, 210, 230]

ax.bar(Country, Online_Shopping, label='Online Shopping', bottom=In_store_Shopping)
ax.bar(Country, In_store_Shopping, label='In-store Shopping')

for i, v in enumerate(Online_Shopping):
    ax.text(i, v+10, str(v), ha='center')
for i, v in enumerate(In_store_Shopping):
    ax.text(i, v+10, str(v), ha='center')

ax.set_title('Shopping behavior of four countries in 2021')
ax.set_xticks(Country)
ax.set_ylabel('Number of people')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig("Bar Chart/png/355.png")
plt.clf()