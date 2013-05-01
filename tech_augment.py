import urllib2, json, pprint
from flask import render_template, Flask, request
import copy
import nltk
import test_radio

feature_dict = {"display" : ["Retina", "AMOLED", "SuperLCD"], "data": ["4G","LTE","HSDPA", "3G"], "wireless" : ["802.11N"], "pairing" : ["NFC"], "camera" : ["Carl%20Zeiss", "Auto%20focus"]}
#queryStringOrig = "https://www.googleapis.com/shopping/search/v1/public/products?key=AIzaSyD-GRHebffj4YspNUw6Bqfnc1pK8O8xWuc&country=US&q=phone"
baseUrl = "http://api.remix.bestbuy.com/v1/products%28search=phone"
queryStringEnd = "%29?show=all&apiKey=kbakn9s69mz3ddgf5yyn5ffc&format=json"
search_result = []
disp_res = 0
#/*User preference*/
requirements = [0,0,0,0,0,0]
#Attribute to index mapping
attr_list = ['display', 'data', 'wireless', 'pairing', 'camera']
#

#1. AMOLED
amoled = "&details.name=AMOLED%20SCREEN%7CshortDescription=AMOLED*%7Cfeatures.feature=AMOLED*"
#2. Retina 
retina = "&features.feature=Retina*"
#3. Super LCD
superlcd = "&features.feature=Super%20LCD*%7CshortDescription=Super%20LCD*"


#1. LTE
lte = "&details.value=LTE*"
#2. HSDPA
hsdpa = "&details.value=HSDPA*"
#3. 4G
Fgr = '&details.value=4G*'
#4. 3G
Tgr = '&details.value=3G*'

#1. 802.11n
E02n = '&features.feature=802.11*n*'

#1. NFC
nfc = '&features.feature=NFC*%7Cdetails.value=NFC*%7CshortDescription=NFC*'

#1. Carl Ziess
car_zei = '&features.feature=Carl*'
#2. AutoFocus
autofocus = '&features.feature=auto*focus*'

#Order according to the better technology.
search_list = [[retina, amoled, superlcd], [Fgr, lte, hsdpa, Tgr], [E02n], [nfc], [car_zei, autofocus]]


def constructQuery (query_str, depth):
   global requirements
   global feature_list
   global search_result
   if (depth == len(feature_list)):
       query_str_final = query_str + queryStringEnd
       print "\n" + query_str + queryStringEnd + "\n"
       a = urllib2.urlopen(query_str_final)
       b = json.load(a)
       if b["total"] > 0:
           print "\n********************************\n"
           print b["total"]
           prod_list = b["products"]
           
           for product in prod_list:
               search_result.append((product['name'], product['url']))
       return
              
   if (requirements[depth] == 0):
       constructQuery(query_str, depth + 1)
       return
   for feature in search_list[depth]:
       str1 = query_str +  feature
       constructQuery(str1, depth+1) 

def search_text(text):
    global disp_res
    global search_result
    for i in range(0, len(requirements)):
        requirements[i] = 0

    tokens = nltk.word_tokenize(text)
    pos_tag = nltk.pos_tag(tokens)
    # Assuming that the reuest is phone, look for other NNs, could
    #have to make a 2 level list for other known devices, or create
    #a dynamic list for phone itself later, easily modifiable for
    #those cases.
    print pos_tag
    for attr,val in pos_tag:
        if val == 'NN':
            if attr in attr_list:
                requirements[attr_list.index(attr)] = 1
    print requirements
    search_result = []
    constructQuery(baseUrl, 0)

def init_data_on_call():
    global search_result
    global disp_res
    disp_res = 0

def content_for_next_page():
    global search_result
    global disp_res
    len_look = len(search_result)
    if (disp_res + 20 <= len_look):
        buf = search_result[disp_res:disp_res+20]
        disp_res = disp_res + 20
    elif (disp_res == len_look):
        buf = []
        buf.append(('Done', 'previous.html'));
        return buf
    else:
        buf = search_result[disp_res:len_look]
        disp_res = len_look
    return buf

def content_for_prev_page():
    global search_result
    global disp_res
    len_look = len(search_result)
    if disp_res == 0:
        buf = []
        buf.append(('Done', 'next.html'));
        return buf
    if (disp_res - 20 <= 0):
        #First page, should ideally be only = 0
        buf = search_result[0:disp_res]
        disp_res = 0
    else:
        # Will never have to display the last page with prev
        disp_res = disp_res - 20
        buf = search_result[disp_res:disp_res + 20]
    return buf

