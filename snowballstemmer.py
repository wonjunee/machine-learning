### Getting Snowball Stemmer from nltk
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

### This finds the stem of each word
print stemmer.stem("responsiveness")
print stemmer.stem("responsivity")
print stemmer.stem("unresponsive")
