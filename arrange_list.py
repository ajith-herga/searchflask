import pickle
from operator import itemgetter
def content_for_feedback_page():
    buf = []
    f = open("result_ranked.txt", "rb")
    getter = pickle.load(f)
    getter.sort(key=itemgetter(1), reverse=1)
    for key in getter:
        buf.append(key[0])
    return buf
