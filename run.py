from os import environ

from app import app

if __name__ == '__main__':
    if environ.get('APP_LOCATION') == 'heroku':
        app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))
    else:
        app.run(host='localhost', port=8080, debug=True, reloader=True)
