import numpy as np

teams = np.array([
    "CSK", "MI", "RCB", "CSK",
    "GT", "MI", "KKR", "RCB"])

unique_teams = np.unique(teams)

print("Unique IPL Teams:", unique_teams)