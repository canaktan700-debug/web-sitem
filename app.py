
from flask import Flask

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return """
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Benim İlk Sitem</title>
    </head>
    <body style="text-align:center; font-family:Arial; padding:50px;">
        <h1>Merhaba Dünya! 🚀</h1>
        <p>İlk web sitemi Python ile yaptım!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
