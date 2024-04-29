
import matplotlib.pyplot as plt
import pandas as pd

data = [[2018, 200, 300, 400],[2019, 250, 350, 450],[2020, 220, 320, 420],[2021, 260, 360, 460]]
df = pd.DataFrame(data,columns=['Year','Enrollment A','Enrollment B','Enrollment C'])

plt.figure(figsize=(15,6))
ax = plt.subplot()
ax.plot(df.Year, df['Enrollment A'], label='Enrollment A')
ax.plot(df.Year, df['Enrollment B'], label='Enrollment B')
ax.plot(df.Year, df['Enrollment C'], label='Enrollment C')
plt.xticks(df.Year)
plt.title("Annual Enrollment in Three Schools from 2018 to 2021")
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig("line chart/png/35.png")
plt.clf()