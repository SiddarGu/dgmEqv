
import matplotlib.pyplot as plt
import numpy as np

data = [[1, 80, 85, 90],
        [2, 85, 90, 95],
        [3, 90, 95, 100],
        [4, 95, 100, 105]]

labels = ["Grade","Math","Science","English"]

grade,math,science,english = np.array(data).T

x = np.arange(len(grade))

width = 0.2

fig, ax = plt.subplots(figsize=(8, 6))

rects1 = ax.bar(x, math, width, label=labels[1])
rects2 = ax.bar(x + width, science, width, label=labels[2])
rects3 = ax.bar(x + width + width, english, width, label=labels[3])

ax.set_xticks(x + width / 2)
ax.set_xticklabels(grade)
ax.set_title("Academic scores of Math, Science and English for grades 1 to 4")
ax.legend()

def add_value_labels(ax, spacing=5):
    for rect in ax.patches:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        space = spacing
        va = 'bottom'

        if y_value < 0:
            space *= -1
            va = 'top'

        label = "{:.0f}".format(y_value)

        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.

add_value_labels(ax)

fig.tight_layout()
plt.savefig('Bar Chart/png/524.png')
plt.clf()