from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Добавляем кастомный фильтр для Jinja2
@app.template_filter('pluralize')
def pluralize(number, form1, form2, form5):
    number = abs(number) % 100
    if 10 < number < 20:
        return form5
    number = number % 10
    if number == 1:
        return form1
    if 2 <= number <= 4:
        return form2
    return form5

from anketa_app import routes