# ex 1
# from flask import Flask
# from datetime import datetime
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def current_date():
#     now = datetime.now()
#     return f"The current date is {now.strftime('%Y-%m-%d')}"
#
#
# if __name__ == '__main__':
#     app.run()


# ex 2
# from flask import Flask
# from datetime import datetime
#
# app = Flask(__name__)
#
# @app.route('/')
# def greet_user():
#     now = datetime.now()
#     hour = now.hour
#     minute = now.minute
#
#     if 8 <= hour < 13:
#         greeting = "Good morning"
#     elif 13 <= hour < 17:
#         greeting = "Good afternoon"
#     elif 17 <= hour < 21:
#         greeting = "Good evening"
#     else:
#         greeting = "Good night"
#
#     return f"{greeting}, the current hour is {hour}:{minute}"
#
# if __name__ == '__main__':
#     app.run()

# ex 3
from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/guess_number/<int:number>')
def guess_number(number):
    random_number = random.randint(1, 100)
    success_message = None
    if number == random_number:
        success_message = "Congratulations! You guessed the correct number!"
    return render_template('guess_number.html', random_number=random_number, success_message=success_message)

if __name__ == '__main__':
    app.run()
