
from flask import Flask, redirect

app = Flask(__name__)

# Mock WhatsApp group links
links = [
    "https://chat.whatsapp.com/MockGroupLink1",
    "https://chat.whatsapp.com/MockGroupLink2",
    "https://chat.whatsapp.com/MockGroupLink3"
]

counter = {"index": 0}

@app.route('/')
def rotator():
    link = links[counter["index"]]
    counter["index"] = (counter["index"] + 1) % len(links)
    return redirect(link)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
