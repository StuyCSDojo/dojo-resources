from flask import Flask
from os.path import join

app = Flask(__name__)

@app.route('/private/resources/')
@app.route('/private/resources/<path:filename>')
def private_resources(filename='index.html'):
    path = join('private_resources/build/html', filename)
    return app.send_static_file(path)

@app.route('/public/resources/')
@app.route('/public/resources/<path:filename>')
def public_resources(filename='index.html'):
    path = join('public_resources/build/html', filename)
    return app.send_static_file(path)

@app.route('/public_resources/knights-tour-sketchpad/')
@app.route('/public_resources/knights-tour-sketchpad/<path:filename>')
def knight_tour(filename = 'index.html'):
    path = join('useful_links/knights-tour-sketchpad', filename)
    return app.send_static_file(path)

@app.route('/public_resources/nqueens-sketchpad/')
@app.route('/public_resources/nqueens-sketchpad/<path:filename>')
def nqueens_sketchpad(filename = 'index.html'):
    path = join('useful_links/nqueens-sketchpad', filename)
    return app.send_static_file(path)

def main():
    app.debug = True
    app.run(host="0.0.0.0", port=5000)

if __name__ == '__main__':
    main()

