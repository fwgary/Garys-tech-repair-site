from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1319125949446361088/Ip0Xv_tormJ_No6aZcxDdqt1ZZ8tpFamjkN5Bp4EZf3w1Qvwer6kENXTgiIJfPAN4pTK'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/devices')
def devices():
    return render_template('devices.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    if request.form.get('agree'):
        # Send a POST request to Discord webhook
        requests.post(DISCORD_WEBHOOK_URL, json={"content": "A new order has been placed!"})
        return redirect(url_for('home'))
    return redirect(url_for('devices'))

@app.route('/faq')
def faq():
    return render_template('faq.html')

if __name__ == '__main__':
    app.run(debug=True)