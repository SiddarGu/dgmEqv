'''
    Put this file under the same directory as the ChartX_annotation.json file

'''

import json, re, random, os
import pandas as pd


with open("ChartX_annotation.json", encoding="utf-8") as f:
    data = json.load(f)

codes = []

pattern = r"(plt\.bar\([^)]+\))"

for ii in data:
    codes.append(ii["redrawing"]["output"])

codes = [code for code in codes if re.search(pattern, code)]

# pattern match color='x'
color_single_char_pattern = r"color\s?=\s?'([^']+)'"

# pattern match color='#xxxxxx'
color_hex_pattern = r"color\s?=\s?'(#[0-9a-fA-F]{6})'"

# pattern match color=letters
color_letters_pattern = r"color\s?=\s?'([a-zA-Z]+)'"

# pattern match color=(x, x, x)
color_rgb_pattern = r"color\s?=\s?\(([^)]+)\)"

# pattern match rotation=num
rotation_pattern = r"rotation\s?=\s?([0-9]+)"

# pattern match figsize=(x, y)
figsize_pattern = r"figsize\s?=\s?\(([^)]+)\)"

codes = [
    code
    for code in codes
    if re.search(color_single_char_pattern, code)
    or re.search(color_hex_pattern, code)
    or re.search(color_letters_pattern, code)
    or re.search(color_rgb_pattern, code)
]

# get all the colors
colors = []

for code in codes:
    colors.extend(re.findall(color_single_char_pattern, code))
    colors.extend(re.findall(color_hex_pattern, code))
    colors.extend(re.findall(color_letters_pattern, code))
    colors.extend(re.findall(color_rgb_pattern, code))

# remove duplicates
colors = list(set(colors))

def randomize_color(color):
    return "#%06x" % random.randint(0, 0xFFFFFF)
    
def randomize_rotation(rotation):
    degrees = [0, 45]
    return random.choice(degrees)

def randomize_figsize(figsize):
    return tuple(random.randint(1, 10) for _ in range(2))

data_pattern = r'\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*\[.*\]\s*'

bar_pattern = r".bar\("

def bar_to_barh(code):
    width_pattern = r"width\s?=\s?([A-Za-z0-9]+)"
    width_to_height = lambda x: f"height={x.group(1)}"
    code = re.sub(width_pattern, width_to_height, code)

    bottom_pattern = r"bottom\s?=\s?([A-Za-z0-9]+)"
    bottom_to_left = lambda x: f"left={x.group(1)}"
    code = re.sub(bottom_pattern, bottom_to_left, code)

    xticks_pattern = "xticks"
    xticks_to_yticks = lambda x: "yticks"
    code = re.sub(xticks_pattern, xticks_to_yticks, code)

    x_label_pattern = "xlabel"
    y_label_pattern = "ylabel"

    # change xlabel to zlabel first
    code = re.sub(x_label_pattern, "zlabel", code)
    code = re.sub(y_label_pattern, "xlabel", code)
    code = re.sub("zlabel", "ylabel", code)

    return re.sub(bar_pattern, ".barh(", code)

save_fig_pattern = r"plt\.savefig\("

def invert_xaxis(code):
    return re.sub(save_fig_pattern, "plt.gca().invert_xaxis()\n\nplt.savefig(", code)

def invert_yaxis(code):
    return re.sub(save_fig_pattern, "plt.gca().invert_yaxis()\n\nplt.savefig(", code)

save_fig_location_pattern = r"plt\.savefig\(\'[^']+\'\)"
save_fig_location_double_quote_pattern = r'plt\.savefig\(\"([^"]+)\"'

def update_savefig_location(code, loc):
    if re.search(save_fig_location_double_quote_pattern, code):
        return re.sub(save_fig_location_double_quote_pattern, f'plt.savefig("{loc}")', code)
    return re.sub(save_fig_location_pattern, f"plt.savefig('{loc}')", code)

def shuffle_data(data):
    """
    Shuffle the data in the code
    should be easy to spot
    """
    nums = re.findall(r'\d+', data)

    nums_deep_copy = [num for num in nums]

    random.shuffle(nums)

    mapping = {nums_deep_copy[i]: nums[i] for i in range(len(nums))}

    # replace the data
    for key, value in mapping.items():
        data = data.replace(key, value)

    return data

def random_replace(data):
    """
    Randomly replace the data with new numbers.
    should be difficult to spot
    """
    nums = re.findall(r'\d+', data)
    
    # randomly select numbers to replace
    replace = random.sample(nums, random.randint(1, len(nums)))
    
    # get len(replace) random numbers from min(nums) to max(nums)
    new_nums = [random.randint(min(nums), max(nums)) for _ in range(len(replace))]

    mapping = {replace[i]: new_nums[i] for i in range(len(replace))}

    # replace the data
    for key, value in mapping.items():
        data = data.replace(key, value)

    return data

def draw_easy_equivalent(grounded_code):
    """
        randomize color
    """
    if re.search(color_single_char_pattern, grounded_code):
        grounded_code = re.sub(color_single_char_pattern, lambda x: f"color='{randomize_color(x.group(1))}'", grounded_code)
        color_change = True
    elif re.search(color_hex_pattern, grounded_code):
        grounded_code = re.sub(color_hex_pattern, lambda x: f"color='{randomize_color(x.group(1))}'", grounded_code)
        color_change = True
    elif re.search(color_letters_pattern, grounded_code):
        grounded_code = re.sub(color_letters_pattern, lambda x: f"color='{randomize_color(x.group(1))}'", grounded_code)
        color_change = True
    elif re.search(color_rgb_pattern, grounded_code):
        grounded_code = re.sub(color_rgb_pattern, lambda x: f"color=({randomize_color(x.group(1))})", grounded_code)
        color_change = True

    """
        randomize rotation
    """
    if re.search(rotation_pattern, grounded_code):
        grounded_code = re.sub(rotation_pattern, lambda x: f"rotation={randomize_rotation(x.group(1))}", grounded_code)
        rotation_change = True

    """
        randomize inverting axes
    """
    if re.search(save_fig_pattern, grounded_code):
        grounded_code = invert_xaxis(grounded_code)
        is_axis_invertible = True

    
    return grounded_code
    

def bar_num_to_bar(code):
    # remove ax.text()
    code = re.sub(r"ax\.text\([^)]+\)", "", code)
    # remove ax.annotate()
    code = re.sub(r"ax\.annotate\([^)]+\)", "", code)

    return code
    

def draw_hard_equivalent():
    pass

def draw_easy_diff():
    pass

def draw_hard_diff():
    pass

for ii in data:
    grounded_code = ii["redrawing"]["output"]
    img_name = ii['imgname']
    c_type = ii['chart_type']


    """ if re.search(figsize_pattern, grounded_code):
        # grounded_code = re.sub(figsize_pattern, lambda x: f"figsize={randomize_figsize(x.group(1))}", grounded_code)
        figsize_change = True

    if re.search(bar_pattern, grounded_code):
        grounded_code = bar_to_barh(grounded_code)
        use_barh = True """

    easy_diff_dir_name = f"./{c_type}/easy_diff"

    if not os.path.exists(easy_diff_dir_name):
        os.makedirs(easy_diff_dir_name)

    save_loc = f"{easy_diff_dir_name}/{img_name}.png"

    # find the first occurence of data
    data = re.search(data_pattern, grounded_code)
    
    if not data:
        continue
    else:
        data = data.group(0)
    data_changed = shuffle_data(data)

    if data == data_changed:
        continue

    # replace the data
    grounded_code = grounded_code.replace(data, data_changed)


    grounded_code = update_savefig_location(grounded_code, save_loc)

    # remove plt.show()
    grounded_code = grounded_code.replace("plt.show()", "")

    try:
        exec(grounded_code)
    except:
        continue


