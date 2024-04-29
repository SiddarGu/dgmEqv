
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
Manufacturing_Output = [800,700,600,500]
Agricultural_Output = [200,400,350,450]
Service_Output = [500,600,400,350]

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111)

ax.bar(Country, Manufacturing_Output, width=0.5, label="Manufacturing Output")
ax.bar(Country, Agricultural_Output, bottom=Manufacturing_Output, width=0.5, label="Agricultural Output")
ax.bar(Country, Service_Output, bottom=[x + y for x, y in zip(Manufacturing_Output,Agricultural_Output)], width=0.5, label="Service Output")

ax.set_title("Manufacturing, Agricultural, and Service Output in four countries in 2021")
ax.set_ylabel("Output (million)")
ax.set_xlabel("Country")
ax.legend(loc="best")
ax.grid(True)

for i, v in enumerate(Manufacturing_Output):
    ax.text(i - 0.2, v + 10, str(v))

for i, v in enumerate(Agricultural_Output):
    ax.text(i - 0.2, v + Manufacturing_Output[i] + 10, str(v))

for i, v in enumerate(Service_Output):
    ax.text(i - 0.2, v + Manufacturing_Output[i] + Agricultural_Output[i] + 10, str(v))

plt.tight_layout()
plt.xticks(Country)
plt.savefig('Bar Chart/png/514.png')
plt.clf()