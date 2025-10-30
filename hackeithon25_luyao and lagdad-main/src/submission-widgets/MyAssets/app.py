from flask import *
from flask_cors import CORS
import os
from hosts_modify import hosts_modify 
app = Flask(__name__)
data= {}
CORS(app)

@app.route("/hosts",methods=["POST"])
def block_hosts():
    data = request.json
    status = "Success"
    print(data)
    try:
        hosts= hosts_modify(data)
        hosts.change_hosts(data["action"])
    except PermissionError and OSError:
        status = "PermissionError"
    except ValueError and KeyError:
        status = "Invalid URL"
    print("error"
          +status)
    return {"status":status}

@app.route("/hosts",methods=["GET"])
def get():
    return("hello")        
    

if __name__ =="__main__":
    app.run(port=5000,debug=True)
