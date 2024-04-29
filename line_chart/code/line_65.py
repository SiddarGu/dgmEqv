
import matplotlib.pyplot as plt
import numpy as np

data = [['Germany',200, 300],
        ['France',250, 330],
        ['Italy',300, 400],
        ['Spain',220, 390]]

x_data = np.arange(len(data))

plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.set_title('Number of Museums and Galleries in Europe in 2021')
ax.set_xticks(x_data)
ax.set_xticklabels([country[0] for country in data],rotation=45, ha="right", rotation_mode="anchor")

ax.plot(x_data, [country[1] for country in data], label='Number of Museums')
ax.plot(x_data, [country[2] for country in data], label='Number of Galleries')
ax.legend(loc='upper left')

plt.grid(True, linestyle='--', color='0.75')
plt.tight_layout()
plt.savefig('line chart/png/8.png')
plt.clf()