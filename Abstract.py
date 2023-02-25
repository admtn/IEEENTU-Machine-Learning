import requests
from lxml import etree


doi = "10.4183/aeb.2022.301" # Replace with the DOI of the research article you want to get the abstract for
'''
url = f"http://api.crossref.org/works/{doi}"
PMID = '36699165'
format = 'json'
encoding = 'unicode'
url2 = f'https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pubmed.cgi/BioC_{format}/{PMID}/{encoding}'
response = requests.get(url)
data = response.json()
data = response.json().get("message")
'''

def getArticleDetails(doi):
    url = f"http://api.crossref.org/works/{doi}"
    response = requests.get(url)
    message = response.json().get("message")
    author = message.get("author")
    name = author[0].get('given') + '. ' + author[0].get('family')
    title = message.get('title')[0]
    abstract = message.get("abstract")

    data_dict = {
        'author_name' : name,
        'title' : title,
    }
    return data_dict

data = getArticleDetails(doi)

#print(data['title'])

'''
root = etree.HTML(data)
for i in range(len(root[0])):
    for j in root[0][i]:
        print(j.text)'''
