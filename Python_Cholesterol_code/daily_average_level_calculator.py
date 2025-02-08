def daily_average_level_calculator(avg_level):
    # Categorize the cholesterol level based on the average.
    if avg_level >= 200:
        return "HIGH LEVEL"
    elif avg_level < 120:
        return "LOW LEVEL"
    else:
        return "NORMAL LEVEL"
