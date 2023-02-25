import requests
from lxml import etree

doi = "10.4183/aeb.2022.301" # Replace with the DOI of the research article you want to get the abstract for
url = f"http://api.crossref.org/works/{doi}"
PMID = '36699165'
format = 'json'
encoding = 'unicode'
url2 = f'https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pubmed.cgi/BioC_{format}/{PMID}/{encoding}'
response = requests.get(url2)
data = response.json()
message = data['documents'][0]['passages'][1]['text']
print(message)
#data = response.json().get("message").get("abstract")
#data = data.replace('jats:', '')

'''
root = etree.HTML(data)
for i in range(len(root[0])):
    for j in root[0][i]:
        print(j.text)'''
