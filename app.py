from flask import Flask
from routes import main_bp
import config

app = Flask(__name__)
app.config.from_object(config)

# Register blueprints
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
