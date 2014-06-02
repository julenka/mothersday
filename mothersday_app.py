import csv
from datetime import datetime
import json

from flask import Flask, request, redirect, render_template

app = Flask(__name__)

def show_summary(sender):
    with open("log.txt") as f:
        data = f.readlines()
    return render_template('index.tmpl',
        user = sender,
        data = data)

@app.route('/')
def show_lidia():
    return show_summary("Lidia")


@app.route("/handle_sms", methods=['GET', 'POST'])
def handle_sms():
    import twilio.twiml
    callers = {"+14256816067": "Julia",
               "+14256816553": "Lidia"}
    from_number = request.values.get('From', None)
    body = request.values.get("Body", None)
    resp = twilio.twiml.Response()

    if from_number not in callers:
        resp.message("sorry, wrong number")
        return str(resp)

    try:
        body = body.replace("\n", "")
        body = body.replace(",", "")

        cur_time = datetime.now()
        with open("log.txt", "a") as f:
            f.write("{}, {}\n".format(cur_time.strftime("%Y-%m-%d %H:%M"), body))
        resp.message("Great job mom! You can view your logs at http://notjulie.com/mothersday" )
        return str(resp)
    except:
        e = sys.exc_info()[0]
        resp.message("error: %s" % str(e))
        return str(resp)

    return "shouldn't be here"

if __name__ == '__main__':
    app.debug = True
    app.run()
