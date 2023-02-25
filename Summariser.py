import spacy
import TextExtractor
from spacy.lang.en.stop_words import STOP_WORDS
stopwords=list(STOP_WORDS)
from string import punctuation
punctuation=punctuation+ '\n'

#text="The human coronavirus was first diagnosed in 1965 by Tyrrell and Bynoe from the respiratory tract sample of an adult with a common cold cultured on human embryonic trachea.1 Naming the virus is based on its crown-like appearance on its surface.2 Coronaviruses (CoVs) are a large family of viruses belonging to the Nidovirales order, which includes Coronaviridae, Arteriviridae, and Roniviridae families.3 Coronavirus contains an RNA genome and belongs to the Coronaviridae family.4 This virus is further subdivided into four groups, ie, the α, β, γ, and δ coronaviruses.5 α- and β-coronavirus can infect mammals, while γ- and δ- coronavirus tend to infect birds.6 Coronavirus in humans causes a range of disorders, from mild respiratory tract infections, such as the common cold to lethal infections, such as the severe acute respiratory syndrome (SARS), Middle East respiratory syndrome (MERS) and Coronavirus disease 2019 (COVID-19). The coronavirus first appeared in the form of severe acute respiratory syndrome coronavirus (SARS-CoV) in Guangdong province, China, in 20027 followed by Middle East respiratory syndrome coronavirus (MERS-CoV) isolated from the sputum of a 60-year-old man who presented symptoms of acute pneumonia and subsequent renal failure in Saudi Arabia in 2012.8 In December 2019, a β-coronavirus was discovered in Wuhan, China. The World Health Organization (WHO) has named the new disease as Coronavirus disease 2019 (COVID-19), and Coronavirus Study Group (CSG) of the International Committee has named it as SARS-CoV-2.9,10 Based on the results of sequencing and evolutionary analysis of the viral genome, bats appear to be responsible for transmitting the virus to humans"
text = TextExtractor.getText('TBI.pdf')
#print(text)
nlp = spacy.load('en_core_web_sm')
doc= nlp(text)
tokens=[token.text for token in doc]
#print(tokens)
word_frequencies={}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
#print("_______________________________________________________________________________________________")
#print(word_frequencies)
max_frequency=max(word_frequencies.values())
for word in word_frequencies.keys():
    word_frequencies[word]=word_frequencies[word]/max_frequency
#print("_______________________________________________________________________________________________")
#print(word_frequencies)
sentence_tokens= [sent for sent in doc.sents]
#print("_______________________________________________________________________________________________")
#print(sentence_tokens)
sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():                            
             sentence_scores[sent]=word_frequencies[word.text.lower()]
            else:
             sentence_scores[sent]+=word_frequencies[word.text.lower()]
#print("_______________________________________________________________________________________________")
#print(sentence_scores)
from heapq import nlargest
select_length=int(len(sentence_tokens)*0.3)

summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)

final_summary=[word.text for word in summary]

summary=''.join(final_summary)
print(summary)
