import TextExtractor
import Summariser
import InfographicGenerator
import getDetails

doi = "10.4183/aeb.2022.301"
data_dict = getDetails.getArticleDetails(doi)
str = TextExtractor.getText('Carbonated.pdf')
for i in range(3):
    str = Summariser.summarise(str)

print(str)
data_dict['summary'] = str
InfographicGenerator.generateInfographic(data_dict)
