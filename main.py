# -*- coding: utf-8 -*-

from gtts import gTTS
from google.cloud import translate_v2 as translate
import html

def text_to_mp3(text): 
    tts = gTTS(text=text, lang='en', slow=False) 
    filename='voice.mp3' 
    tts.save(f"mp3/{filename}") 

def translator(text):
    client = translate.Client()
    result = client.translate(text, target_language='en')
    translated_text = result['translatedText']
    result_text = html.unescape(translated_text)
    print(result_text)

    return result_text

origin_text = "현대차-BTS, 환경의 날 맞아 '수소 에너지' 알린다"
text = translator(origin_text)
text_to_mp3(text)

