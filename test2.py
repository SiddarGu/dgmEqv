# count how many files are in ./altered

import os

easy_diffs = 0
easy_equivalents = 0

# list all folders in the current directory
folders = [f for f in os.listdir() if os.path.isdir(f)]

# iterate over each folder
for folder in folders:
    # go to "easy_diff" folder if it exists
    if os.path.exists(f"{folder}/easy_diff"):
        # count how many files are in "easy_diff"
        easy_diffs += len(os.listdir(f"{folder}/easy_diff"))

    # go to "easy_equivalent" folder if it exists
    if os.path.exists(f"{folder}/easy_equivalent"):
        # count how many files are in "easy_equivalent"
        easy_equivalents += len(os.listdir(f"{folder}/easy_equivalent"))

print(f"easy_diffs: {easy_diffs}")
print(f"easy_equivalents: {easy_equivalents}")