def budgetShopping(n, bundleQuantities, bundleCosts):
    opt = [0]*(n+1)
    l = len(bundleQuantities)
    for i in range(1, n+1):
        for j in range(l):
            if i >= bundleCosts[j]:
                opt[i] = max(opt[i], opt[i-bundleCosts[j]] + bundleQuantities[j])
    return opt[n]

n=4
bq = [10, 1]
bc = [2, 20]
budgetShopping(n, bq, bc)



from sklearn.base import BaseEstimator, TransformerMixin

class EmojiExtractor(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass

    def get_emoji(self, tweet):
    	return ''.join(x for x in tweet if x in emoji.UNICODE_EMOJI)

    def transform(self, df, y=None):
        return df['text'].apply(self.get_emoji)

    def fit(self, df, y=None):
        return self

from sklearn.pipeline import Pipeline, FeatureUnion

pipeline = Pipeline([
    ('features', FeatureUnion([
        ('tfidf', TfidfVectorizer(min_df=1, max_df=0.9, ngram_range=(1, 4), strip_accents='unicode', norm='l2')), # can pass in either a pipeline
        ('emoji', EmojiExtractor()) # or a transformer
    ])),
    ('clf', tree.DecisionTreeClassifier(criterion="entropy"))  # classifier
])


from sklearn.base import BaseEstimator, TransformerMixin

class TextSelector(BaseEstimator, TransformerMixin):
    def __init__(self, key):
        self.key = key

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.key]

text = Pipeline([
                ('selector', TextSelector(key='text')),
                ('emoji', EmojiExtractor( stop_words='english'))
            ])

emoji_feats = EmojiExtractor()
tfidf = TfidfVectorizer()
feats = FeatureUnion([('emoji', emoji_feats), ('tfidf', tfidf)])



def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text

def strip_mentions(text):
    entity_prefixes = ['@']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)

def strip_hashtags(text):
    entity_prefixes = ['#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)

def strip_all_entities(text):
    entity_prefixes = ['@','#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)

def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def remove_stopwords(text, is_lower_case=False):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text

def simple_stemmer(text):
    ps = nltk.porter.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text


def lemmatize_text(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text

text_pipeline = [strip_links, strip_mentions, strip_hashtags, strip_all_entities, remove_special_characters, remove_stopwords, lemmatize_text]