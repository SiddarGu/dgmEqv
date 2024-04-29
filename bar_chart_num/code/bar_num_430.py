
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
Years = [2000, 2005, 2010, 2015, 2020]
Num_Scientists = [20000, 25000, 30000, 35000, 40000]
Num_Engineers = [40000, 45000, 50000, 55000, 60000]
ax.bar(Years, Num_Scientists, label='Scientists')
ax.bar(Years, Num_Engineers, bottom=Num_Scientists, label='Engineers')
plt.xticks(Years)
for x,y in zip(Years,Num_Scientists):
    label = "{}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,2), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
for x,y in zip(Years,Num_Engineers):
    label = "{}".format(y)
    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,2), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
plt.title('Number of Scientists and Engineers in the last 20 years', fontsize=10)
ax.legend(loc='upper center')
plt.tight_layout()
plt.savefig("Bar Chart/png/431.png")
plt.clf()