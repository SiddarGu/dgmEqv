
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))

years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
SAT_scores = [1000, 1100, 1200, 1100, 1200, 1300, 1400]
ACT_scores = [20, 22, 24, 26, 28, 30, 32]
plt.plot(years, SAT_scores, label="SAT", color='black', marker='o', linewidth=2, markersize=7)
plt.plot(years, ACT_scores, label="ACT", color='red', marker='o', linewidth=2, markersize=7)
plt.title("Average SAT and ACT scores from 2001 to 2007")
plt.xlabel('Year')
plt.ylabel('Score')
plt.xticks(years)
plt.legend(loc='upper left')

for x, y in zip(years, SAT_scores):
    plt.annotate('{}'.format(y), xy=(x,y), xytext=(-10, 10), textcoords='offset points', rotation=45)
for x, y in zip(years, ACT_scores):
    plt.annotate('{}'.format(y), xy=(x,y), xytext=(-35, -30), textcoords='offset points', rotation=45, wrap=True)

plt.tight_layout()
plt.grid()
plt.savefig('line chart/png/536.png')
plt.clf()