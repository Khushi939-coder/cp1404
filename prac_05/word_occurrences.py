text = "this is a collection of words of nice words this is a fun thing it is"

print(f"Text: {text}")

lists = text.split()

counts = {}
for word in lists:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

max_length = max(len(word) for word in counts)

for word in sorted(counts):
    print(f"{word:<{max_length}} : {counts[word]}")




