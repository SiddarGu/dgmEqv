
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
year = [2015, 2016, 2017, 2018]
enroll_rate = [90, 92, 94, 95]
grad_rate = [75, 77, 80, 82]

ax = plt.subplot()
ax.bar(year, enroll_rate, width=0.3, color='blue', label='Enrollment rate(%)')
ax.bar([i+0.3 for i in year], grad_rate, width=0.3, color='red', label='Graduation rate(%)')
ax.set_xticks([i+0.15 for i in year])
ax.set_xticklabels(year, rotation=0, wrap=True)
ax.legend()
plt.title('Enrollment and Graduation Rates of Students from 2015 to 2018')
plt.tight_layout()
plt.savefig('bar chart/png/352.png')
plt.clf()