import matplotlib.pyplot as plt
import squarify

# Given data
data_string = """Hospital Services,35
Physician Services,25
Prescription Drugs,20
Nursing Home Care,10
Dental Services,5
Mental Health Services,3
Medical Equipment,2"""

# Splitting the data into lines and parsing them
data_lines = data_string.split('\n')

# Extracting labels and associated data
data_labels = [line.split(',')[0] for line in data_lines]
data = [float(line.split(',')[1]) for line in data_lines]

# Since there isn't a separate line header, line_labels is not populated
line_labels = []

# Creating the treemap
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=data, label=data_labels, alpha=.8, text_kwargs={'wrap': True})
plt.axis('off')
plt.title('Healthcare Expenditure Distribution by Services in 2023')

# Tidy up and save the figure to the absolute path
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1003.png')
plt.clf()
