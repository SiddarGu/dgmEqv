
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
x_data = ["USA","UK","Germany","France"]
y_data = [200,180,220,210]
y_data_1 = [150,170,190,180]
y_data_2 = [130,100,110,120]
ax.bar(x_data, y_data, label="Museums", width=0.3, bottom=0)
ax.bar(x_data, y_data_1, label="Galleries", width=0.3, bottom=y_data)
ax.bar(x_data, y_data_2, label="Theaters", width=0.3, bottom=y_data_1)
plt.xticks(x_data, x_data, rotation=45, ha="right", wrap=True)
plt.title("Number of arts and culture venues in four countries in 2021")
ax.legend(loc="upper left")
plt.tight_layout()
plt.savefig("bar chart/png/400.png")
plt.clf()