
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 7, 3.8],
        ['UK', 8, 3.5],
        ['Germany', 9, 3.7],
        ['France', 7.5, 3.6]]

def plot(data):
    countries, hours, avg_gpa = zip(*data)
    x_pos = np.arange(len(countries))
    
    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(x_pos, hours, color='b', align='center', label='Hours')
    ax.bar(x_pos, avg_gpa, color='g', bottom=hours, align='center', label='GPA')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(countries)
    ax.set_title('Average School Hours and GPA in four countries in 2021')
    plt.tight_layout()
    plt.legend()
    for xpos, ypos, yval in zip(x_pos, hours, avg_gpa):
        ax.annotate(str(yval), xy=(xpos, ypos + yval/2))
    plt.savefig('Bar Chart/png/71.png')
    plt.clf()

plot(data)