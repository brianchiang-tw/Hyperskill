import requests
from bs4 import BeautifulSoup

idx_lang_dict = {   1: "Arabic",    \
                    2: "German",    \
                    3: "English",    \
                    4: "Spanish",    \
                    5: "French",    \
                    6: "Hebrew",    \
                    7: "Japanese",    \
                    8: "Dutch",    \
                    9: "Polish",    \
                    10: "Portuguese",    \
                    11: "Romanian",    \
                    12: "Russian",    \
                    13: "Turkish",    \
                 }


welcome_msg = "Hello, you're welcome to the translator.Translator supports:"

for idx in range(1, 14):
    print(f'{idx}. {idx_lang_dict[idx]}')

print(welcome_msg)

try:
    src_lang = int(input("Type the number of your language: "))
    dst_lang = int(input("Type the number of language you want to translate to:"))

    if (src_lang not in idx_lang_dict) or (dst_lang not in idx_lang_dict):
        raise KeyError("Error: Invalid language index. Index should be in range 1 ~ 13")

except Exception as err:

    print()
    print(err)
    exit()

word = input("Type the word you want to translate:")

# ----------------------------------------------------------------------

# generate HTTP query URL
url = "https://context.reverso.net/translation/" + idx_lang_dict[src_lang].lower() + "-" + idx_lang_dict[dst_lang].lower() + '/' + word

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.136 Safari/537.36'}

# HTTP connection with GET
response = requests.get(url, headers = headers)

if response:
    # Successful connection with status code = 200
    #print(str(response.status_code) + " OK")
    pass

else:

    print('Fail')
    print(response.status_code)

html_source_code = response.content

# Get HTML parser with BeautifulSoup
soup = BeautifulSoup(html_source_code, "lxml")



# --------------------------
# for translated word

translation = soup.select("a.translation.ltr.dict")

# a list for translated word
translation_list = []


for dest_lang_word in translation:
    # add translated word, with whitespace characters removal
    translation_list.append( dest_lang_word.text.strip() )

print()
print(f'{idx_lang_dict[dst_lang]} Translations:')

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


print(f'{idx_lang_dict[dst_lang]} Examples:')

# print first 5 example sentences
for pair_idx in range(5):
    print( sentence_list[2*pair_idx] + ":" )
    print( sentence_list[2*pair_idx+1] )

    if pair_idx != 4:
        # new line between each example sentence pair
        print()

