import csv
from daily_average_level_calculator import daily_average_level_calculator
from utils import calculate_average

def process_cholesterol():
    persons = []
    try:
        with open('cholesterol.csv', 'r') as file:
            reader = csv.reader(file)
            # If your CSV has a header, uncomment the following line to skip it:
            # next(reader, None)
            for row in reader:
                # Skip empty rows.
                if not row:
                    continue
                # Expecting: name, morning, afternoon, evening.
                name, morning, afternoon, evening = row
                try:
                    morning_level = float(morning)
                    afternoon_level = float(afternoon)
                    evening_level = float(evening)
                except ValueError:
                    # If any of the values cannot be converted, skip this row.
                    print(f"Invalid data for {name}. Skipping row.")
                    continue

                # Calculate the average cholesterol level.
                avg_level = calculate_average([morning_level, afternoon_level, evening_level])
                # Determine the result using the calculator function.
                result = daily_average_level_calculator(avg_level)

                # Add extra advice if the level is HIGH.
                if result == "HIGH LEVEL":
                    result += ". Book an appointment with your GP."

                # Append the processed data.
                persons.append([name, avg_level, result])
    except FileNotFoundError:
        # Handle the case where the CSV file does not exist.
        print("Error: 'cholesterol.csv' not found.")
        return

    with open('daily_cholesterol_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write header row for clarity.
        writer.writerow(["Name", "Average Cholesterol Level (mg/dL)", "Result"])
        writer.writerows(persons)
    print("Results saved to 'daily_cholesterol_results.csv'")
