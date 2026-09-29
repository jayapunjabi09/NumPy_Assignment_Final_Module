import numpy as np

likes = np.array([200, 250, 150, 300, 350, 450, 500])
comments = np.array([10, 15, 20, 30, 45, 50, 40])

engagement = likes + comments
average = engagement / 7

print("Likes:", likes)
print("Comments:", comments)
print("Engagement per post:", engagement)
print("average engagement:", average)
