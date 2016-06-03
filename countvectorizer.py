### Bag of words

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
string1 = "hi Katie the self driving car will be late Best Sebastian"
string2 = "Hi Sebastian the machine learning class will be great great great Best Katie"
string3 = "Hi Katie the machine learning class will be most excellent"
email_list = [string1, string2, string3]

bag_of_words = vectorizer.fit(email_list)
print bag_of_words
bag_of_words = vectorizer.transform(email_list)
print bag_of_words
print vectorizer.vocabulary_.get("great")