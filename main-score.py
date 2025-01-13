from flask import Flask, render_template_string
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)

HTML_SCORE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Scores Game</title>
</head>
<body>
    <h1>The score is <div id="score">{{ score }}</div></h1>
</body>
</html>
"""

HTML_ERROR_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Scores Game</title>
</head>
<body>
    <h1><div id="score" style="color:red">{{ error }}</div></h1>
</body>
</html>
"""

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as f:
            score = f.read().strip()
        return render_template_string(HTML_SCORE_TEMPLATE, score=score)
    except Exception as e:
        return render_template_string(HTML_ERROR_TEMPLATE, error=f"Error reading score: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
