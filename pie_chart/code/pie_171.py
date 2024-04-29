
import matplotlib.pyplot as plt
plt.figure(figsize=(9,9))
plt.subplot()
music_genres=["Pop","Hip-Hop","Rock","Country","EDM","Jazz","Classical"]
percentages = [30,20,15,10,10,10,5]

plt.pie(percentages, labels=music_genres, autopct="%1.1f%%", pctdistance=0.8, 
        wedgeprops={"edgecolor":"black"},textprops={'fontsize': 14})

plt.title("Music Genre Popularity in the US, 2023", fontsize=20)
plt.tight_layout()
plt.savefig('pie chart/png/245.png')
plt.clf()