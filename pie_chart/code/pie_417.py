
import matplotlib.pyplot as plt

plt.figure(figsize=(8,8))
labels = 'Impressionism', 'Realism', 'Expressionism', 'Surrealism', 'Pop Art', 'Post-Impressionism'
sizes = [25, 15, 20, 10, 15, 15]
explode = (0.1, 0, 0, 0, 0, 0)  # only "explode" the 1st slice

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize':14, 'color':'black'})
plt.title("Popularity of Painting Styles in the World, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/48.png')
plt.clf()