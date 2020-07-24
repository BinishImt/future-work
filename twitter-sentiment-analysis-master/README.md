# twitter-sentiment-analysis
Twitter Sentiment Analysis

Sentiment Analysis is a technique widely used in text mining. Twitter Sentiment Analysis, therefore means, using advanced text mining techniques to analyze the sentiment of the text (here, tweet) in the form of positive, negative, and neutral.

Programming tools: Python, NLTK, TextBlob, Keras, sklearn, Numpy, pandas, Matplotlib.

Environment: Google Colab on Tesla K80 GPU

Dataset: Twitter data download from (https://www.kaggle.com/kazanova/sentiment140/kernels)

Aim: The program should be able to classify tweets as Positive or Negative.


Results: 
predict("you are so Intelligent")
{'elapsed_time': 0.23145675659179688,
 'label': 'POSITIVE',
 'score': 0.9715249538421631}

predict("you are so dumb")
{'elapsed_time': 0.23145675659179688,
 'label': 'POSITIVE',
 'score': 0.9715249538421631}


Steps: 
Download the data from the above-provided link.
Use NLP techniques to preprocess the data. 
Make sure that the target variable is balanced.
Load word2vec pre-trained model from the gensim NLP library.
Create a vocabulary of similar words. (word embedding).
Encode all the target categories.
Train the word2vec model using LSTM neural network.
Predict on unseen test tweets.
Accuracy: 78%


Real-time usage: 
Brand Improvement
Domain-specific trend tracking
Customer segmentation
Determining the most effective twitter handlers.
