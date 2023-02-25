import requests
from lxml import etree

doi = "10.2196/40201" # Replace with the DOI of the research article you want to get the abstract for
url = f"http://api.crossref.org/works/{doi}"
response = requests.get(url)
data = response.json().get("message").get("abstract")
data = data.replace('jats:', '')

root = etree.HTML(data)
for i in range(len(root[0])):
    for j in root[0][i]:
        print(j.text)
