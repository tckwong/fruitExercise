from flask import Flask, request, Response
import mariadb
import json
import sys


app = Flask(__name__)

# decoration
@app.route('/api')

def homepage():
    return "<h1>Hello World</h1>"

@app.route('/api/fruit', methods=['GET', 'POST', 'PATCH'])

def fruit():
    fruit_name = "durian"
    if (request.method == 'GET'):
        resp = {
            'fruitName' : fruit_name
        }
        return Response(json.dumps(resp),
                                mimetype="application/json",
                                status=200)
    elif (request.method == 'POST'):
        data = request.json

        if (data.get('fruitName') != None):
            resp = "Wrong fruit"
            code = 400
            if (data.get('fruitName') == fruit_name):
                resp = "Correct fruit"
                code = 201
            return Response(resp,
                            mimetype="text/plain",
                            status=code)
        else:
            return Response("ERROR, MISSING ARGS",
                            mimetype="text/plain",
                            status=400)
    elif (request.method == 'PATCH'):
        return Response("Endpoint under maintenance",
                        mimetype="text/plain",
                        status=503)
    else:
        print("Something went wrong")


if (len(sys.argv) > 1):
    mode = sys.argv[1]
    if (mode == "production"):
        import bjoern
        host = '0.0.0.0'
        port = 5000
        print("Server is running in production mode")
        bjoern.run(app, host, port)
    elif (mode == "testing"):
        from flask_cors import CORS
        CORS(app)
        print("Server is running in testing mode")
        app.run(debug=True)
        #Should not have CORS open in production
    else:
        print("Invalid mode arugement, exiting")
        exit()
else:
    print ("No arguement was provided")
    exit()

