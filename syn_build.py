import urllib2, json

synonymBase = "http://words.bighugelabs.com/api/2/7975c2c8cdd9ce63a094b67f99a39be7/"

def do_syn_search_for(query_str):
    
    #This does the query search for synonyms
    if (query_str == ""):
        return []
        pass

    synonymEnd = synonymBase + query_str + "/json"
    a = urllib2.urlopen(synonymEnd)
    b = json.load(a)
    if "noun" in b:
        return b["noun"]["syn"]
    else:
        return []
