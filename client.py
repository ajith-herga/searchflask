from flask import render_template, Flask, request
app = Flask(__name__)

data = {}

@app.route('/')
def index():
    return render_template('request.html')


@app.route('/results/', methods=['POST'])
def show_results():
    if request.method == 'POST':

        categoryButton = request.form['category']

        if categoryButton == 'phone':
            print "Phone category button clicked \n"
            data['category'] = 'phone'
            
            choiceButton = request.form['display']
             
            if choiceButton == 'latest':
                print "Phone latest choiceButton clicked \n"
                data['choice'] = 'latest'

            elif choiceButton == 'newish':
                print "Phone newishButton clicked \n"
                data['choice'] = 'new-ish'
            
            elif choiceButton == 'old':
                print "Phone old choiceButton clicked \n"
                data['choice'] = 'old'
            pass
        pass
    pass
    
    return render_template('results.html', data=data)
    pass

if __name__ == '__main__':
   app.run(debug=True)
   pass

