from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentiments = SentimentIntensityAnalyzer()
from deepface import DeepFace

def check(comment):
    sentiment_dict = sentiments.polarity_scores(comment)
    #print(sentiment_dict['compound'])
    if sentiment_dict['compound'] >= 0.05 :
        return ("Positive")
    elif sentiment_dict['compound'] <= - 0.05 :
        return ("Negative")
    else :
        return ("Neutral")

def checkimg(filename):
    obj = DeepFace.analyze(img_path = filename, actions = ['emotion'])
    return obj['dominant_emotion']

# comm = input("Enter Your Comments")
# print(check(comm))