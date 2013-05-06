from flask import render_template, Flask, request
import urllib2, json, pprint
import url_builder
import product_search
import init_url
import user_search_backend

app = Flask(__name__)
enteredQuery = ""

test_url = user_search_backend
json_response = ""


@app.route('/')
def index():
    return render_template('request.html')


@app.route('/results/', methods=['POST'])
def show_results():
    global enteredQuery

    url_builder.data['searchString'] = ""
    #print request
    if request.method == 'POST':
        enteredQuery = request.form['text']
        if enteredQuery == "":
            return index()
        strip_ver = enteredQuery.lower().strip()
        test_url.search_text(strip_ver)
    return next_page()


@app.route('/next/')
def next_page():
    global enteredQuery
    (buf, start, end) = test_url.content_for_next_page()
    return render_template('results.html', content_page = buf, start = start , end = end, query = enteredQuery)
 
@app.route('/previous/')
def previous_page():
    global enteredQuery
    (buf, start, end) = test_url.content_for_prev_page()
    return render_template('results.html', content_page = buf, start = start, end = end, query = enteredQuery)

if __name__ == '__main__':
    test_url.init_data_on_call();
    app.run(debug=True, port=5001)
    pass

