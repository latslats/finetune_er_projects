def remove_empty_lines(original_file, cleaned_file):
    with open(original_file, 'r') as file:
        with open(cleaned_file, 'w') as new_file:
            for line in file:
                # Check if line is not empty
                if line.strip():
                    new_file.write(line)

# Usage
original_file = './finetune.jsonl'
cleaned_file = './cleanedtune.jsonl'
remove_empty_lines(original_file, cleaned_file)
