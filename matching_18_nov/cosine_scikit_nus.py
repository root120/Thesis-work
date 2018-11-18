#import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


file = open('tf_idf_input.txt','r',encoding='utf8')
querys = open('80Games.txt','r',encoding='utf8')
final_result = open('final_result.txt','w',encoding='utf8')
file = file.read().split('\n')
querys = querys.read().split('\n')
file = file[:-1]


def isRoadAccidentMatched(val):
    listOfRoadAccident = [2, 4, 5, 6, 7, 8, 9, 13, 17, 19, 21]
    if val in listOfRoadAccident:
        return True
    else:
        return False


def CosineSimiWorks(tmp,queryId):
    myvec = TfidfVectorizer(tokenizer=lambda x:x.split())
    myvec_mat = myvec.fit_transform(tmp)
    #print(myvec.get_feature_names())
    cosine = cosine_similarity(myvec_mat[queryId], myvec_mat)
    #print('Cosine: ',cosine, ' ',type(cosine))
    return cosine


def getMaxSimiId(cosineMat,queryID):
    mx=-9999999999.5
    mxSimiId=0
    for i in range(0,len(cosineMat[0])):
        if cosineMat[0][i] > mx and i != queryId:
            mx = cosineMat[0][i]
            mxSimiId = i


    return mxSimiId


#queryId = 14

#tmp = open('tmp.txt', 'w', encoding='utf8')


for news in querys:
    if len(news) < 1:
        continue

    file.append(news)
    queryId = 23
    cosineMat = CosineSimiWorks(file, queryId)
    #print('15: ',file[15])
    #print(cosineMat)
    final_result.write(news)
    final_result.write('\n')
    #print(cosineMat)
    mxId = getMaxSimiId(cosineMat, queryId)
    if isRoadAccidentMatched(mxId):
        final_result.write("Road Accident")
    else:
        final_result.write("Not Road Accident")
    final_result.write('\n')
    file.remove(file[queryId])




