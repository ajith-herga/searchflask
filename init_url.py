#Variables - globals

searchString = ""
bestBuyKey = "bkrmw5nuvtje73guc2v8mt8q"
formatString = "json"
baseUrl = "https://api.remix.bestbuy.com/v1/products"

def render_on_next_page():
    myUrl = baseUrl
    myUrl = url_builder.add_search_string(myUrl)
    myUrl = url_builder.add_empty_query_string(myUrl)
    myUrl = url_builder.add_api_key_to_query_string(myUrl)
    myUrl = url_builder.add_format_to_query_string(myUrl)
    myUrl = url_builder.add_next_page_number(myUrl)
    print "MY URL" + myUrl + "\n" 
    response = urllib2.urlopen(myUrl)
    json_response = json.load(response)
    return render_template('results.html', json_response = json_response)

def render_on_previous_page():
    myUrl = baseUrl
    myUrl = url_builder.add_search_string(myUrl)
    myUrl = url_builder.add_empty_query_string(myUrl)
    myUrl = url_builder.add_api_key_to_query_string(myUrl)
    myUrl = url_builder.add_format_to_query_string(myUrl)
    myUrl = url_builder.add_previous_page_number(myUrl)
    print "MY URL" + myUrl + "\n" 
    response = urllib2.urlopen(myUrl)
    json_response = json.load(response)
    return render_template('results.html', json_response = json_response)

def init_data_on_call():
    url_builder.data['searchString'] = searchString
    url_builder.data['bestBuyKey'] = bestBuyKey
    url_builder.data['formatString'] = formatString
    url_builder.data['page'] = 0
    url_builder.data['base'] = baseUrl

def search_text(text):
   well = 0
