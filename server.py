from flask import Flask
from flask import request

app=Flask(__name__)

#Members api route

@app.route("/members")
def members():
    return {"members":["rizo","abcd"]}

@app.route("/predict/<long>/<lat>")
def predict(long,lat):
    recievedmessage={"long":long,"lat":lat}
    response=scanareapredict(recievedmessage)
    return {"value":response}

def scanareapredict(x):
    # y=predict(x)
    pass
    return 0

@app.route("/chatbot",methods=['GET','POST'])
def chatbot():
    recievedmessage=request.data.decode()
    response=chatbotpredict(recievedmessage)
    return {"message":response}

def chatbotpredict(x):
    # y=model.predict(x)
    pass
    return "asd"


if __name__=="__main__":
    app.run(debug=True)