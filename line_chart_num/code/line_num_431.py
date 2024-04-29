
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))

x=["K","1","2","3","4","5","6","7","8"]
y=[2.5,2.8,3.2,3.6,3.9,4.1,4.4,4.7,5]
plt.plot(x,y,linestyle='--', marker='o', color='g',label="Average GPA")
plt.xticks(x, rotation=45)
plt.title("Average GPA for each grade in Primary School")
plt.xlabel("Grade")
plt.ylabel("Average GPA")

for a,b in zip(x,y):
    plt.annotate(str(b),xy=(a,b))

plt.legend()
plt.tight_layout()
plt.savefig("line chart/png/538.png")
plt.clf()