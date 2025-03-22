import csv

# Task 2: CSV File Processing
def process_csv_file(csv_file):
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            data = list(reader)

            # Display structured format
            print("\nStructured Data from CSV:")
            print(f"{header[0]:<10} {header[1]:<10} {header[2]:<10}")
            print("-" * 30)
            for row in data:
                print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10}")

            # Filter rows where age > 25
            print("\nFiltered Data (Age > 25):")
            print(f"{header[0]:<10} {header[1]:<10} {header[2]:<10}")
            print("-" * 30)
            for row in data:
                if int(row[2]) > 25:
                    print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10}")

    except FileNotFoundError:
        print(f"Error: '{csv_file}' not found.")
    except ValueError:
        print("Error: Incorrect data format in CSV.")

# Example Usage
process_csv_file("data.csv")