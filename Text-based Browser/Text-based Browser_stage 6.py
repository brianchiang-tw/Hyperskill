import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created ¡§soft¡¨ magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker¡¦s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

import sys, os

# write your code here

if len(sys.argv) == 2:
    directory_name = sys.argv[1]

    path = ".\\" + directory_name

    if not os.path.isdir(path):
        os.mkdir(path)
else:

    path = ".\\" + "tb_tabs"

    if not os.path.isdir(path):
        os.mkdir(path)


# record of browser history
history = []

choice = -1
while choice != 0:

    url = input()
    content = None

    if url == "exit":
        choice = 0

    elif url == "back":
        history.pop()
        web_name = None

        if history:

            web_name = history[-1]

            with open(path + "/" + web_name, 'r', encoding="utf_8") as f:
                parsed_content = f.read()
                print( parsed_content )

    #elif url.count('.') != 0 and url in ("bloomberg.com", "nytimes.com"):
    elif url.count('.') != 0:

        try:

            tokens = url.split('.')
            response = None

            if not url.startswith("https"):
                # check https:// prefix
                url = "https://" + url

            response = requests.get(url)

            content = response.text

            soup = BeautifulSoup(content, 'html.parser')
            valid_tags = ["p","a","ul","al","li","h1","h2","h3","h4","h5","h6"]

            parsed_content = []
            for tag in soup.find_all(valid_tags):

                if tag.name == 'a':
                    print(Fore.BLUE + tag.text)
                    parsed_content.append(Fore.BLUE + tag.text)
                else:
                    print(Fore.WHITE + tag.text)
                    parsed_content.append(Fore.WHITE + tag.text)

            # add current website into browser history
            web_name = '.'.join(tokens[:-1])
            #history.add( web_name )
            history.append( web_name )


            with open(path + "/" + web_name, 'w', encoding="utf_8") as f:
                #f.write(content)
                f.write('\n'.join(parsed_content))


        except Exception as e:
            print('Error: Incorrect URL')


    elif url in history:

        web_name = url
        with open(path + "/" + web_name, 'r', encoding="utf_8") as f:
            parsed_content = f.read()
            print( parsed_content )

    else:
        print('Error: Incorrect URL')
