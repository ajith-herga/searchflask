import urllib2, json, pprint
from flask import render_template, Flask, request
import copy
import nltk

baseUrl = "http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?"
queryStringEnd = "&apikey=100e31514a617a41b95c792e60f097b80b2dcc2f&outputMode=json"
GoogleStringOrig = "https://www.googleapis.com/customsearch/v1?key=AIzaSyD-GRHebffj4YspNUw6Bqfnc1pK8O8xWuc&cx=013036536707430787589:_pqjad5hr1a&q="
synonymBase = "http://words.bighugelabs.com/api/2/7975c2c8cdd9ce63a094b67f99a39be7/"
queryStringOrig = "https://www.googleapis.com/shopping/search/v1/public/products?key=AIzaSyD-GRHebffj4YspNUw6Bqfnc1pK8O8xWuc&country=US&q=phone"



def do_google_custom_search_for(query_str):
	search_list = []	
	#This does the query search assuming that this is in the phone domain.

	google_query_URL = GoogleStringOrig + "phone%20" + query_str + "%20technology"
	a = urllib2.urlopen(google_query_URL)
	b = json.load(a)
	for items in b["items"]:
	    search_list.append(items["link"])

	return search_list  

def do_google_product_search_for(query_str):
	search_list = []
	
	google_product_query_URL = queryStringOrig + query_str
	a = urllib2.urlopen(google_product_query_URL)
	b = json.load(a)
	#print b
	if b["totalItems"] == 0:
		return []
		
	for items in b["items"]:
		if items["product"]:
			search_list.append((items["product"]["title"], items["product"]["link"]))

	return search_list
