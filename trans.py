import os
from googletrans import Translator
from bs4 import BeautifulSoup

translator = Translator()
path = './temp'
new_path = './temp/hindu'

if not os.path.exists(new_path):
    os.makedirs(new_path)

files = os.listdir(path)

def trans(file):
    new_file = f'hindu_{file}'
    en_list = []
    hi_list = []
    #try:
    if not file.startswith('hindu'):
        with open(f'{path}/{file}', "r", encoding="utf8") as f:
            file = f.read()
            soup = BeautifulSoup(file, "html.parser")
            text = soup.get_text().strip()
            lines = text.splitlines()
            for line in lines:
                stripped_line = line.strip()
                if stripped_line != '':
                    print(line)
                    try:
                        if_integer = int(stripped_line[1:-1])
                        print(f'Integer {stripped_line} detected')
                    except:
                        try:
                            out = translator.translate(line, dest='hi')
                            translation = out.text
                            print(translation)
                    
                        except Exception as err:
                            print(err)
                            pass
                        else:
                            if stripped_line == 'Google':
                                translation = 'गूगल'
                            elif stripped_line == 'Follow':
                                translation = 'अनुसरण करना'
                            elif stripped_line == 'Showing':
                                translation = 'दिखा'
                            elif stripped_line == 'Privacy Policy':
                                translation = 'गोपनीयता नीति'
                            elif stripped_line == 'by Class Central':
                                translation = 'द्वारा Class Central'

                            hi_list.append(out.text)
                            en_list.append(line)

                            #for i, eng in enumerate(en_list):
                            #print(i, eng)
                            for tag in soup.find_all(text=lambda t: t.strip() == stripped_line):
                                print(f'Found {stripped_line}, replacing with {translation}')
                                if stripped_line != translation.strip():
                                    tag.replace_with(translation)

                            # Write the file.
                            with open(f'{new_path}/{new_file}', "wb") as file:
                                file.write(soup.prettify("utf-8"))
                                print('file written')

        print(f'Eng List: {len(en_list)}, Hindu List: {len(hi_list)}')
        #except:

for file in files:
    if file.endswith('.html'):
        print(file)
        try:
            trans(file)
        except Exception as e:
            print(e)
