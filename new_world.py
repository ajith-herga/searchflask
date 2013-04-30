import init_url
app = Flask(__name__)


test_url = product_build


@app.route('/')
def index():
    return render_template('request.html')


@app.route('/queryentered/', methods=['POST'])
def entered_query():
    if request.method == 'POST':
        enteredQuery = request.form['text']
        if enteredQuery == "":
            return index()
        strip_ver = enteredQuery.lower().strip()
        test_url.search_text(strip_ver)
        if (test_url.feedback_needed):
            return feedback_page()
        else:
            return next_page()

@app.route('/feedbackentered/', methods=['POST'])
def gather_fdbk():
    if request.method == 'POST':
        return render_template("next.html")

@app.route('/next/')
def next_page():
    buf = test_url.content_for_next_page()
    return render_template('results.html', content_page = buf)
 
@app.route('/previous/')
def previous_page():
    buf = test_url.content_for_prev_page()
    return render_template('results.html', content_page = buf)

@app.route('/feedback/')
def feedback_page():
    buf = test_url.content_for_next_page()
    return render_template('request_keyword.html', data_list = buf)
 
@app.route('/')
def previous_page():
    buf = test_url.content_for_prev_page()
    return render_template('results.html', content_page = buf)
if __name__ == '__main__':
    test_url.init_data_on_call();
    app.run(debug=True)
    pass

