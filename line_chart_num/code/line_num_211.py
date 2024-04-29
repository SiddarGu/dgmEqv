
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 7))

# create subplot
ax = plt.subplot()

# set x,y axis
x = [2001, 2002, 2003, 2004]
y1 = [50, 51, 53, 55]
y2 = [60, 62, 64, 66]
y3 = [4000, 4500, 4700, 4800]
y4 = [400, 420, 440, 460]

# set x and y axis label
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number', fontsize=14)

# set title
ax.set_title('Growth of Art Institutions and Artworks in the US from 2001 to 2004', fontsize=14)

# plot line chart
ax.plot(x, y1, marker='o', linestyle="--", color='r', label='Museums')
ax.plot(x, y2, marker='o', linestyle="--", color='b', label='Galleries')
ax.plot(x, y3, marker='o', linestyle="--", color='g', label='Paintings')
ax.plot(x, y4, marker='o', linestyle="--", color='y', label='Sculptures')

# set xticks to prevent interpolation
ax.set_xticks(x)

# set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# add annotations
ax.annotate('50', xy=(2001, 50))
ax.annotate('51', xy=(2002, 51))
ax.annotate('53', xy=(2003, 53))
ax.annotate('55', xy=(2004, 55))
ax.annotate('60', xy=(2001, 60))
ax.annotate('62', xy=(2002, 62))
ax.annotate('64', xy=(2003, 64))
ax.annotate('66', xy=(2004, 66))
ax.annotate('4000', xy=(2001, 4000))
ax.annotate('4500', xy=(2002, 4500))
ax.annotate('4700', xy=(2003, 4700))
ax.annotate('4800', xy=(2004, 4800))
ax.annotate('400', xy=(2001, 400))
ax.annotate('420', xy=(2002, 420))
ax.annotate('440', xy=(2003, 440))
ax.annotate('460', xy=(2004, 460))

# draw grid
ax.grid(True, linestyle='dotted')

# resize the image
plt.tight_layout()

# save image
plt.savefig('line chart/png/335.png')

# clear current image state
plt.clf()