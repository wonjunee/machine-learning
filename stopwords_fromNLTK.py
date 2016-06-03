### Download nltk
import nltk
nltk.download()

### Getting Stopwords from NLTK
from nltk.corpus import stopwords
sw = stopwords.words("english")

print len(sw)