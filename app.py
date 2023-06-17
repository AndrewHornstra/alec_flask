from flask import Flask, request


app = Flask(__name__)

@app.route("/test", methods=["POST"])
def send_to_textract():
    return {
        "Hey": "Alec",
        "The form data you sent in was": request.form,
        f"You also sent in {len(request.files)} files, named": [request.files[file].filename for file in request.files],
        "status": 200
    }

if __name__ == "__main__":
    app.run()