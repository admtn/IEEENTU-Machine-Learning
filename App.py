import TextExtractor
import Summariser
import InfographicGenerator
import getDetails
import getAbstract

doi = "10.2196/40201"
url = f"http://api.crossref.org/works/{doi}"
data_dict = getDetails.getArticleDetails(doi)
str = getAbstract.abst(url)
#str = TextExtractor.getText('covid.pdf')
for i in range(1):
    str = Summariser.summarise(str)

print(str)
data_dict['summary'] = str
InfographicGenerator.generateInfographic(data_dict)
