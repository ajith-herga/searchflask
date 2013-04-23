import urllib2
import json
import copy

feature_list = [["Retina", "AMOLED", "SuperLCD"], ["4G","LTE","HSDPA", "3G"], ["802.11N"], ["NFC"], ["Carl%20Zeiss", "Auto%20focus"]]
#queryStringOrig = "https://www.googleapis.com/shopping/search/v1/public/products?key=AIzaSyD-GRHebffj4YspNUw6Bqfnc1pK8O8xWuc&country=US&q=phone"
queryStringOrig = "http://api.remix.bestbuy.com/v1/products%28search=phone"
queryStringEnd = "%29?show=all&apiKey=kbakn9s69mz3ddgf5yyn5ffc"
#/*User preference*/
requirements = [1,0,0,0,0,0]


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
   if (depth == len(feature_list)):
       print "\n" + " ********************************************************************" + query_str + queryStringEnd + "\n"
       return
       a = (urllib2.urlopen(query_str).read())
       b = json.loads(a)
       if b["totalItems"] > 0:
           #print "\n********************************\n"
           c = len(b["items"])
           for i in range(0, c):  
               print (str(i+1) + ". "+ b["items"][i]["product"]["title"]+"\n")
               bbquery = "http://api.remix.bestbuy.com/v1/products(search=" +  b["items"][i]["product"]["title"] + ")?apiKey=kbakn9s69mz3ddgf5yyn5ffc"
               print bbquery + "\n"
               try:
                   c =  (urllib2.urlopen(bbquery).read())
                   d = json.loads(c)
                   if len(d["products"]) > 0:
                       print d[0][name] + "#############################################################################3"       
               except urllib2.HTTPError:
                   print "Not found at best buy" 
       return
              
   if (requirements[depth] == 0):
       constructQuery(query_str, depth + 1)
       return
   for feature in search_list[depth]:
       str1 = query_str +  feature
       constructQuery(str1, depth+1) 

constructQuery(queryStringOrig, 0) 
#queryString1 = ""
#queryString2 = ""
#queryString3 = ""
#queryString4 = ""
#j=0
#for feature in feature_list:
#   if (requirements[j] == 0) :
#       j+=1
#       continue
#   for keyword in feature:
#   
#   queryString1 = copy.copy(queryStringOrig)
#   queryString1 += str1+"+"
#   for str2 in data :
#       queryString2 = copy.copy(queryString1)
#       queryString2 += str2+"+"
#       for str3 in wifi:
#           queryString3 = copy.copy(queryString2)
#           queryString3 += str3
#           #print queryString3 + "\n****************************\n"
#           for str4 in sound:
#              queryString4 = copy.copy(queryString3)
#              queryString4 += str4
#               
#              a = (urllib2.urlopen(queryString3).read())
#              b = json.loads(a)
#              if b["totalItems"] > 0:
#                  #print "\n********************************\n"
#                  c = len(b["items"])
#                  for i in range(0, c):  
#                      print (str(j+i+1) + ". "+ b["items"][i]["product"]["title"]+"\n")
#                  j+=i+1 
#
#
#
 #
 #
 #
 #
 #


