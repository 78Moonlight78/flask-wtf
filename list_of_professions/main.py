from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/list_prof/<style>')
def index(style):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template('list_prof.html', style=style, professions=professions)

    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
