
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

country = ['USA', 'UK', 'Germany', 'France']
gpa = [3.5, 3.7, 3.6, 3.8]
test_score = [85, 80, 75, 90]

ax.bar(country, gpa, label='Average GPA', bottom = test_score, color='g')
ax.bar(country, test_score, label='Average Test Score', color='b')

ax.set_title('Academic performance of students in four countries in 2021', fontsize=14)
ax.set_xlabel('Country')
ax.set_ylabel('Score')
ax.set_xticks(country)

for x, y, s in zip(country, gpa, gpa):
    ax.annotate(s, xy=(x, y), xytext=(0, 10), textcoords="offset points", ha='center', va='bottom')
for x, y, s in zip(country, test_score, test_score):
    ax.annotate(s, xy=(x, y), xytext=(0, 10), textcoords="offset points", ha='center', va='bottom')

ax.legend()
plt.tight_layout()
plt.savefig('Bar Chart/png/513.png')
plt.clf()