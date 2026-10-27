scores = [45, 70, 85, 30, 90, 55]


total = 0
for score in scores:
    total += score

average = total / len(scores)

# Calculate passing and failing scores
passing = 0
failing = 0

for score in scores:
    if score >= 40:
        passing += 1
    else:
        failing += 1


print("Scores:", scores)
print("Total:", total)
print("Average:", average)
print("Number of passing scores:", passing)
print("Number of failing scores:", failing)