import urllib2, json, pprint
from flask import render_template, Flask, request
from operator import itemgetter
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


def keyword_extract(search_links_list):
    for get in search_links_list:
        query_alch_final = baseUrlKey + "&url=" + get.strip() + queryStringEnd
        a = urllib2.urlopen(query_alch_final)
        b = json.load(a)
        for senti in b["keywords"]:
            if senti["sentiment"]["type"] == "positive":
                rank_list.append((senti["text"], senti["relevance"], senti["sentiment"]["score"]))
    #pickle.dump(rank_list, outfile)

    buf = []
    rank_list.sort(key=itemgetter(1), reverse=1)
    for key in rank_list:
        buf.append(key[0])
    
    return buf

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
  

def alchemy_search_function(search_links_list):
    #f = open("search.txt")
    #outfile = open("result_ranked.txt", "wb")
    #getter = f.readlines()
    return keyword_extract(search_links_list)
    
    pass

