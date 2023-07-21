#! python3
#program to search and extract emails and phone numbers
import re, pyperclip

phone_number = re.compile(r'''((\d{3}|\(\d{3}\))?        #area code
                              (\s|-|\.)?               #separator
                              (\d{3})                  #first three digits
                              (\s|-|\.)
                              (\d{4})
                              (\s*(ext|x|ext.)\s*(\d{2,5}))?
                              )''', re.VERBOSE)
email = re.compile(r'''([a-zA-Z0-9_%+-]+
                       @
                       [a-zA-Z0-9.-]+
                       (\.[a-zA-Z]{2,4})
                       )''',re.VERBOSE)


text = str(pyperclip.paste())
matches =[]
for group in phone_number.findall(text):
    print(group[0])
    phone_num = '-'.join([group[1],group[3],group[5]])
    if group[8] != '':
        phone_num = ' x' +group[8]
    matches.append(phone_num)
for j in email.findall(text):
    matches.append(j[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print(matches)
    print('\n'.join(matches))
else:
    print('No phone number or emails were found')


