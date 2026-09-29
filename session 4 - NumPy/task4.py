import numpy as np

google_pay = np.array([True, True, False, False, True])
phonepe = np.array ([False, True, False, True, False])

result = np.logical_or(google_pay, phonepe)

print("Google Pay:", google_pay)
print("Phonepe:", phonepe)
print("Paid by either app or both:", result)