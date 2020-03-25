from flask import Flask

app = Flask(__name__)

import os

# Try loading an evn var, or go to default.
which_env_file = os.environ.get('FROM_ENV_FILE', '.env-* did not load')

@app.route('/')
def index():
    return f'I am the index function: {which_env_file}'

