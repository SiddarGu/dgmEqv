import matplotlib.pyplot as plt
import squarify

# Given data
data_str = """Category,Market Share (%)
Banking,25
Insurance,20
Investments,20
Real Estate,15
Financial Services,10
Fintech,5
Asset Management,3
Wealth Management,2"""

# Parse the data
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]  # Extracting the column labels
line_labels = [line.split(',')[0] for line in data_lines[1:]]  # Extracting the row labels
data = [float(line.split(',')[1]) for line in data_lines[1:]]  # Extracting the numerical data

# Create a treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.7, text_kwargs={'wrap': True})
plt.title("Financial Market Share Distribution by Category")

# Resize the image and save it
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1004.png', format='png')

# Clear the current figure to release memory and avoid overlaps
plt.clf()
