from flask import Flask

#defines application

app = create_app()
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == '__main__':
    app.run(debug=True use_reloader=False)#use_reloader=False makes it so the application doesn't initiate twice--
    #when handling data this can cause errors.