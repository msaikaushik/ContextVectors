import string
import re
import pprint

def sort_dict_by_value(d, reverse = False):
    return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

def getFeatures(text1, text2, n):

    # remove punctuation from the texts
    processedText1 = text1.translate(str.maketrans('', '', string.punctuation))
    processedText2 = text2.translate(str.maketrans('', '', string.punctuation))

    #clean strings
    pat = re.compile(r'[^a-zA-Z ]+')
    processedText1 = re.sub(pat, '', processedText1).lower()
    processedText2 = re.sub(pat, '', processedText2).lower()

    tokens = set();
    # dict for keeping track of occurrences. to be used later in ranking.
    hashFrequency = {}
    hashTokenRanking = {}
    hashRankingToken = {}
    nbTokensInText1 = 0

    splitText1 = processedText1.split(' ');
    for word in splitText1:
        tokens.add(word)
        if word in hashFrequency:
            hashFrequency[word] = hashFrequency[word] + 1
        else:
            hashFrequency[word] = 1

    nbTokensInText1 = len(tokens)

    # for adding missing words which are present in text 2 in cvectors of text 1. add word in token list
    splitText2 = processedText2.split(' ');
    for word in splitText2:
        tokens.add(word)
        if word not in hashFrequency:
            hashFrequency[word] = 0
    
    i = 1
    # sort hash frequency
    sortedHashFreq = sort_dict_by_value(hashFrequency, True)

    for token in sortedHashFreq:
        hashTokenRanking[token] = i
        hashRankingToken[i] = token
        i = i + 1


    #create context vectors
    after = {}
    before = {}

    # print(hashFrequency)
    # print(hashTokenRanking)
    # print(tokens)

    for index, word in enumerate(splitText1):
        # word = splitText1[index]
        targetWordIndex = hashTokenRanking[word]


        # iterate from 1 to n (inclusive)
        for position in range(1, n+1):

            # for after
            if (index + position < len(splitText1)):
                contextWord = splitText1[index + position]
                contextWordIndex = hashTokenRanking[contextWord]

                if (targetWordIndex in after):
                    positionDict = after[targetWordIndex]
                    if (position in positionDict):
                        relFreqAtPositionJ = after[targetWordIndex][position]
                        relFreqAtPositionJ[contextWordIndex - 1] = relFreqAtPositionJ[contextWordIndex - 1] + 1
                    else:
                        #create an array
                        relFreqAtPositionJ = [0] * len(tokens)
                        relFreqAtPositionJ[contextWordIndex - 1] = 1
                        positionDict[position] = relFreqAtPositionJ

                else:
                    relFreqAtPositionJ = [0] * len(tokens)
                    relFreqAtPositionJ[contextWordIndex - 1] = 1

                    positionDict = {}
                    positionDict[position] = relFreqAtPositionJ

                    after[targetWordIndex] = positionDict

            # for before
            if (index - position >= 0):
                contextWord = splitText1[index - position]
                contextWordIndex = hashTokenRanking[contextWord]

                if (targetWordIndex in before):
                    positionDict = before[targetWordIndex]
                    if (position in positionDict):
                        relFreqAtPositionJ = before[targetWordIndex][position]
                        relFreqAtPositionJ[contextWordIndex - 1] = relFreqAtPositionJ[contextWordIndex - 1] + 1
                    else:
                        #create an array
                        relFreqAtPositionJ = [0] * len(tokens)
                        relFreqAtPositionJ[contextWordIndex - 1] = 1
                        positionDict[position] = relFreqAtPositionJ

                else:
                    relFreqAtPositionJ = [0] * len(tokens)
                    relFreqAtPositionJ[contextWordIndex - 1] = 1

                    positionDict = {}
                    positionDict[position] = relFreqAtPositionJ

                    before[targetWordIndex] = positionDict


    # print(after)
    # print(before)

    # process before and after for missing position vectors


    contextVectorHash = {}
    # combine after and before for each vector (flatten it)
    # context vectors of all the words - this will also have info like its occurance in the corpus, so dont worry abt this
    # ranked acc to freq occurance
    for rank in hashTokenRanking.values():
        contextVectorHash[rank] = []

        # start adding freq from before
        # n to 1 in before (so negative)
        for negativePos in range(n, 0, -1):
            # print(negativePos)
            if (rank not in before):
                contextVectorHash[rank] += [0] * len(tokens)
            else:
                if (negativePos not in before[rank]):
                    contextVectorHash[rank] += [0] * len(tokens)
                else:        
                    contextVectorHash[rank] += before[rank][negativePos]

        for positivePos in range(1, n+1):
            if (rank not in after):
                contextVectorHash[rank] += [0] * len(tokens)
            else:
                if (positivePos not in after[rank]):
                    contextVectorHash[rank] += [0] * len(tokens)
                else:    
                    contextVectorHash[rank] += after[rank][positivePos]

    for rank in hashTokenRanking.values():
        arrVector = contextVectorHash[rank]
        # contextVectorHash[rank] = npArrVector / nbTokensInText1
        contextVectorHash[rank] = [x / 10 for x in arrVector]

    # print(contextVectorHash)
    # return getObservations(contextVectorHash, contextVectorHash)
    return contextVectorHash