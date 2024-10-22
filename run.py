from app import config
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()
app = config()

if __name__ == '__main__':
    app.run(debug=True)