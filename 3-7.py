with open('sample.txt', 'r') as f:
    line = f.readline()
    print(line)

with open('sample.txt', 'r') as f:
    line = f.readlines()
print(lines)

with open ('sample.txt','w') as f:
    f.write('test')


