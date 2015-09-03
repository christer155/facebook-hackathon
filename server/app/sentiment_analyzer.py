# todo
import csv
import pickle
from legacyAnalyzer import getFeatureVector,getStopWordList,processTweet, extract_features
import legacyAnalyzer

inpTweets = csv.reader(open('../data/full_training_dataset.csv', 'rb'), delimiter=',', quotechar='"')
stopWords = getStopWordList('../data/feature_list/stopwords.txt')
legacyAnalyzer.featureList = []
for row in inpTweets:
    sentiment = row[0]
    trainingTweet = row[1]
    processedTweet = processTweet(trainingTweet)
    featureVector = getFeatureVector(processedTweet, stopWords)
    legacyAnalyzer.featureList.extend(featureVector)
# Remove featureList duplicates
featureList = list(set(legacyAnalyzer.featureList))
    
def classifyTweet(tweet):

#     # Generate the training set
#     training_set = nltk.classify.util.apply_features(extract_features, tweets)
#      
#     # Train the Naive Bayes classifier
#     NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
#      
#     clFile = open("classifier", "wb")
#     pickle.dump(NBClassifier, clFile)
#     clFile.close()
 
    clFile = open("../data/naivebayes_trained_model.pickle", "r")
    NBClassifier = pickle.load(clFile)
    clFile.close()
    
    # Test the classifier
    # processedTweet = processTweet(tweet)
    # vec = getFeatureVector(processedTweet, stopWords)
    sentiment = NBClassifier.classify(extract_features(tweet))
#     print "tweet = %s, sentiment = %s\n" % (tweet, sentiment)
    return sentiment
    
clToScore = {"positive": 1, "neutral": 0, "negative": -1}
    
def classifyTweets(tweets):
    
    score = 0
    for tweet in tweets:
        classification = classifyTweet(tweet)
#         print classification
        score += clToScore[classification]
    return score
        
print classifyTweets([["great", "food"], ["very", "noisy"], ["worst", "food"]])