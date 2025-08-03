from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        try:
            page = wikipedia.page(search_term)
            return render_template('result.html', title=page.title, summary=page.summary, url=page.url)
        except Exception as e:
            return f"Error: {str(e)}"
    return '''
    <h1>Wikipedia Search</h1>
    <form method="post">
        <input name="search_term" placeholder="Enter search term">
        <button type="submit">Search</button>
    </form>
    '''

app.run(host='127.0.0.8', port=3399, debug=True)

