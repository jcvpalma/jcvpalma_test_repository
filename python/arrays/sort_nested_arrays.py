vetor = [
    [1,2],
    [8,4],
    [5,9,7]
]

result = []

for v in vetor:
    if isinstance(v, list) == True:
        for x in v:
            result.append(x)
    else:
        result.append(v)

result.sort()

for w in result:
    print(w)
