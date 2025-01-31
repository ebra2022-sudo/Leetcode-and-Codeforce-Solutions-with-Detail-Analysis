tests = int(input())
assert(tests in range(1,10001))
number_of_differences = []
for i in range(tests):
    word = input()
    assert(len(word)==10)
    count = 0
    for i in range(10):
        if "codeforces"[i] != word[i]:
            count += 1
    number_of_differences.append(count)

for i in number_of_differences:
    print



