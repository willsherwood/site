from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1')
def prob():
    return render_template('problem.html')

@app.route('/fonts/<path:path>')
def fonts_serve(path):
    return send_from_directory('fonts', path)

@app.route('/css/<path:path>')
def css_serve(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>')
def js_serve(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    app.run(debug=True)
