from flask import render_template, Flask, request
import urllib2, json, pprint
import url_builder
import product_search
import nltk
app = Flask(__name__)

#Attribute to index mapping
attr_list = ['display', 'data_connectivity', 'wireless_connectivity', 'pairing_connectivity', 'camera_technology']
#Variables - globals
json_response = ""

#URL Form : https://api.remix.bestbuy.com/v1/products(search=phones)?apiKey=bkrmw5nuvtje73guc2v8mt8q&format=json
baseUrl = "https://api.remix.bestbuy.com/v1/products"

@app.route('/')
def index():
    return render_template('request.html')


@app.route('/results/', methods=['POST'])
def show_results():
    url_builder.data['searchString'] = ""
    print request
    if request.method == 'POST':
        enteredQuery = request.form['text']
        if enteredQuery == "":
            return index()
        #Clear the requirements list
        for i in range(0, len(product_search.requirements)):
            product_search.requirements[i] = 0

        tokens = nltk.word_tokenize(enteredQuery.lower().strip())
        pos_tag = nltk.pos_tag(tokens)
        # Assuming that the reuest is phone, look for other NNs, could have to 
        # make a 2 level list for other known devices, or create a dynamic list 
        # for phone itself later, easily modifiable for those cases.
        for attr,val in pos_tag:
            if val == 'NN':
                if attr in attr_list:
                    product_search.requirements[attr_list.index(attr)] = 1
        print product_search.requirements
        product_search.constructQuery(product_search.queryStringOrig, 0) 
    return next_page()




@app.route('/next/')
def next_page():
    myUrl = baseUrl
    myUrl = url_builder.add_search_string(myUrl)
    myUrl = url_builder.add_empty_query_string(myUrl)
    myUrl = url_builder.add_api_key_to_query_string(myUrl)
    myUrl = url_builder.add_format_to_query_string(myUrl)
    myUrl = url_builder.add_next_page_number(myUrl)
    #print "MY URL" + myUrl + "\n" 
    #response = urllib2.urlopen(myUrl)
    return render_template('results.html');
    json_response = json.load(response)
    return render_template('results.html', json_response = json_response )

@app.route('/previous/')
def previous_page():
    myUrl = baseUrl
    myUrl = url_builder.add_search_string(myUrl)
    myUrl = url_builder.add_empty_query_string(myUrl)
    myUrl = url_builder.add_api_key_to_query_string(myUrl)
    myUrl = url_builder.add_format_to_query_string(myUrl)
    myUrl = url_builder.add_previous_page_number(myUrl)
    #print "MY URL" + myUrl + "\n" 
    #response = urllib2.urlopen(myUrl)
    #json_response = json.load(response)
    #return render_template('results.html', json_response = json_response)
    return render_template('results.html')
if __name__ == '__main__':
    url_builder.data['searchString'] = url_builder.searchString
    url_builder.data['bestBuyKey'] = url_builder.bestBuyKey
    url_builder.data['formatString'] = url_builder.formatString
    url_builder.data['page'] = 0
    app.run(debug=True)
    pass

