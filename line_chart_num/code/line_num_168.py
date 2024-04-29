
import matplotlib.pyplot as plt

data = [
    [2019, 80, 65, 50], 
    [2020, 82, 70, 60],
    [2021, 85, 75, 65], 
    [2022, 87, 80, 70]
]

year = [row[0] for row in data] 
social_networking_usage = [row[1] for row in data] 
online_shopping_usage = [row[2] for row in data]
streaming_service_usage = [row[3] for row in data]

fig, ax = plt.subplots(figsize=(15, 8))

ax.plot(year, social_networking_usage, label='Social Networking Usage')
ax.plot(year, online_shopping_usage, label='Online Shopping Usage')
ax.plot(year, streaming_service_usage, label='Streaming Service Usage')

for i, txt in enumerate(social_networking_usage):
    ax.annotate(txt, (year[i], social_networking_usage[i]))

for i, txt in enumerate(online_shopping_usage):
    ax.annotate(txt, (year[i], online_shopping_usage[i]))

for i, txt in enumerate(streaming_service_usage):
    ax.annotate(txt, (year[i], streaming_service_usage[i]))

plt.xticks(year)
plt.title('Online usage trend in the United States from 2019 to 2022')
plt.xlabel('Year')
plt.ylabel('Internet Usage Percentage')
ax.legend(loc="best")
plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/516.png')
plt.clf()