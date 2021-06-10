from PyDictionary import PyDictionary
dictionary=PyDictionary()

res = []

with open('random-text.txt','r') as file:
    punctuations = ["!","(",")","-","[","]","{","}","'",";",":","\",","<",">",".","/","?","@","#","$","%","^","&","*","_","~"]
    uninteresting_words = ['The', 'A', 'To', 'If', 'Is', 'It', 'Of', 'And', 'Or', 'An', 'As', 'I', 'Me', 'My', 'We', 'Our', 'Ours', 'You', 'Your', 'Yours', 'He', 'She', 'Him', 'His', 'Her', 'Hers', 'Its', 'They', 'Them', 'Their', 'What', 'Which', 'Who', 'Whom', 'This', 'That', 'Am', 'Are', 'Was', 'Were', 'Be', 'Been', 'Being', 'Have', 'Has', 'Had', 'Do', 'Does', 'Did', 'But', 'At', 'By', 'With', 'From', 'Here', 'When', 'Where', 'How', 'All', 'Any', 'Both', 'Each', 'Few', 'More', 'Some', 'Such', 'No', 'Nor', 'Too', 'Very', 'Can', 'Will', 'Just']

    glossary={} 
    for line in file:        
        for word in line.split():
            no_punct=""
            word=word.capitalize()
            for char in word:
                if char.isalpha():
                    if char not in punctuations:
                        no_punct=no_punct+char
            if no_punct not in uninteresting_words:
                if no_punct in glossary.keys():
                    glossary[no_punct]+=1
                elif no_punct not in glossary:
                    glossary[no_punct]=1
            no_punct="" 

    avg = 0
    for j in glossary.values():
        avg = avg + j
    avg= avg/len(glossary)

    for i,j in glossary.items():
        if j > avg:
            res.append(i)
        

for i in res:
    print("{} : {}".format(i,dictionary.meaning(i)))
