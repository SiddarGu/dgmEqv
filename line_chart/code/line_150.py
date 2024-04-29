
import matplotlib.pyplot as plt
import numpy as np

data = [[2001, 800000, 700000],
        [2002, 900000, 600000],
        [2003, 600000, 800000],
        [2004, 700000, 900000],
        [2005, 800000, 700000],
        [2006, 900000, 600000]]

fig, ax = plt.subplots(figsize=(10,5))

year = [x[0] for x in data] 
civil_cases = [x[1] for x in data] 
criminal_cases = [x[2] for x in data]

ax.plot(year, civil_cases, label="Civil Cases")
ax.plot(year, criminal_cases, label="Criminal Cases")

plt.xticks(year)
plt.title('Annual comparison of civil and criminal cases in the US', fontsize=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of cases', fontsize=12)
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/418.png')
plt.clf()