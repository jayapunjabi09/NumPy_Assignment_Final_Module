import numpy as np

post1 = np.array([100, 200, 300, 400, 500, 600, 700])
post2 = np.array([150, 250, 350, 450, 550, 650, 750])
post3 = np.array([200, 300, 400, 500, 600, 700, 800])

stacked_likes = np.vstack((post1, post2, post3))

print("Stacked Likes:")
print(stacked_likes)