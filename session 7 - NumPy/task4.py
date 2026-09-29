import numpy as np

messages = np.array([
    [10, 12, 15, 8, 9, 11, 10],
    [2, 3, 1, 2, 1, 3, 2],
    [15, 18, 12, 20, 17, 16, 14]
])

print("Original Messages:")
print(messages)


# Remove the user who sent the fewest messages
total_messages = np.sum(messages, axis=1)
least_user = np.argmin(total_messages)

messages = np.delete(messages, least_user, axis=0)

print("After Removing Least Active User:")
print(messages)


# Add a new user
new_user = np.array([[5, 6, 7, 8, 9, 10, 11]])

messages = np.insert(messages, len(messages), new_user, axis=0)

print("After Adding New User:")
print(messages)