r1 = r'<(.*?)>'
text = re.sub(r1, "", data['Text'][0])

x_bert = np.zeros((len(data), 768))
bc = BertClient(ip='localhost',check_version=False, check_length=False)
for i in range(len(data)):
    text = re.sub(r1, "", data['Text'][i])
    x_bert[i, ] = bc.encode([text])
    
np.savetxt('bert_vec.csv', x_bert, delimiter=",")
