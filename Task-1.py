import csv

#Task 1: Read & Write to a File
def process_text_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            line_count = len(lines)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(f"Number of lines: {line_count}\n")
            file.write(f"Number of words: {word_count}\n")

        print(f"Processed '{input_file}' successfully. Results saved in '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")



process_text_file("input.txt", "output.txt")