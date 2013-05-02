from flask import render_template, Flask, request
import arrange_list
import pickle
import figure
import data_builder
import decode_file

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
        #Need to call the google's query here so that we get the top results to extract keywords from
        search_results_links = data_builder.do_google_custom_search_for(query)
        
        ranked_keyword_list = decode_file.keyword_extract(search_results_links)
        
        return feedback_page(ranked_keyword_list)


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
def feedback_page(ranked_keyword_list):
    #buf = test_url.content_for_feedback_page()
    buf = ranked_keyword_list
    return render_template('request_keyword.html', data_list = buf, header = "Pick Keywords");

@app.route('/synonym/')
def synonym_page():
    buf = test_url.content_for_feedback_page()
    return render_template('fill_expert.html', data_list = buf, header = "Pick Synonym");

@app.route('/show_feedback/')
def show_gathered_feedback():
    global data
    sorted_data = data.items()
    sorted_data.sort(key=itemgetter(0), reverse=0)
    return render_template('print_database.html', data_list = sorted_data, tab_head = "Database", head_block = "Feedback" )

@app.route('/show_synonyms/')
def show_synonyms():
    global synonyms
    sorted_data = synonyms.items()
    sorted_data.sort(key=itemgetter(0), reverse=0)
    return render_template('print_database.html', data_list = sorted_data, tab_head = "Database",  head_block = "Synonyms")

@app.route('/flush_feedback/')
def flush_feedback():
    #TODO

    return render_template('welcome.html', info = "Flush feedback done")

@app.route('/flush_synonyns/')
def flush_synonyms():
    #TODO

    return render_template('welcome.html', info = "Flush synonyms done")

if __name__ == '__main__':
    global data
    global outfile
    global query
    #infile = open("feedback_sorted.txt", "rb")
    data = {}
    query = ""
    #infile.close()
    #outfile = open("feedback_sorted.txt", "wba", 0)
    app.run(port=5003,debug=True)
    pass


