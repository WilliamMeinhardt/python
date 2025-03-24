def calculate_statistics(numbers):
    if not numbers:
        raise ValueError("Listen kan ikke være tom.")
    
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return {"sum": total, "average": average, "max": maximum, "min": minimum}

# Eksempelbruk
numbers = [5, 260, 67, 7, 0.1]
result = calculate_statistics(numbers)

print("Sum:", result["sum"])
print("Gjennomsnitt:", result["average"])
print("Største verdi:", result["max"])
print("Minste verdi:", result["min"])
