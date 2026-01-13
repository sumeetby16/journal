import sys

if len(sys.argv) < 2:
    print("Usage: python array_scores.py <score1> <score2> <score3> ...")
    sys.exit()

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Scores:", scores)
print("Sum =", total)
print("Average =", average)
print("Maximum =", maximum)
print("Minimum =", minimum)
