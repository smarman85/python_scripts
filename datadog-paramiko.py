import os
import base64
import paramiko

input_file = open("../Documents/repos/configuration-management/ansible/inventory")

def write_to_file(host, payload):
    with open("kennel.yaml", "a") as outfile:
        outfile.write("""\
{0}
    {1}
""".format(host, payload

def bark(host):
    print(host)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host)
    stdin, stdout, stderr = client.exec_command('/sbin/service datadog-agent status')
    #decode_out = stdout.read().decode('utf-8')
    decode_err = stderr.read().decode('utf-8')
    if decode_err == "":
        for line in stdout:
            print ("    " + line.strip('\n'))
    else:
        print("    " + decode_err)
    client.close()

for line in input_file:
    if (line[0:2] != "lv"
            or "qadb" in line
            or "qaccapi" in line
            or "qaqi" in line
            or "pmt" in line
            or "sbx" in line
            or "wam" in line
            or "prod" in line
       ):
        pass
    else:
        bark(line.strip())

input_file.close()
