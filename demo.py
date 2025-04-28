name = input('Enter file: ')
try:
    handle = open(name, 'r')
except FileNotFoundError:
    print('File cannot be opened:', name)
    quit()

counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigCount = None
bigWord = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
