from flask import Flask, jsonify, request

app = Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "John"
    }
]

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Jenkins CI/CD Demo"
    })

@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

@app.route("/employees", methods=["POST"])
def add_employee():

    data = request.get_json()

    employees.append({
        "id": len(employees) + 1,
        "name": data["name"]
    })

    return jsonify({
        "message": "Employee Added"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)