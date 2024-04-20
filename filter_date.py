import re
from datetime import datetime

# Function to check if the date is after June 2022
def is_after_june_2022(date_str):
    date_format = "%Y-%m-%d"
    date = datetime.strptime(date_str, date_format)
    return date > datetime(2022, 6, 30)

# Reading the input file and writing to a new file
with open('all_text.txt', 'r', encoding='utf-8') as infile, \
     open('filtered_output.txt', 'w', encoding='utf-8') as outfile:

    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}_UTC')
    current_caption = []
    include_current_caption = False

    for line in infile:
        if date_pattern.search(line):
            if current_caption and include_current_caption:
                outfile.writelines(current_caption)
                outfile.write("\n")  # Optional: Add extra line for separation

            current_caption = [line]  # Start a new caption
            date_str = line.split('_')[0].split(' ')[-1]  # Extracting the date part
            include_current_caption = is_after_june_2022(date_str)
        else:
            current_caption.append(line)  # Accumulate lines for the current caption

    # Write the last caption if it meets the date criteria
    if current_caption and include_current_caption:
        outfile.writelines(current_caption)
