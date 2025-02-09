import csv
from daily_average_level_calculator import daily_average_level_calculator
from utils import calculate_average

def process_cholesterol():
    persons = []
    try:
        with open('cholesterol.csv', 'r') as file:
            # Use DictReader to automatically handle the header row.
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Retrieve values using the header names.
                    name = row["Patients"]
                    morning_level = float(row["Morning"])
                    afternoon_level = float(row["Afternoon"])
                    evening_level = float(row["Evening"])
                except (ValueError, KeyError):
                    print(f"Invalid data for {row.get('Patients', 'Unknown')}. Skipping row.")
                    continue

                # Calculate the average cholesterol level.
                avg_level = calculate_average([morning_level, afternoon_level, evening_level])
                # Determine the result.
                result = daily_average_level_calculator(avg_level)

                #Extra advice if the level is HIGH.
                if result == "HIGH LEVEL":
                    result += ". Book an appointment with your GP."

                # Append the processed data.
                persons.append([name, avg_level, result])
    except FileNotFoundError:
        print("Error: 'cholesterol.csv' not found.")
        return

    with open('daily_cholesterol_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write header row.
        writer.writerow(["Name", "Average Cholesterol Level (mg/dL)", "Result"])
        writer.writerows(persons)
    print("Results saved to 'daily_cholesterol_results.csv'")
