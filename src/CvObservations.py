from scipy import spatial
import numpy as np

def getObservations(contextVectors1, contextVectors2):

    similarityMatrix = np.zeros((len(contextVectors1) + 1, len(contextVectors2) + 1))
    # observations = pd.DataFrame()
    observations = []


    # key ranking should be same from global rank list containing all the words
    for tokenRank1 in contextVectors1.keys():
        for tokenRank2 in contextVectors2.keys():
            # print(1-spatial.distance.cosine(contextVectors1[tokenRank1], contextVectors2[tokenRank2]))
            similarityMatrix[tokenRank1][tokenRank2] = 1 - spatial.distance.cosine(contextVectors1[tokenRank1], contextVectors2[tokenRank2])

    # print(similarityMatrix.max())

    observations.append(similarityMatrix.min()) #["minimum"]
    observations.append(similarityMatrix.max()) #["maximum"]
    observations.append(np.median(similarityMatrix)) #["median"]
    observations.append(similarityMatrix.mean()) #["mean"] 
    observations.append(similarityMatrix.std()) #["std"]

    observations.append(np.quantile(similarityMatrix, 0.25)) #["25% quantile"]
    observations.append(np.quantile(similarityMatrix, 0.50)) #["50% quantile"]
    observations.append(np.quantile(similarityMatrix, 0.75)) #["75% quantile"] 

    # observations.to_csv("observations_cv.csv")

    # return observations
    print(observations)
