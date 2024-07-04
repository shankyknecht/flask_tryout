from flask import Flask

@app.route('/')
def home():
    return <p>"welkom op onze vernieuwde website"</p>

app=Flask('__main__')
if __name__ == '__main__': 
    app.run(port=5000,debug=true)