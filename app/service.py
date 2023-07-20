import numpy as np
from PIL import Image
from wordcloud import WordCloud
from nltk.corpus import stopwords
import requests
import pandas as pd


def tokenize(data):
  comment_words = ''
  for val in data:
    val = str(val)
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens)+" "
  return comment_words

def gen_world_cloud(comment_words):
    stopWords = stopwords.words('portuguese')
    stopWords.extend(['nan'])
    wordcloud = Image.new('RGB', (1900, 1080), color = (255,255,255))
    if len(comment_words) > 0:
        pic = np.array(Image.open(requests.get('https://images.emojiterra.com/twitter/v14.0/512px/1f535.png',stream=True).raw))
        wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopWords, mask = pic,
                min_font_size = 10).generate(comment_words)
    return wordcloud

def gen_general_world_cloud(data_file):
    sheet_names = data_file.sheet_names
    frames = []
    for r in sheet_names:
        frame = pd.read_excel(data_file, sheet_name=r)
        frames.append(frame)
    
    dataframe = pd.concat(frames)
    comment_words = tokenize(dataframe[dataframe.columns[0]])
    wordCloud = gen_world_cloud(comment_words)
    return wordCloud
  
def gen_total_world_cloud(data_esquerda, data_direita):
    sheet_names = data_esquerda.sheet_names
    frames = []
    for r in sheet_names:
        frame = pd.read_excel(data_esquerda, sheet_name=r)
        frames.append(frame)
    
    sheet_names = data_direita.sheet_names
    for i in sheet_names:
        frame = pd.read_excel(data_direita, sheet_name=i)
        frames.append(frame)
          
    dataframe = pd.concat(frames)
    comment_words = tokenize(dataframe[dataframe.columns[0]])
    wordCloud = gen_world_cloud(comment_words)
    return wordCloud