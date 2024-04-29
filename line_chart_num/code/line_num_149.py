
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(1, 1, 1)

data = [[2001, 800, 900, 1000, 1100], 
        [2002, 1000, 1000, 1100, 1200], 
        [2003, 800, 1100, 1200, 1300], 
        [2004, 1100, 1200, 1300, 1400]]

year, enrollment_A, enrollment_B, enrollment_C, enrollment_D = zip(*data)

ax.plot(year, enrollment_A, color='red', marker='o', label="Enrollment A")
ax.plot(year, enrollment_B, color='blue', marker='v', label="Enrollment B")
ax.plot(year, enrollment_C, color='green', marker='^', label="Enrollment C")
ax.plot(year, enrollment_D, color='pink', marker='s', label="Enrollment D")

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.set_title('University Enrollment in Four Majors from 2001 to 2004')
ax.set_xlabel('Year')
ax.set_ylabel('Enrollment (thousands)')
ax.legend(loc='upper left', bbox_to_anchor=(0.05, 0.95))

for i, txt in enumerate(enrollment_A):
    ax.annotate(txt, (year[i], enrollment_A[i]))
for i, txt in enumerate(enrollment_B):
    ax.annotate(txt, (year[i], enrollment_B[i]))
for i, txt in enumerate(enrollment_C):
    ax.annotate(txt, (year[i], enrollment_C[i]))
for i, txt in enumerate(enrollment_D):
    ax.annotate(txt, (year[i], enrollment_D[i]))

plt.tight_layout()
plt.savefig('line chart/png/261.png')
plt.clf()