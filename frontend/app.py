from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder=".")

@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

# CSS files
@app.route('/<path:filename>.css')
def css_files(filename):
    return send_from_directory('.', f'{filename}.css')

# JavaScript files
@app.route('/<path:filename>.js')
def js_files(filename):
    return send_from_directory('.', f'{filename}.js')

# Images 
@app.route('/<path:filename>.png')
def png_files(filename):
    return send_from_directory('.', f'{filename}.png')

@app.route('/<path:filename>.jpeg')
def jpeg_files(filename):
    return send_from_directory('.', f'{filename}.jpeg')

@app.route('/<path:filename>.jpg')
def jpg_files(filename):
    return send_from_directory('.', f'{filename}.jpg')

if __name__ == "__main__":
    app.run(debug=True)