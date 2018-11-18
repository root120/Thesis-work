rootfile = open('root.txt','r',encoding='utf8')
stopfile = open('stop.txt','r',encoding='utf8')
mainfile = open('all_bangla_output.txt','r',encoding='utf8')
cleanData = open('clean_data.txt','w',encoding='utf8')

rootfile = rootfile.read().split('\n')
stopfile = stopfile.read().split('\n')
mainfile = mainfile.read().split('\n')


root={}
for x in rootfile:
    v = x.split(' ')
    if(len(v)!=2):
        continue
    a,b=v[0],v[1]
    if a not in root:
        root[a] = b

stop = []
for x in stopfile:
    if x not in stop:
        stop.append(x)


def cutStop(line):
    global stop
    global root
    line = line.split(' ')
    myLine = ''
    for word in line:
        if(len(word)>0):
            if word not in stop:
                myLine += word
                myLine += ' '
    return myLine


def toRoot(line):
    global root
    line = line.split(' ')
    myline = ''
    for word in line:
        if len(word) < 1:
            continue
        if word in root:
            word = root[word]
        myline += word + ' '
    return cutStop(myline)


for eachLine in mainfile:
    thisLine = cutStop(eachLine)
    thisLine = toRoot(thisLine)
    cleanData.write(thisLine)
    if len(thisLine) > 1:
        cleanData.write('\n')
