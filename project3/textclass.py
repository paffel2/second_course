import re
class Text(object):
    def __init__(self,text):
        self.text = text
    
    def findWords(self):
        wordsList = re.split('[:!\n .,]+',self.text)
        vovels = "уеыаоэясиюё"
        result = []
        for word in wordsList:
            temp = word.lower()
            if len(temp) == 0:
                continue
            elif temp[-1] in vovels:
                result.append(word)
        return result
