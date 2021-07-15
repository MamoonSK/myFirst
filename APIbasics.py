from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/',methods=['post'])
def post_ex():
    data=request.get_json()
    num1=int(data['num1'])
    num2=int(data['num2'])
    ss=num1+num2
    return(jsonify({'sum':ss}))

@app.route('/',methods=['get'])
def get_ex():
    return "Hello World!" #jsonify(['Mamoon','Rasheed','Shaik'])

#if(__name__=='__main__'):
app.run()
