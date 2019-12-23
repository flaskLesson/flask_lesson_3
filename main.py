from flask import Flask
from routes import user

app = Flask(__name__)
app.secret_key = "SECRET!!!"

app.register_blueprint(user.user_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5050', debug=True)
