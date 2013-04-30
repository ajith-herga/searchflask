import urllib2, json, pprint
from flask import render_template, Flask, request
import copy
import nltk

baseUrl = "http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?"
queryStringEnd = "&apikey=100e31514a617a41b95c792e60f097b80b2dcc2f&outputMode=json"
GoogleStringOrig = "https://www.googleapis.com/customsearch/v1?key=AIzaSyD-GRHebffj4YspNUw6Bqfnc1pK8O8xWuc&cx=013036536707430787589:_pqjad5hr1a&q="
attr_list = []
requirements = []
search_list = []

query_str_final = GoogleStringOrig + "phone%20display%20technology"
a = urllib2.urlopen(query_str_final)
b = json.load(a)
for items in b["items"]:
    print items["link"]
