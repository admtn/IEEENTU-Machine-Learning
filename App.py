import TextExtractor
import Summariser

str = TextExtractor.getText('TBI.pdf')
for i in range(4):
    str = Summariser.summarise(str)

print(str)
