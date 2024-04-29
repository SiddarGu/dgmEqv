
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker

plt.figure(figsize=(15,8))
ax = plt.subplot()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.plot(['6th','7th','8th','9th','10th'], [80,85,90,95,100], label='Average Test Score', marker='o')
plt.plot(['6th','7th','8th','9th','10th'], [85,90,95,90,95], label='Average Reading Score', marker='o')
plt.plot(['6th','7th','8th','9th','10th'], [75,80,85,90,95], label='Average Math Score', marker='o')

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
plt.xticks(rotation=45)
plt.title('Average Scores of Students by Grade Level in a School District in 2021')
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")
plt.tight_layout()

for i,j in zip(['6th','7th','8th','9th','10th'], [80,85,90,95,100]):
    ax.annotate(str(j),xy=(i,j))

for i,j in zip(['6th','7th','8th','9th','10th'], [85,90,95,90,95]):
    ax.annotate(str(j),xy=(i,j))

for i,j in zip(['6th','7th','8th','9th','10th'], [75,80,85,90,95]):
    ax.annotate(str(j),xy=(i,j))

plt.savefig('line chart/png/107.png')

plt.clf()