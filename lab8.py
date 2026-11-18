import sys

# Accept number of scores
n = int(sys.argv[1])

scores = []

# Accept scores
score = sys.argv[2].split(",")

for i in range(n):
    scores.append(float(score[i]))

# Calculate sum
total = 0

for score in scores:
    total = total + score

# Calculate average
average = total / n

# Find maximum and minimum
maximum = scores[0]
minimum = scores[0]

for score in scores:
    if score > maximum:
        maximum = score

    if score < minimum:
        minimum = score

# Display results
print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
print("Maximum Score:", maximum)
print("Minimum Score:", minimum)