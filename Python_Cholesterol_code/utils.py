def calculate_average(values):
    # Return 0 if the list is empty.
    if not values:
        return 0
    return sum(values) / len(values)
