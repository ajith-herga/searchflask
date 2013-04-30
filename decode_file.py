import urllib2, json, pprint
from flask import render_template, Flask, request
import copy
import nltk
import pickle

baseUrlKey = "http://access.alchemyapi.com/calls/url/URLGetRankedKeywords?"
baseUrlEnt = "http://access.alchemyapi.com/calls/url/URLGetRankedNamedEntities?"
queryStringEnd = "&apikey=100e31514a617a41b95c792e60f097b80b2dcc2f&sentiment=1&outputMode=json"
attr_list = []
requirements = []
search_list = []
rank_list = []


def keyword_extract():
    for get in getter:
        query_alch_final = baseUrlKey + "&url=" + get.strip() + queryStringEnd
        a = urllib2.urlopen(query_alch_final)
        b = json.load(a)
        for senti in b["keywords"]:
            if senti["sentiment"]["type"] == "positive":
                rank_list.append((senti["text"], senti["relevance"], senti["sentiment"]["score"]))
    pickle.dump(rank_list, outfile)

def entity_extract():
    for get in getter:
        query_alch_final = baseUrlEnt + "&url=" + get.strip() + queryStringEnd
        a = urllib2.urlopen(query_alch_final)
        b = json.load(a)
        for senti in b["entities"]:
            if senti["type"] == "FieldTerminology":
                if senti["sentiment"]["type"] == "positive":
                    rank_list.append((senti["text"], senti["relevance"], senti["sentiment"]["score"]))
            if senti["type"] == "Technology":
                if senti["sentiment"]["type"] == "positive":
                    rank_list.append((senti["text"], senti["relevance"], senti["sentiment"]["score"]))
    pickle.dump(rank_list, outfile)
  
f = open("search.txt")
outfile = open("result_ranked.txt", "wb")
getter = f.readlines()
keyword_extract()
exit()
