from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Test route is working!'

@app.route('/')
def index():
    # Define the list of programming languages
    languages = [
        {'STT': 1, 'ten': "Python"},
        {'STT': 2, 'ten': "Java"},
        {'STT': 3, 'ten': "C++"}
    ]
    languages.append({'STT': 4, 'ten': ".NET"})
    languages.append({'STT': 5, 'ten': "Matlab"})

    # Pass the list to the template
    return render_template('abc.html', ngon_ngu=languages)

if __name__ == '__main__':
    app.run(debug=True)


