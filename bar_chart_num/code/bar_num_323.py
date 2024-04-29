
import matplotlib.pyplot as plt

country = ["USA","UK","Germany","France"]
court_cases = [10000,8000,9000,7000]
lawyers = [4000,5000,4500,5000]

fig, ax = plt.subplots(figsize=(12, 7))
ax.bar(country, court_cases, color="#f9a65a", label="Court Cases")
ax.bar(country, lawyers, bottom=court_cases, color="#9e66ab", label="Lawyers")
ax.set_title("Number of court cases and lawyers in four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Number")
ax.legend(loc="upper right")
ax.set_xticks(country)

for i, v in enumerate(court_cases):
    ax.text(i - 0.2, v + 1000, str(v), color="#f9a65a", fontsize=14)
for i, v in enumerate(lawyers):
    ax.text(i - 0.2, court_cases[i] + v + 1000, str(v), color="#9e66ab", fontsize=14)

plt.tight_layout()
plt.savefig('Bar Chart/png/498.png')
plt.clf()