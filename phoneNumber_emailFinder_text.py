#This program uses web scraping and pattern matching with regex's to find
#phone numebrs and email addresses on a given webpage and return them.

import requests, re

def findNumbers(URL):
    page = requests.get(URL)
    content = page.text
    phoneNumRegex1 = re.compile(r'\d{3}-\d{3}-\d{4}')
    matchobject1 = phoneNumRegex1.findall(content)
    if not matchobject1:
        print("No phone number found")
    else:
        for i in matchobject1:
            print("Phone number found: " + i)

    phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
    matchobject2 = phoneNumRegex2.findall(content)
    for i in matchobject2:
        print("Phone number found: ", i[0], i[1])

def findEmails(URL):
    page = requests.get(URL)
    content = page.text
    emailRegex = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9.]+",re.VERBOSE)
    matchObject1 = emailRegex.findall(content)
    if not matchObject1:
        print("No emails found.")
    else:
        for i in matchObject1:
            print("Email Found: ", i)
    


Website = input("Enter URL of web page you'd like to search for phone numebrs and email addresses: ")
try:
    findNumbers(Website)
    findEmails(Website)
except:
    print("You have not entered a URL or the URL does not exist")



