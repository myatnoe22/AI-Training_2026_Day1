for i in range(5):
    print(i)
total=-0
scores = [70, 85, 60, 90, 45]
for score in scores:
    total += score
average = total / len(scores)
print("Score:", score)
print("Total:", total)
print("Average:", average)