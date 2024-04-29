import matplotlib.pyplot as plt
import numpy as np

def create_plot(x_values, y_values, data, save_path):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    color_list = ['r', 'g', 'b']
    for i in range(data.shape[1]):
        ax.bar3d(np.arange(len(x_values)), [i]*len(x_values), np.zeros(len(x_values)), 0.4, 0.4, data[:, i], color=color_list[i % len(color_list)], alpha=0.7)

    ax.set_xticks(np.arange(len(x_values)))
    ax.set_yticks(np.arange(len(y_values)))
    ax.set_xticklabels(x_values, rotation=45, horizontalalignment='right')
    ax.set_yticklabels(y_values)

    ax.set_title('Overview of Case Progression in Legal Affairs from 2016 to 2020')

    plt.tight_layout()
    plt.savefig(save_path, format='png')
    plt.close()

info = "Year,Number of Cases Resolved,Number of Active Cases,Number of New Cases\n 2016,600,750,800\n 2017,650,800,950\n 2018,700,850,1100\n 2019,750,900,1200\n 2020,800,980,1300"
data_list = [item.split(',') for item in info.split('\n')]
y_values = data_list[0][1:]
x_values = [item[0].strip() for item in data_list[1:]]
data = np.array([[np.float32(j) for j in i[1:]] for i in data_list[1:]])

create_plot(x_values, y_values, data, '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/172_202312302235.png')
