
import matplotlib.pyplot as plt

country = ["USA", "UK", "Germany", "France"]
law_grads = [5000, 4500, 4000, 4300]
lawyers = [18000, 17000, 16000, 15000]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.bar(country, law_grads, label="Law Graduates", bottom=lawyers, width=0.4, color="orange")
ax.bar(country, lawyers, label="Lawyers", width=0.4, color="blue")
ax.set_title("Number of law graduates and lawyers in four countries in 2021")
ax.set_xlabel("Country")
ax.set_xticks(country)
ax.legend(loc='upper left')
for i, v in enumerate(law_grads):
    ax.text(i - 0.2, v + lawyers[i] + 1000, str(v), color='black', fontsize=10)
for i, v in enumerate(lawyers):
    ax.text(i - 0.2, v + 500, str(v), color='black', fontsize=10)
plt.tight_layout()
plt.savefig("Bar Chart/png/110.png")
plt.clf()