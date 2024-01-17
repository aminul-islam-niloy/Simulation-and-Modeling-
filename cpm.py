import numpy as np

class Activity:
    
    def __init__(self, idx, activity, duration) -> None:
        self.idx = idx
        self.activity = activity
        self.duration = duration
        self.predecessor = []
        self.successor = []
        self.early_start = 0
        self.early_finish = 0
        self.late_start = 0
        self.late_finish = 0
        self.slack = 0

file_path = "./input2.txt"

activities = {}
index = []

for lines in open(file_path):
    words = lines.rstrip('\n').split(',')
    idx = int(words[0])
    activity = words[1]
    duration = int(words[2])
    predecessors = words[3]
    index.append(idx)
    activities[idx] = Activity(idx, activity, duration)
    
    if predecessors:
        predecessors = predecessors.split(';')
        for item in predecessors:
            item = int(item)
            activities[idx].predecessor.append(item)
            activities[item].successor.append(idx)

maxEF = 0

# Forward pass (early start and early finish)
for idx in index:
    if not activities[idx].predecessor:
        activities[idx].early_finish = activities[idx].duration
    else:
        maxTime = 0
        for item in activities[idx].predecessor:
            maxTime = max(maxTime, activities[item].early_finish)

        activities[idx].early_start = maxTime
        activities[idx].early_finish = maxTime + activities[idx].duration

    maxEF = max(maxEF, activities[idx].early_finish)

# Backward pass (late start and late finish)
for i in range(len(index)):
    idx = index[len(index) - i - 1]
    if not activities[idx].successor:
        activities[idx].late_finish = maxEF
        activities[idx].late_start = maxEF - activities[idx].duration
    else:
        minTime = float("inf")
        for item in activities[idx].successor:
            minTime = min(minTime, activities[item].late_start)

        activities[idx].late_finish = minTime
        activities[idx].late_start = minTime - activities[idx].duration

# Calculate slack and identify critical tasks
for idx in index:
    activities[idx].slack = activities[idx].late_start - activities[idx].early_start
    activities[idx].is_critical = activities[idx].slack == 0

# Find the critical path
result = [activities[idx].activity for idx in index if activities[idx].is_critical]

# Print the critical path
for i in range(len(result) - 1):
    print(result[i] + " -> ", end="")
print(result[len(result) - 1])
