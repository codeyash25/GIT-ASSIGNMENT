from flask import Flask , render_template
import json
app = Flask(__name__)

file  = open('Data.json' , 'r')
user_data = json.load(file)
file.close()
@app.route('/api')
def API():
    return user_data

if __name__ == '__main__':
    app.run(debug=True)