import numpy as np
import matplotlib.pyplot as plt

# Represent the data
y_values = ['Number of Students (1000s)', 'Faculty Size', 'Annual Tuition Fees ($000)']
x_values = ['Harvard', 'Yale', 'MIT', 'Stanford', 'Princeton', 'Columbia', 'Brown', 'Cornell']
data = np.array([[20, 2.3, 50], [12, 1.9, 52], [11, 2.1, 49], [16, 2.4, 55],
                 [8, 1.6, 48], [19, 2.2, 60], [9, 1.7, 54], [14, 2.0, 56]], dtype=np.float32)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

colors = ['r', 'g', 'b']
for c, k in zip(colors, range(data.shape[1])):
    xs = np.arange(len(x_values))
    ys = data[:, k]
    ax.bar(xs, ys, k, zdir='y', color=c, alpha=0.8)

ax.set_xlabel('Schools')
ax.set_ylabel('Metrics')
ax.set_zlabel('Value')
ax.set_xticks(np.arange(len(x_values)))
ax.set_yticks(np.arange(len(y_values)))
ax.set_xticklabels(x_values, rotation=45, ha='right')
ax.set_yticklabels(y_values, ha='left')
ax.set_title('Annual Tuition Fees in Comparison with the Student Population and Faculty Size at Top US Universities')
ax.view_init(30, -20)

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/3D/png/187_202312302235.png')

# Clear the current figure after saving it
plt.clf()
