import socket
import subprocess

# get HostName
print(socket.gethostname())

# get hostname Ip v4
print(socket.gethostbyname(socket.gethostname()))

def get_interface():
    command = "cat /proc/net/wireless |  awk 'NR==3{print $1}'"
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    output = str(process.stdout)
    output = output[:-2]
    return output

def get_ip():
    command = "ip -f inet -o addr show {} | cut -d\  -f 7 | cut -d/ -f 1".format(get_interface())
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    output = process.stdout
    return output[:-1]

print("ip : {}".format(get_ip()))
print("interface : {}".format(get_interface()))

def getNetworkDevicesList():
    """
    :return list of connected device(s) on local network
    """
    prefixIp = get_ip().split('.')[:-1]
    plage = "{0}.0-255".format('.'.join(prefixIp))
    nmap_command = "nmap -sP {0}".format(plage)
    process = subprocess.run(nmap_command, shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
    output2 = process.stdout

    try:
        rawdeviceList = [[elem.split(' ')[4], elem.split(' ')[5].strip('()')] for elem in output2.split('\n') if 'Nmap' and 'report' in elem and len(elem.split(' ')) == 6]
        ip = {elem[0]: elem[1] for elem in rawdeviceList}
        return ip
    except IndexError:
        print("error")


print(getNetworkDevicesList())