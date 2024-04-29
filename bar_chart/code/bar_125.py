
import matplotlib.pyplot as plt 
x = ["USA","UK","Germany","France"] 
y1 = [50,40,30,20] 
y2 = [100,90,80,70] 
y3 = [300,250,200,150] 
fig = plt.figure(figsize=(10,5)) 
ax = fig.add_subplot() 
ax.bar(x, y1, label="Doctors(1000s)", bottom=0, width=0.2, color="r") 
ax.bar(x, y2, label="Nurses(1000s)", bottom=y1, width=0.2, color="g") 
ax.bar(x, y3, label="Hospitals", bottom=[i+j for i,j in zip(y1,y2)], width=0.2, color="b") 
ax.set_title("Number of healthcare professionals and hospitals in four countries in 2021", fontsize = 14) 
ax.set_xticklabels(x, rotation=45, ha="right") 
ax.legend(loc = "upper right") 
plt.tight_layout()
plt.savefig("bar chart/png/85.png")
plt.clf()