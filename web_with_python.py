# import urllib.request
# import urllib.parse
# import webbrowser
# import re

# NOT WORKING FOR GOOGLE
# url = 'https://www.google.com/search'
# values = {'q': 'python programming tutorial'}
#
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
#
# headers = {'user-Agent': 'Chrome'}
#
# rqst = urllib.request.Request(url, data, headers = headers)
# resp = urllib.request.urlopen(rqst)
# respData = resp.read()
#
# print(respData)

# values = {'q': 'tony stark'}
# data = urllib.parse.urlencode(values)
#
# url = 'https://www.google.com/search?'+data
#
# headers = {}
# headers['user-Agent'] = 'Google Chrome'
#
# rqst = urllib.request.Request(url, headers = headers)
# resp = urllib.request.urlopen(rqst)

# url = 'https://www.pythonprogramming.net/search/?'
# values = {'q': 'car'}
#
# data = urllib.parse.urlencode(values)
#
# url += data
#
# rqst = urllib.request.Request(url)
#
# resp = urllib.request.urlopen(rqst)
#
# with open('D:/Documents/temp.html', 'w') as temp:
#     temp.write(str(resp.read()))
# webbrowser.open('D:/Documents/temp.html')
#
# url = 'https://www.google.com/search?'
# values = {'q': 'python tutorial'}
# headers = {'user-Agent': 'Google chrome'}
#
# data = urllib.parse.urlencode(values)
#
# url += data
#
# rqst = urllib.request.Request(url, headers = headers)
#
# resp = urllib.request.urlopen(rqst)
# respData = str(resp.read())
#
# # hyperlinks = re.findall(r'<a .*?>.*?</a>', respData)
# # for i in hyperlinks:
# #     print(i)
#
# paragraphs = re.findall(r'www.*?[.]com', respData)
# for i in paragraphs:
#     print(i)
#
# import requests
#
# url = 'https://www.google.com/images/branding/googleg/1x/googleg_standard_color_128dp.png'
#
# data = requests.get(url)
#
# print(data.status_code)
# print(data.ok) # return True for any status code less than 400, else False
# print(data.headers)
#
# # with open('D:/Documents/temp.png', 'wb') as temp:
# #     temp.write(data.content)
# # webbrowser.open('D:/Documents/temp.html')
#
#
# # http status code :
# #     200 for success
# #     300 for redirect
# #     400 for client side error
# #     500 fro server side error
#
# import requests
#
# url = 'https://httpbin.org/get'
# values = {'page': 2,'count': 25}
#
# data = requests.get(url, params = values)
#
# print(data.text)
#
# import requests
#
# url = 'https://httpbin.org/post'
# values = {'username': 'subho', 'password': 'raspberry@3'}
#
# data = requests.post(url, params = values)
#
# print(data.text)
# print(data.json()) # create python dictionary from json data
#
# import requests
#
# url = 'https://httpbin.org/basic-auth/subho/raspberry'
# auth = ('subho', 'raspberry')
#
# data = requests.get(url, auth = auth)
#
# print(data.status_code)
# print(data.ok)
# print(data.content)
# print(data.text)
# print(data.json())
#
# import requests
#
# url = 'https://httpbin.org/delay/5'
#
# data = requests.get(url, timeout = 10)
#
# print(data.status_code)
# print(data.ok)
# print(data.content)
# print(data.text)
# print(data.json())