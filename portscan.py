

from re import search
from socket import AF_INET, SOCK_DGRAM, SOCK_STREAM, socket
from time import localtime, asctime

class PortScan():

    PORTS = []
    TARGET = []

    def main():
        options = ["-a/all (tcp and udp)","-t/tcp","-u/udp"]

        print(
f"""----Portscan----
Portscan scans the first 1-10000 well known Ports
Following Options are avaliable:
{options}
Enter IP and follwing Option
Example: 192.168.0.0 -a 
        """)

        target_init = input("Enter Host IP (IPV4): ") #Options for multiple Hosts will be following
        target = target_init[:-3]
        PortScan.TARGET.append(target)

        if search("-a",target_init):

            print("scanning for TCP and UPD")
            print("---TCP Scan---")
            PortScan.tcp_scan()
            print("---UDP Scan---")
            PortScan.udp_scan()

        if search("-t",target_init):
            print("scanning only for TCP")
            print("---TCP Scan---")
            PortScan.tcp_scan()

        if search("-u",target_init):
            print("scanning only for UPD")
            print("---UDP Scan---")
            PortScan.udp_scan()
        
        else:
            print("----PLEASE ENTER VALID OPTION OR EXIT WITH CTRL + C----")
            PortScan.main()
        
    def tcp_scan():
        var_protocol = "TCP"
        var_socket = SOCK_STREAM
        PortScan.scanning(var_protocol, var_socket)
    
    def udp_scan():
        var_protocol = "UDP"
        var_socket = SOCK_DGRAM
        PortScan.scanning(var_protocol, var_socket)

    def scanning(var_protocol,var_socket):
        try:
            for n in PortScan.TARGET:
                print(n)
                for port in range(0,1023): #Scanning for well known Ports
                    t = localtime()
                    timer = asctime(t)

                    s = socket(AF_INET,var_socket)
                    s.settimeout(0.1) #sec
                    connection = s.connect_ex((n,port))
                    
                    state = "[OPEN]" if connection == 0 else "[CLOSED]"
                    print(f"time: {timer} {var_protocol}: {port} is {state}")
                    s.close()
                    PortScan.PORTS.append(f"TCP Port: {port} is {state} /{timer}")

                print("scan finished")
                print(PortScan.PORTS)

        except:
            print("Error Occured")

if __name__=="__main__":
    PortScan.main()