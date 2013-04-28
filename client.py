from flask import render_template, Flask, request
import urllib2, json, pprint
import url_builder
import product_search
import init_url
app = Flask(__name__)


test_url = product_search
json_response = ""


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
        strip_ver = enteredQuery.lower().strip()
        test_url.search_text(strip_ver)
    return next_page()


@app.route('/next/')
def next_page():
    buf = test_url.content_for_next_page();
    return render_template('results.html', json_response=buf)
 
@app.route('/previous/')
def previous_page():
    buf = test_url.content_for_prev_page();
    return render_template('results.html', json_response=buf)
if __name__ == '__main__':
    test_url.init_data_on_call();
    app.run(debug=True)
    pass

