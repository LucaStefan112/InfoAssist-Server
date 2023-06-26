from flask import Flask, request
from trainer import chatbot

app = Flask(__name__)
requestCount = 0
maximumRequestCount = 200

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response


@app.route('/ask', methods=['POST'])
def get_endpoint():
    global requestCount
    global maximumRequestCount

    # Get the message from the body
    message = request.json.get('message')

    if message:
        if requestCount <= maximumRequestCount:
            response = chatbot(message)
            requestCount += 1
        else:
            print("Reached maximum number of requests!")
            response = "Reached maximum number of requests!"
    else:
        response = "Empty message received. Aborted request!"

    return {
        'message': response,
        'success': True
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
