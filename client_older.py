from flask import render_template, Flask, request
import urllib2, json, pprint
import url_builder
import product_search
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
    if request.method == 'POST':
        
        categoryButton = request.form['category']
        if categoryButton == 'phone':
            checkedAttributes = request.form.getlist("Attribute")
        for i in range(0, len(product_search.requirements)):
            product_search.requirements[i] = 0;
        i = 0;
        for attr in attr
            if attr in checkedAttributes:
                print attr
        print "Depth "
        print product_search.requirements
        print "Checked Attributes ", checkedAttributes, "\n"
        
    return next_page()




@app.route('/next/')
def next_page():
    myUrl = baseUrl
    myUrl = url_builder.add_search_string(myUrl)
    myUrl = url_builder.add_empty_query_string(myUrl)
    myUrl = url_builder.add_api_key_to_query_string(myUrl)
    myUrl = url_builder.add_format_to_query_string(myUrl)
    myUrl = url_builder.add_next_page_number(myUrl)
    print "MY URL" + myUrl + "\n" 
    response = urllib2.urlopen(myUrl)
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
    print "MY URL" + myUrl + "\n" 
    response = urllib2.urlopen(myUrl)
    json_response = json.load(response)
    return render_template('results.html', json_response = json_response)

if __name__ == '__main__':
    url_builder.data['searchString'] = url_builder.searchString
    url_builder.data['bestBuyKey'] = url_builder.bestBuyKey
    url_builder.data['formatString'] = url_builder.formatString
    url_builder.data['page'] = 0
    app.run(debug=True)
    pass

