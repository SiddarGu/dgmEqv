
import matplotlib.pyplot as plt

data = [['USA', 50, 3.5], ['UK', 60, 4.5], ['Germany', 70, 5.5], ['France', 65, 4.0]]

country, turnout, spending = zip(*data)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
ax.bar(country, turnout, width=0.4, align="center", label="Voter Turnout")
ax.bar(country, spending, bottom=turnout, width=0.4, align="center", label="Government Spending")
ax.set_title('Voter turnout and government spending in four countries in 2021')
ax.set_xticks(country)
ax.set_xlabel("Country")
ax.set_ylabel("Percentage (%) & Billion ($B)")
ax.legend(loc="upper right")

for i in range(0, len(country)):
    ax.annotate('{}%'.format(turnout[i]), (country[i], turnout[i]/2), ha="center")
    ax.annotate('${}B'.format(spending[i]), (country[i], turnout[i] + spending[i]/2), ha="center")

plt.tight_layout()
fig.savefig('Bar Chart/png/359.png')
plt.clf()