import file_getter
import nltk
import data_builder

data = {}
synonyms = {}
query_list = []
result_links = []
disp_res = 0

def check(feat, query, feat_dict):
    global list_dict
    global last_ind
    global term
    global query_list

    if (feat == ""):
        query_list.append(query)
        print query
        return
    
    last_elemen = (feat == list_dict[last_ind])
    for term in feat_dict[feat]:
        if (last_elemen):
            query1 = query + "%20" + term
            check("", query1, feat_dict)
        else:
            query1 = query + "%20" + term
            check(list_dict[(list_dict.index(feat) + 1)], query1, feat_dict)
    return

def wrapper_links(feat_dict):
    global list_dict
    global last_ind
    global term
    global query_list

    list_dict = [term for term in feat_dict]
    last_ind = len(list_dict) - 1
    term = []
    query_list = []
    check(list_dict[0], '', feat_dict)

    
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
            print data
            break
        except Exception, e:
            continue
        finally:
            pass


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
            #print filename
            break
        except Exception, e:
            #print e
            continue
        finally:
            pass 
    pass


def search_text(query_text):
    global data
    global synonyms
    global query
    global query_list
    global result_links
    global disp_res


    temp_synonyms = {}
    temp_data = {}

    tokens = nltk.word_tokenize(query_text)
    pos_tag = nltk.pos_tag(tokens)
    
    #print pos_tag
    
    for attr,val in pos_tag:
        if val == 'NN' and attr != 'phone':
            

            temp_data[attr] = [attr]

            if attr in synonyms.keys():
                if attr in data:
                    temp_data[attr] = data[attr] 
            else:    
                for key in synonyms.keys():
                    if attr in synonyms[key]:
                        if key in data:
                            del temp_data[attr]
                            temp_data[key] = data[key]
                            
            
    wrapper_links(temp_data)

    disp_res = 0
    result_links = []
    for query_temp in query_list:
        result_links.extend(data_builder.do_google_product_search_for(query_temp))

    #print result_links

    return 

def content_for_next_page():
    global disp_res
    global result_links

    len_look = len(result_links)

    if (disp_res + 20 <= len_look):
        buf = result_links[disp_res:disp_res+20]
        start = disp_res
        disp_res = disp_res + 20
        end = disp_res

    elif (disp_res == len_look):
        buf = []
        buf.append(('Done', 'previous'));
        start = disp_res
        end = start

    else:
        buf = result_links[disp_res:len_look]
        disp_res = len_look
        start = disp_res
        end = len_look
        pass

    return (buf, start, end)

def content_for_prev_page():
    global result_links
    global disp_res
    
    len_look = len(result_links)
    if disp_res == 0:
        buf = []
        buf.append(('Done', 'next'));
        start = end = len_look

    elif (disp_res - 20 <= 0):
        #First page, should ideally be only = 0
        buf = result_links[0:disp_res]        
        start = 0
        end = disp_res
        disp_res = 0
    else:
        # Will never have to display the last page with prev
        disp_res = disp_res - 20
        buf = result_links[disp_res:disp_res + 20]
        start = disp_res
        end = disp_res + 20

    return (buf, start, end)


def are_synonyms(a, b):
    global data
    global synonyms
    global query
    
    return a in synonyms.get(b,[]) \
               or b in synonyms.get(a,[]) \
               or any(a in words and b in words for words in synonyms.values())

def init_data_on_call():
    global data
    global synonyms
    global query
    global disp_res

    disp_res = 0

    read_latest_synonyms()
    read_latest_feedback()
    pass
