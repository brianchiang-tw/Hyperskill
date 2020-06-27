import requests
from bs4 import BeautifulSoup

print('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
dst_lang = input()
print('Type the word you want to translate:')
word = input()
print(f'You chose "{dst_lang}" as the language to translate "{word}" to.')



url_en_to_fr = "https://context.reverso.net/translation/english-french/"
url_fr_to_en = "https://context.reverso.net/translation/french-english/"
url = None

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.136 Safari/537.36'}



if 'fr' == dst_lang:
    url = url_en_to_fr + word

elif 'en' == dst_lang:
    url = url_fr_to_en + word

else:
    print('Error')
    exit()

response = requests.get(url, headers = headers)
if response:
    #print('Success')
    #print(response.text)
    print(str(response.status_code) + " OK")

else:
    print('Fail')
    print(response.status_code)

html_source_code = response.content

soup = BeautifulSoup(html_source_code, "lxml")



# --------------------------
# for translated word
#translation = soup.select("a.translation.ltr.dict em.translation")
#translation = soup.select("a.translation.ltr.dict em.translation")
#translation = soup.select("a.translation.ltr.dict em")

translation = soup.select("a.translation.ltr.dict")

translation_list = ['Translation']
#print( "find" + str(len(translation)) + "elements")

for dest_lang_word in translation:
    #print(dest_lang_word.text)
    translation_list.append( dest_lang_word.text.strip() )

print(translation_list)

# --------------------------
# for example sentence


example_sentence = soup.select("#examples-content span.text")
sentence_list = ['Translation']
for sentence in example_sentence:

    sentence_list.append(sentence.text.strip())
    #print( sentence.text )

print(sentence_list)

#words = soup.select(".example .trg .text em")

#for word in words:
#    print(word)
