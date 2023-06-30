from flask import Flask, render_template, request, redirect, url_for
import pyshorteners

app = Flask(__name__)

s = pyshorteners.Shortener(api_key="YOUR_KEY")

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = ""
    if request.method == 'POST':
        long_url = request.form.get('url')
        try:
            short_url = s.bitly.short(long_url)
        except Exception as e:
            return str(e)
    return render_template('index.html', short_url=short_url)

if __name__ == "__main__":
    app.run(debug=True)
