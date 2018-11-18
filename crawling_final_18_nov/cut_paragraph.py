file = open('crawl_it_output.txt','r',encoding='utf8')
out = open('cut_paragraph_output.txt','w',encoding='utf8')
file = file.read().split('\n')



for lines in file:
    thisLine = lines.split(' ')
    flag = 0
    # print(thisLine)
    # print('\n')

    for word in thisLine:
        # print(word, end='*')

        if len(word) < 1:
            continue
        if(word == "<p><img" or word == "<p><iframe" or word == "</p><p><img" or word == "<br/><img" and flag == 0):
            # print('paise')
            # print('\n')
            flag = 1

        if(flag == 1):
            str = ''
            for alp in word:
                str += alp
                if(str == "width="):
                    flag = 0
                    break

        if(flag == 0):
            out.write(word)
            out.write(" ")
    out.write('\n')
