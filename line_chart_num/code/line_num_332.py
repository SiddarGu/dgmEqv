
import matplotlib.pyplot as plt
plt.figure(figsize=(14,7))
ax = plt.subplot()
plt.plot([2019,2020,2021,2022], [0.8,0.9,1,0.7], label='Military')
plt.plot([2019,2020,2021,2022], [0.2,0.3,0.4,0.6], label='Education')
plt.plot([2019,2020,2021,2022], [0.7,0.8,0.9,1], label='Healthcare')
ax.set_xticks([2019,2020,2021,2022])
ax.set_xticklabels(['2019','2020','2021','2022'], rotation=0, wrap=True)
plt.xlabel('Year')
plt.ylabel('Spending (trillion dollars)')
plt.title('Government Spending Trends in United States from 2019 to 2022')
plt.legend()
for x, y in zip([2019,2020,2021,2022], [0.8,0.9,1,0.7]):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
for x, y in zip([2019,2020,2021,2022], [0.2,0.3,0.4,0.6]):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
for x, y in zip([2019,2020,2021,2022], [0.7,0.8,0.9,1]):
    label = "{:.2f}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.tight_layout()
plt.savefig('line chart/png/101.png')
plt.clf()