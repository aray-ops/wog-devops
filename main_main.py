from flask import Flask, render_template_string
from utils import SCORES_FILE_NAME

app = Flask(__name__)

ERROR_HTML = """
<html>
    <head>
        <title>Scores Game - Error</title>
    </head>
    <body>
        <h1 style="color:red">Error</h1>
        <div style="color:red">{{ error_message }}</div>
    </body>
</html>
"""

SUCCESS_HTML = """
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>Your Score is: <div style="color:green">{{ score }}</div></h1>
    </body>
</html>
"""

@app.route('/')
def score_server():
    """
    Serve the current score over HTTP with HTML formatting.
    """
    try:
        with open(SCORES_FILE_NAME, 'r') as f:
            score = f.read().strip()
        return render_template_string(SUCCESS_HTML, score=score)
    except Exception as e:
        return render_template_string(ERROR_HTML, error_message=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
