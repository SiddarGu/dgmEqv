
import matplotlib.pyplot as plt

country = ["USA","UK","Germany","France"]
schools = [25,30,28,32]
universities = [45,50,42,47]

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)
ax.bar(country,schools,width=0.4,label="Schools")
ax.bar(country,universities,bottom=schools,width=0.4,label="Universities")
ax.set_xticklabels(country,rotation=45,ha="right")
ax.set_title("Number of schools and universities in four countries in 2021")
ax.legend()
plt.tight_layout()
plt.savefig("bar chart/png/187.png")
plt.clf()