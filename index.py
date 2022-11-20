from flask import Flask
import requests
import id

def blocking():
    block1 = '<div style="display:flex;justify-content:center"><h1>'
    block2 = '</h1></div>'

    block = ''
    block += block1
    block+=str(id.id_counter())
    block+=block2
    return block

app = Flask(__name__)
'''
with open("xyz.txt", "r") as file:
    s = ''
    for i in range(50):
        s += file.readline()
'''




@app.route("/")
def index():
    
    s = "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Document</title></head><body><div style='display:flex;justify-content: center;'><h1>Количество подписчиков:</h1></div>"+ blocking() +"</body></html><script>setTimeout(function(){location.reload();},3000);</script>"
    print(s)

    return s


@app.route("/user/<name>")
def user(name):
    return '<h1>hello %s</h1>' % name

if __name__ == '__main__':
    app.run()