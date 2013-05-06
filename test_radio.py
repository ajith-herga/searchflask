from flask import render_template, Flask, request
from operator import itemgetter
import arrange_list
import pickle
import figure
import data_builder
import decode_file
import file_getter
import syn_build

app = Flask(__name__)

external_repo = figure
test_url = arrange_list

data = {}
synonyms = {}
query = ""

latest_correct_feedback_file = ""
latest_correct_synonym_file = ""

@app.route('/')
def index():
    return render_template('request_expert.html',\
                            header = 'Give Expert Advice')


@app.route('/queryentered/', methods=['POST'])
def expert_query():
    global query
    global data
    global synonyms

    if request.method == 'POST':
        print request.form
        query = request.form['text']
        print "query", query
        #Need to call the google's query here so that we get the top results to extract keywords from
        
        category_button = request.form['category']
        print category_button

        if category_button == 'feedback':
            search_results_links = data_builder.do_google_custom_search_for(query)
            print "search_results_links", search_results_links
            synonyms[query] = [query]
            ranked_keyword_list = decode_file.keyword_extract(search_results_links)
            
            return feedback_page(ranked_keyword_list)
        else:
            print 'Category is synonyms'
            synonyms[query] = [query]
            ranked_keyword_list = syn_build.do_syn_search_for(query)
            print ranked_keyword_list
            return synonym_page(ranked_keyword_list)
        


@app.route('/feedbackentered/', methods=['POST'])
def gather_fdbk():
    global query
    global data
    global synonyms

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
    global data
    global synonyms

    if request.method == 'POST':
        print request.form
        query = request.form['text']
        return synonym_page()


@app.route('/synonymentered/', methods=['POST'])
def gather_syn():
    global query
    global data
    global synonyms

    if request.method == 'POST':
        entered_syn = request.form
        if (len(entered_syn) == 0):
            return synonym_page()
        temp = []
        for term in entered_syn:
            temp.append(entered_syn[term].strip().replace(" ", "%20"))

        synonyms[query] = temp
        print synonyms
        external_repo.feat_dict = synonyms
        external_repo.wrapper_links()
        return render_template('request_expert.html', header = 'Give Expert Advice')

@app.route('/feedback/')
def feedback_page(ranked_keyword_list):
    #buf = test_url.content_for_feedback_page()
    buf = ranked_keyword_list
    return render_template('request_keyword.html', data_list = buf, header = "Pick Keywords");

@app.route('/synonym/')
def synonym_page(ranked_keyword_list):
    #buf = test_url.content_for_feedback_page()
    buf = ranked_keyword_list
    return render_template('request_synonym.html', data_list = buf, header = "Pick Synonym");

@app.route('/show_feedback/')
def show_gathered_feedback():
    global query
    global data
    global synonyms

    sorted_data = data.items()
    sorted_data.sort(key=itemgetter(0), reverse=0)
    return render_template('print_database.html', data_list = sorted_data, tab_head = "Database", head_block = "Feedback" )

@app.route('/show_synonyms/')
def show_synonyms():
    global query
    global data
    global synonyms

    sorted_data = synonyms.items()
    sorted_data.sort(key=itemgetter(0), reverse=0)
    print sorted_data
    return render_template('print_database.html', data_list = sorted_data, tab_head = "Database",  head_block = "Synonyms")

@app.route('/flush_feedback/')
def flush_feedback():
    #TODO
    file_getter.flush_feedback_to_file(data)
    return render_template('welcome.html', info = "Flush feedback done")

def read_latest_synonyms():
    global query
    global data
    global synonyms

    latest_synonym_files = []
    latest_synonym_files = file_getter.get_last_modified_files('./synonyms/')
    
    if not latest_synonym_files:
        return

    for filename in latest_synonym_files:
        try:
            synonyms = file_getter.read_from_file_and_populate_synonyms(filename)
            print filename
            break
        except Exception, e:
            print e
            continue
        finally:
            pass 
    pass


@app.route('/flush_synonyns/')
def flush_synonyms():
    global query
    global data
    global synonyms

    file_getter.flush_synonyms_to_file(synonyms)
    return render_template('welcome.html', info = "Flush synonyms done")


def read_latest_feedback():
    global query
    global data
    global synonyms

    latest_feedback_files = []
    latest_feedback_files = file_getter.get_last_modified_files('./feedback/')
    
    if not latest_feedback_files:
        return

    for filename in latest_feedback_files:
        try:
            data = file_getter.read_from_file_and_populate_data(filename)
            break
        except Exception, e:
            continue
        finally:
            pass

    #TODO: Once we have the latest files, parse the one that is the correct one and latest
    pass


if __name__ == '__main__':
    
    #global data
    #global synonyms

    #global outfile
    #global query
    #infile = open("feedback_sorted.txt", "rb")
    #data = {}
    #synonyms = {}
    #query = ""
    #infile.close()
    #outfile = open("feedback_sorted.txt", "wba", 0)
    read_latest_feedback()
    read_latest_synonyms()
    app.run(port=5003,debug=True)
    pass


