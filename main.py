#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord= request.form.get('button_discord')
    button_html= request.form.get('button_html')
    button_bd= request.form.get('button_bd')
    button_css= request.form.get('button_css')
    button_c_sharp= request.form.get('button_c_sharp')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_bd=button_bd, button_css=button_css, button_c_sharp=button_c_sharp)

if __name__ == "__main__":
    app.run(debug=True)