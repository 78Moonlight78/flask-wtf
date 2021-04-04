from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/answer')
@app.route('/auto_answer')
def answer():
    profile = {
        'title': 'title',
        'surname': 'surname',
        'name': 'name',
        'education': 'education',
        'profession': 'profession',
        'sex': 'male',
        'motivation': 'motivation',
        'ready': 'True',
    }
    return render_template('auto_answer.html', **profile)

    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
