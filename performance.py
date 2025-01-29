import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Replace with your actual data
actual_values = np.array([440, 445, 450, 455, 460, 465, 470, 475, 480, 485])
predicted_values = np.array([438, 443, 452, 454, 459, 467, 469, 476, 478, 486])

# Calculate RMSE
rmse_value = np.sqrt(mean_squared_error(actual_values, predicted_values))
print(f"Root Mean Squared Error (RMSE): {rmse_value}")

# Calculate MAE
mae_value = mean_absolute_error(actual_values, predicted_values)
print(f"Mean Absolute Error (MAE): {mae_value}")

# Confidence Intervals (assuming 95% confidence, 1.96 multiplier for normal distribution)
std_error = np.std(actual_values - predicted_values)
ci_upper = predicted_values + 1.96 * std_error
ci_lower = predicted_values - 1.96 * std_error

print(f"Confidence Interval Upper Bound: {ci_upper}")
print(f"Confidence Interval Lower Bound: {ci_lower}")
