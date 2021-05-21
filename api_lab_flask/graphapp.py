#!/usr/bin/python3

import numpy as np # number operations
import yaml # pyyaml for yaml
import re  # regex
import paramiko # ssh into servers
from flask import Flask, render_template
import matplotlib.pyplot as plt

def sshlogin(ip, un, passw):
    sshsession = paramiko.SSHClient()
    sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshsession.connect(hostname=ip, username=un, password=passw)
    ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command("cat /proc/uptime")
    sshresult = ssh_stdout.read().decode('utf-8').split()[0]
    with open("sshresult", "w") as myfile:
        myfile.write(sshresult)
    days = (int(float(sshresult)) / 86400)  # convert uptime in sec to days
    sshsession.close()
    print(days)
    return days

app = Flask(__name__)

@app.route("/graphin")
def graphin():
    with open("/home/student/myCode/api_lab_flask/sshpass.yml") as sshpass: # creds for our servers
        creds = yaml.load(sshpass)
    print(f"how many clients: {len(creds)}")
    svruptime = []
    xtick = []
    for cred in creds:
        xtick.append(cred['ip'])
        resp = sshlogin(cred['ip'], cred['un'], cred['passw'])
        svruptime.append(resp)
    xtick = tuple(xtick) # create a tuple
    svruptime = tuple(svruptime)

    # graphin
    N = len(creds) # total number of bars
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    p1 = plt.bar(ind, svruptime, width)

    plt.ylabel('Uptime in Days')

    plt.title('Uptime of Servers in Days')
    plt.xticks(ind, xtick)
    plt.yticks(np.arange(0, 20, 1)) # prob want to turn this into a log scale

    plt.savefig('/home/student/myCode/api_lab_flask/static/status.png') # might want to save this with timestamp for history purposes
    return render_template("graph.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
