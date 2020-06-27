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

# HTTP connection with GET
response = requests.get(url, headers = headers)

if response:
    # Successful connection with status code = 200
    print(str(response.status_code) + " OK")

else:

    print('Fail')
    print(response.status_code)

html_source_code = response.content

soup = BeautifulSoup(html_source_code, "lxml")



# --------------------------
# for translated word

translation = soup.select("a.translation.ltr.dict")

# a list for translated word
translation_list = []


for dest_lang_word in translation:
    # add translated word, with whitespace characters removal
    translation_list.append( dest_lang_word.text.strip() )

str_context_eg = """
Context examples:
"""
print(str_context_eg)


if 'fr' == dst_lang:
    print('French Translations:')

elif 'en' == dst_lang:
    print('English Translations:')


# print first 5 translated words
for idx in range(5):
    print( translation_list[idx] )

# one new line after translated word section
print()



# --------------------------
# for example sentence


example_sentence = soup.select("#examples-content span.text")

# "Translation" is demanded by online judge
sentence_list = []

for sentence in example_sentence:
    # add sentence, with whitespace characters removal
    sentence_list.append(sentence.text.strip())


if 'fr' == dst_lang:
    print('French Examples:')

elif 'en' == dst_lang:
    print('English Examples:')


# print first 5 example sentences
for pair_idx in range(5):
    print( sentence_list[2*pair_idx] )
    print( sentence_list[2*pair_idx+1] )

    if pair_idx != 4:
        # new line between each example sentence pair
        print()
