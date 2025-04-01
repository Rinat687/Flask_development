from flask import render_template, request, session
from anketa_app import app

# Установим секретный ключ для работы с сессиями
app.secret_key = 'your-secret-key-123'


@app.route('/', methods=['GET', 'POST'])
def index():
    # Инициализируем список анкет в сессии, если его нет
    if 'ankets' not in session:
        session['ankets'] = []

    if request.method == 'POST':
        # Создаем новую анкету
        new_anket = {
            'name': request.form.get('name'),
            'city': request.form.get('city'),
            'hobby': request.form.get('hobby'),
            'age': request.form.get('age')
        }

        # Добавляем новую анкету в список
        session['ankets'].append(new_anket)
        # Важно: нужно явно пометить сессию как измененную
        session.modified = True

    # Передаем все анкеты в шаблон
    return render_template('index.html', ankets=session.get('ankets', []))