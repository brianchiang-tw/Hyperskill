import requests


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
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
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

import sys, os

# write your code here

if len(sys.argv) == 2:
    directory_name = sys.argv[1]

    path = ".\\" + directory_name

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

        if history:

            if history[-1] == "bloomberg":
                content = bloomberg_com

            elif history[-1] == "nytimes":
                content = nytimes_com

            print(content)

    elif url.count('.') != 0 and url in ("bloomberg.com", "nytimes.com"):

        tokens = url.split('.')
        response = None
        if url == "bloomberg.com":
            #print(bloomberg_com)
            response = requests.get("https://"+url)
            #content = bloomberg_com
            content = response.text


        elif url == "nytimes.com":
            #print(nytimes_com)
            response = requests.get("https://"+url)
            #content = nytimes_com
            content = response.text

        print(content)

        # add current website into browser history
        web_name = tokens[0]
        #history.add( web_name )
        history.append( web_name )


        with open(path + "/" + web_name, 'w') as f:
            f.write(content)

    elif url in history:

        web_name = url
        with open(path + "/" + web_name, 'r') as f:
            content = f.read()
            print( content )

    else:
        print('Error: Incorrect URL')
