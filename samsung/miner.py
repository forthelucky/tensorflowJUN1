from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import re

class Samsung:
    def __init__(self):
        pass

    @staticmethod
    def read_file():
        okt = Okt()
        okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        # stem = true 어간만 추출, 즉 아버지의 > 아버지만 추출
        filename = 'data/kr-Report_2018.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            texts = f.read()
        return texts

    @staticmethod
    def extract_hangeul(texts):
        temp = texts.replace('\n', ' ') #줄바꿈을 없앤다.
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        #^ start의 의미이다. ㄱ부터, 힣까지 라는 의미. 한글만.
        temp = tokenizer.sub('', temp)
        #한글 빼고 나머지를 다 지우라.
        return temp

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize()
        print(tokens[:7])