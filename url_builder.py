import urllib2, json, pprint

data = {}


def add_empty_query_string(baseUrl):
    return baseUrl + "?"

def add_search_string(baseUrl) :
    return baseUrl + "(search=" + data['searchString'] + ")"

def add_api_key_to_query_string(baseUrl):
    return baseUrl + "&apiKey=" + data['bestBuyKey']

def add_format_to_query_string(baseUrl):
    return baseUrl + "&format=" + data['formatString']

def add_next_page_number(baseUrl):
    if data['page'] >= 0 :
        data['page'] = data['page'] + 1
        baseUrl = baseUrl + "&page=" + str(data['page'])
    
    return baseUrl

def add_previous_page_number(baseUrl):
    if data['page'] > 1 :
        data['page'] = data['page'] - 1;
        baseUrl = baseUrl + "&page=" + str(data['page'])

    return baseUrl

