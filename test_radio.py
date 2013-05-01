from flask import render_template, Flask, request
import arrange_list
import pickle
import figure
app = Flask(__name__)

external_repo = figure
test_url = arrange_list

@app.route('/')
def index():
    return render_template('request_expert.html',\
                            header = 'Give Expert Advice')


@app.route('/queryentered/', methods=['POST'])
def expert_query():
    global query
    if request.method == 'POST':
        print request.form
        query = request.form['text']
        return feedback_page()


@app.route('/feedbackentered/', methods=['POST'])
def gather_fdbk():
    global query
    global data
    global outfile
    if request.method == 'POST':
        entered_fdbk = request.form
        if (len(entered_fdbk) == 0):
            return feedback_page()
        temp = []
        for term in entered_fdbk:
            temp.append(entered_fdbk[term].strip().replace(" ", "%20"))
        data[query] = temp
        external_repo.feat_dict = data
        external_repo.wrapper_links()
        return render_template('request_expert.html', header = 'Give Expert Advice')

@app.route('/synonymquery/', methods=['POST'])
def expert_syn():
    global query
    if request.method == 'POST':
        print request.form
        query = request.form['text']
        return synonym_page()


@app.route('/synonymentered/', methods=['POST'])
def gather_syn():
    global query
    if request.method == 'POST':
        entered_syn = request.form
        if (len(entered_fdbk) == 0):
            return synonym_page()
        temp = []
        for term in entered_syn:
            temp.append(entered_syn[term].strip().replace(" ", "%20"))
        syn[query] = temp
        external_repo.feat_dict = syn
        external_repo.wrapper_links()
        return render_template('request_expert.html', header = 'Give Expert Advice')

@app.route('/feedback/')
def feedback_page():
    buf = test_url.content_for_feedback_page()
    return render_template('request_keyword.html', data_list = buf, header = "Pick Keywords");

@app.route('/synonym/')
def synonym_page():
    buf = test_url.content_for_feedback_page()
    return render_template('fill_expert.html', data_list = buf, header = "Pick Synonym");

if __name__ == '__main__':
    global data
    global outfile
    infile = open("feedback_sorted.txt", "rb")
    data = {}
    infile.close()
    outfile = open("feedback_sorted.txt", "wba", 0)
    app.run(port=5003,debug=True)
    pass


