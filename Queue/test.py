import sentiment_analysis as s

example_sentense = "The movie is okay" 

sentiment = s.analyze_sentence(example_sentense)

#print the sentiment
print(sentiment)

# print the sentiment score
print(sentiment.score)
