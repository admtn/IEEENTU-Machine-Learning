import TextExtractor
import Summariser
import InfographicGenerator
import Abstract

doi = "10.4183/aeb.2022.301"
data_dict = Abstract.getArticleDetails(doi)

str = TextExtractor.getText('TBI.pdf')
for i in range(4):
    str = Summariser.summarise(str)

print(str)

data_dict['summary'] = str
InfographicGenerator.generateInfographic(data_dict)
