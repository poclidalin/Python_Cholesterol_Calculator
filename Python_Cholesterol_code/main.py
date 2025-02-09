from process_data import process_cholesterol
from daily_average_level_calculator import daily_average_level_calculator

def interactive_cholesterol_input():
    # Start an infinite loop for user input.
    while True:
        user_input = input("Enter the individual's daily average cholesterol level (mg/dL), or type 'exit' to quit: ").strip().lower()
        
        # Exit if the user types exit.
        if user_input == 'exit':
            print("Goodbye!")
            break
        
        try:
            # Convert the user input to a float.
            level = float(user_input)
            # Calculate the cholesterol level result.
            result = daily_average_level_calculator(level)
            # Debug print to see what result we got.
            print(f"DEBUG: Computed result: {result}")
            
            # If the result is HIGH LEVEL, give additional message.
            if result == "HIGH LEVEL":
                print(f"The cholesterol level result is: {result}. Book an appointment with your GP.")
            else:
                print(f"The cholesterol level result is: {result}")
        except ValueError:
            # Handle non-numeric inputs.
            print("Invalid input! Please enter a valid numerical cholesterol level or type 'exit' to quit.")
        
        # Ask the user if he want to continue.
        while True:
            continue_input = input("Do you want to enter another value? (yes/no): ").strip().lower()
            if continue_input in ('yes', 'no'):
                break
            else:
                print("Invalid input. Please answer with 'yes' or 'no'.")
        
        if continue_input != 'yes':
            print("Goodbye!")
            break

if __name__ == '__main__':
    # Process the CSV data.
    process_cholesterol()
    # Start the interactive input.
    interactive_cholesterol_input()
