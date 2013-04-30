feature_dict = {"display" : ["Retina", "AMOLED", "SuperLCD"], "data": ["4G","LTE","HSDPA", "3G"], "wireless" : ["802.11N"], "pairing" : ["NFC"], "camera" : ["Carl%20Zeiss", "Auto%20focus"]}
feature_fact = {"display" : ["Retina", "AMOLED", "SuperLCD"], "data": ["4G","LTE","HSDPA", "3G"]}
feat_dict = feature_dict

list_dict = [term for term in feat_dict]
last_ind = len(list_dict) - 1
term = []
def check(feat, query, req):
    last_elemen = (feat == list_dict[last_ind])
    if ((last_elemen) && (feat in list_dict)):
        return
    for term in feat_dict[feat]:
      if (last_element):
          print (query + " " + term)
          return
      else:
          query1 = query + " " + term
          check(list_dict[(list_dict.index(feat) + 1)], query1)
    return
print list_dict
check(list_dict[0], "")
