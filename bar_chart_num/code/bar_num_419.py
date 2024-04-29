
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
ax = plt.subplot()

Genre = ["Abstract","Realism","Impressionism","Surrealism"]
Painting = [50,40,60,40]
Photography = [60,50,70,50]
Sculpture = [70,60,80,60]

x = range(len(Genre))
ax.bar(x,Painting,label="Painting",width=0.3)
ax.bar(x,Photography,bottom=Painting,label="Photography",width=0.3)
ax.bar(x,Sculpture,bottom=[i+j for i,j in zip(Painting,Photography)],label="Sculpture",width=0.3)

ax.set_title("Number of artworks in four genres in 2021")
ax.set_xticks(x)
ax.set_xticklabels(Genre)
ax.legend(loc="upper left")

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x(), p.get_height()))

plt.tight_layout()
plt.savefig("Bar Chart/png/165.png")
plt.clf()