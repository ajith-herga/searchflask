import test_radio

feature_dict = {"display" : ["Retina", "AMOLED", "SuperLCD"], "data": ["4G","LTE","HSDPA", "3G"], "wireless" : ["802.11N"], "pairing" : ["NFC"], "camera" : ["Carl%20Zeiss", "Auto%20focus"]}
feature_fact = {"display" : ["Retina", "AMOLED", "SuperLCD"], "data": ["4G","LTE","HSDPA", "3G"]}
feat_dict = feature_dict


def check(feat, query):
    global list_dict
    global last_ind
    global term
    if (feat == ""):
        print query
        return
    last_elemen = (feat == list_dict[last_ind])
    for term in feat_dict[feat]:
        if (last_elemen):
            query1 = query + " " + term
            check("", query1)
        else:
            query1 = query + " " + term
            check(list_dict[(list_dict.index(feat) + 1)], query1)
    return

def wrapper_links():
    global list_dict
    global last_ind
    global term
    list_dict = [term for term in feat_dict]
    last_ind = len(list_dict) - 1
    term = []
    check(list_dict[0], '')

def are_synonyms(a, b):
    return a in synonym.get(b,[]) \
               or b in synonym.get(a,[]) \
               or any(a in words and b in words for words in synonym.values())


