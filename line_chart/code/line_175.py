
import matplotlib.pyplot as plt
import pandas as pd

data=[[200,15000],[225,16000],[250,17000],[275,18000]]
columns=['Revenue(million dollars)','Attendance']
index=['NBA All-Star Game 2021','NBA All-Star Game 2022','NBA All-Star Game 2023','NBA All-Star Game 2024']
df = pd.DataFrame(data=data,index=index,columns=columns)
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.plot(df.index,df['Revenue(million dollars)'],label='Revenue(million dollars)',marker='o')
ax.plot(df.index,df['Attendance'],label='Attendance',marker='o')
ax.legend(loc='upper left')
ax.set_title('Revenue and Attendance in NBA All-Star Games from 2021-2024')
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.savefig('line chart/png/245.png')
plt.clf()