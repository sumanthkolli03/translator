import codecs, os
from time import strftime
from datetime import datetime
from html import unescape
from charset_normalizer import from_bytes, from_path
from google.cloud import translate_v2 as translate
from sys import argv

#setting up API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'api.json'
translate_client = translate.Client()


#translation
script, target = argv
file = str(from_path(target, True).best())
result = translate_client.translate(file, target_language="eng", format_ = "text")
translatedText = unescape(result["translatedText"])

print(u"Text: {}".format(result["input"]))
print(u"Translation: {}".format(translatedText))
print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))


#write to file
time = datetime.now().strftime("%m%d%Y %H-%M-%S")
with codecs.open(f"translated {time}.txt","w", encoding="utf-8") as file:
    file.write(translatedText)