
tests = int(input())
results = []
for i in range(tests):
    triplets = list(map(int, input().split(" ")))
    triplets.sort()
    if triplets[0] + triplets[1] == triplets[2]:
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result)
    