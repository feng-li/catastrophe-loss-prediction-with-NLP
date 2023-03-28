data['Token'] = 0
for i in range(data.shape[0]):
    data['Token'][i] = word_tokenize(data['Text_clean'][i])

# Load keyword phrase database
f1 = open("keywords.txt").read()
f2 = f1.replace("\n"," ")
keywords = f2.split();

data['Keywords_str'] = 0
for i in range(data.shape[0]):
    data['Keywords_str'][i] = str([str(word) for word in data['Token'][i] if word in keywords])
    
# Obtain the word frequency matrix of keywords
corpus = data['Keywords_str']
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
wc_data = pd.DataFrame(X.toarray())
wc_data.columns = vectorizer.get_feature_names()

# Output word vectors
sentences = []
for i in range(len(data)):
    sentences.append(eval(data.Keywords_str[i]))

vector_size = 128
model_w2v = word2vec.Word2Vec(sentences, vector_size = vector_size, seed = 123, workers = 1)
model_w2v.save('model_w2v_128.bin')

# Output weighted word vectors
x_self = np.zeros((len(data), vector_size))
for i in range(len(data)):
    e = eval(data.Keywords_str[i])
    line_count = wc_data.apply (lambda x: x.sum (), axis=1)[i]
    for j in range(len(e)):
        x_self[i,] +=  model_w2v.wv[e[j]]
    x_self[i,] = x_self[i,] / line_count
    
np.savetxt('word2vec_vec.csv', x_self, delimiter=",")
