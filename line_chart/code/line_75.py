
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

grade = [5, 6, 7, 8, 9]
math_score = [90, 95, 100, 105, 95]
science_score = [80, 85, 90, 95, 90]
soc_score = [85, 90, 95, 100, 90]

ax.plot(grade, math_score, label='Mathematics Score', marker='o', color='blue')
ax.plot(grade, science_score, label='Science Score', marker='o', color='green')
ax.plot(grade, soc_score, label='Social Sciences Score', marker='o', color='orange')

ax.set_title('Academic Performance of Grade 5 to 9 Students in Mathematics, Science and Social Sciences', fontsize=14)
ax.set_xlabel('Grade')
ax.set_ylabel('Score')
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

plt.legend(loc='upper left', bbox_to_anchor=(1,1))
plt.tight_layout()
plt.savefig('line chart/png/465.png')
plt.clf()