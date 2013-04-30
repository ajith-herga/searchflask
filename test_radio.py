from flask import render_template, Flask, request
import arrange_list
app = Flask(__name__)


test_url = arrange_list


@app.route('/')
def index():
    return render_template('request.html')


@app.route('/queryentered/', methods=['POST'])
def show_results():
    if request.method == 'POST':
        print request.form
        return feedback_page()

@app.route('/feedbackentered/', methods=['POST'])
def gather_fdbk():
    if request.method == 'POST':
        entered_fdbk = request.form
        if (len(entered_fdbk) == 0):
            return feedback_page()
        for term in entered_fdbk:
            print entered_fdbk[term]       
        return render_template("request.html")

@app.route('/feedback/')
def feedback_page():
    buf = test_url.content_for_feedback_page()
    return render_template('request_keyword.html', data_list = buf)
if __name__ == '__main__':
    app.run(port=5003,debug=True)
    pass

