from flask import Flask, render_template, request
import zlib

app = Flask(__name__)

def crc32(text):
    return format(zlib.crc32(text.encode("utf-8")) & 0xffffffff, "08X")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        original = request.form["original"]
        received = request.form["received"]
        sender_crc = crc32(original)
        receiver_crc = crc32(received)
        accepted = sender_crc == receiver_crc
        result = {
            "sender_crc": sender_crc,
            "receiver_crc": receiver_crc,
            "accepted": accepted
        }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
