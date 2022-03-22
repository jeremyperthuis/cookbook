import py_cui
import socket
import subprocess

def get_ip():
    """
    :return: local network ip
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

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


class mainTUI:
    def __init__(self, master):
        self.master = master

        #self.panel_1 = self.master.add_text_box('network devices', 0, 0, row_span=4, column_span=2)
        self.panel_2 = self.master.add_text_box('Local ip', 2, 6, row_span=4, column_span=2, initial_text="IDHUEHEH")
        self.bouton = self.master.add_button('ip', 0, 2, command=self.display_ip)
        self.bouton = self.master.add_button('scan network devices', 0, 4, command=self.display_devices)
        self.liste = self.master.add_scroll_menu('network devices', 0, 0, row_span=7, column_span=2)

        # self.panel_1.add_item('TEST')
        # self.panel_1.add_item('TEST_2')
        # self.panel_1.add_item('TEST_3')
        # self.panel_2.set_text('test')

    def display_ip(self):
        str = get_ip()
        self.panel_2.set_text('{}'.format(str))

    def display_devices(self):
        str = getNetworkDevicesList()

        list_item = []
        for elem in str:
            list_item.append(elem)
            try:
                self.liste.remove_item(elem)
            except:
                pass
        #self.panel_1.set_text('{}\n test'.format(str))
        self.liste.add_item_list(list_item)


root = py_cui.PyCUI(10, 10)
root.set_title('CUI TODO List')
s = mainTUI(root)
root.start()