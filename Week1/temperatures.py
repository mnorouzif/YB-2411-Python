#     Tasks:
# Print the average temperature for a week.
# Find the highest and lowest temperature recorded.
# Convert all temperatures to Fahrenheit and print the result.
# (Formula: F = C * 9/5 + 32)
# Identify the days (by index) where the temperature was above 20°C.
 
# Help syntax: 
 
import numpy as np
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])


# 1. Print the average temperature for the week
average_temp = np.mean(temperatures)
print(f"Average temperature: {average_temp:.2f}°C")

# 2. Find the highest and lowest temperature recorded
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
print(f"Highest temperature: {max_temp}°C")
print(f"Lowest temperature: {min_temp}°C")

# 3. Convert all temperatures to Fahrenheit
fahrenheit = temperatures * 9/5 + 32
print("Temperatures in Fahrenheit:", fahrenheit)

# 4. Identify the days (by index) where the temperature was above 20°C
above_20_indices = np.where(temperatures > 20)
print("Days with temperature above 20°C (0=Mon, 6=Sun):", above_20_indices[0])
