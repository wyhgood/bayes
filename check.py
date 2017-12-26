f = open('model2.txt', 'r') 
lines = f.readlines()

s = set()
f2 = open('to_0.5','r')
for line in f2.readlines():
    s.add(line.strip())

for line in lines:
    if len(line.split(':')) !=2:
        print(line)
        continue
    if line.split(':')[0] in s:
        print(line.split(':')[0]+":"+str(0.5))
        continue
    score = line.split(':')[1]
    if float(score) > 0.6 and float(score) < 0.75: 
        print(line.split(':')[0]+":"+str(0.5))
    elif float(score) >= 0.75 and float(score) < 0.85:
        print(line.split(':')[0]+":"+str(float(score)-0.1))
    else:
        print(line.strip())
