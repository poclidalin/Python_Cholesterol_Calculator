from process_data import process_cholesterol
from daily_average_level_calculator import daily_average_level_calculator

def interactive_cholesterol_input():
    # Start an infinite loop for user input.
    while True:
        user_input = input("Enter the individual's daily average cholesterol level (mg/dL), or type 'exit' to quit: ").strip().lower()
        
        # Exit condition if the user types 'exit'.
        if user_input == 'exit':
            print("Goodbye!")
            break
        
        try:
            # Try to convert the user input to a float.
            level = float(user_input)
            # Calculate the cholesterol level result.
            result = daily_average_level_calculator(level)
            # Debug print to see what result we got.
            print(f"DEBUG: Computed result: {result}")
            
            # If the result is HIGH LEVEL, provide additional advice.
            if result == "HIGH LEVEL":
                print(f"The cholesterol level result is: {result}. Book an appointment with your GP.")
            else:
                print(f"The cholesterol level result is: {result}")
        except ValueError:
            # Handle non-numeric inputs.
            print("Invalid input! Please enter a valid numerical cholesterol level or type 'exit' to quit.")
        
        # Ask if the user wants to continue; enforce valid 'yes' or 'no' responses.
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
    # Process the CSV data when the script is run.
    process_cholesterol()
    # Start the interactive input loop.
    interactive_cholesterol_input()
