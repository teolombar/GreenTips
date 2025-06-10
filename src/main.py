from flask import Flask, render_template, request, redirect, url_for
import random
import datetime
from tips import ranTip, ranQuiz
install()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    date = datetime.datetime.now()
    ftoday = date.strftime("%d/%m/%Y")
    yesterday = date - datetime.timedelta(days=1)
    fyesterday = yesterday.strftime("%d/%m/%Y")
    xyesterday = date - datetime.timedelta(days=2)
    xfyesterday = xyesterday.strftime("%d/%m/%Y")
    xxyesterday = date - datetime.timedelta(days=3)
    xxfyesterday = xxyesterday.strftime("%d/%m/%Y")
    xxxyesterday = date - datetime.timedelta(days=4)
    xxxfyesterday = xxxyesterday.strftime("%d/%m/%Y")
    tip = ranTip(date.day, date.month, date.year)
    ytip = ranTip(yesterday.day, yesterday.month, yesterday.year)
    xytip = ranTip(xyesterday.day, xyesterday.month, xyesterday.year)
    xxytip = ranTip(xxyesterday.day, xxyesterday.month, xxyesterday.year)
    xxxytip = ranTip(xxxyesterday.day, xxxyesterday.month, xxxyesterday.year)
    quiz = ranQuiz(date.day, date.month, date.year)
    text = ''
    if request.method == 'POST':
        text = ''
        ans = request.form.get('quiz')
        if ans == str(quiz.get('correct')):
            text = 'Ottimo! Continua così!'
        else:
            text = 'Ops, prova a cambiare le tue abitudini.'

    return render_template("index.jinja",
        tip=tip,
        ytip=ytip,
        xytip=xytip,
        xxytip=xxytip,
        xxxytip=xxxytip,
        ftoday=ftoday,
        fyesterday=fyesterday,
        xfyesterday=xfyesterday,
        xxfyesterday=xxfyesterday,
        xxxfyesterday=xxxfyesterday,
        qTitle=quiz.get('Title', 'none'),
        qOne=quiz.get('one', 'none'),
        qTwo=quiz.get('two', 'none'),
        qThree = quiz.get('three', 'none'),
        text=text
    )

if __name__ == "__main__":
    app.run(debug=False)
