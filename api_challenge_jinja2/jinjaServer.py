#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request
from flask.templating import render_template_string

app = Flask(__name__)
PORT = 3000

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route('/gethost')
def getHosts():
    try:
        print(groups)
        return render_template('hostInfo.j2', group=groups)
    except Exception as err:
        return "Bad happend inside getHosts() " + err

@app.route("/host/")
def hostInfo():
    try:
        qparms = {}
        # user passes hostName= or default "bootstrapped switch"
        qparms["hostName"]  = request.args.get("hostName", "host DEFAULT")
        # user passes fqdn= or default "DEFAULT"
        qparms["fqdn"]  = request.args.get("fqdn", "DEFAULT")
         # user passes ip= or default "0.0.0.0"
        qparms["ip"] = request.args.get("ip", "0.0.0.0")
        print(f'\n{qparms} \n all info')
        groups.append(qparms)
        print(groups)
        # render template and save as baseIOS.conf
        return render_template("hostInfo.j2", group = groups)

    except Exception as err:
        return "Bad happend inside hostInfo() " + err

if __name__ == "__main__":
    print(f'listening port: {PORT}')
    app.run(host="0.0.0.0", port=PORT)