
import matplotlib.pyplot as plt
import numpy as np

year = np.array([2010, 2011, 2012, 2013])
civil_cases = np.array([25, 30, 28, 32])
criminal_cases = np.array([45, 50, 48, 51])
family_cases = np.array([20, 15, 18, 17])
employment_cases = np.array([10, 12, 14, 15])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

ax.plot(year, civil_cases, color='b', marker='o',label="Civil Cases")
ax.plot(year, criminal_cases, color='y', marker='*',label="Criminal Cases")
ax.plot(year, family_cases, color='m', marker='s',label="Family Cases")
ax.plot(year, employment_cases, color='g', marker='^',label="Employment Cases")

ax.set_title("Changes in Types of Cases Handled by the Legal System in the Past Decade")
ax.set_xlabel('Year')
ax.set_ylabel('Number of Cases')

ax.set_xticks(year)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.savefig('line chart/png/203.png')
plt.clf()