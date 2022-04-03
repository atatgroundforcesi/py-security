#!/usr/bin/env python3

from platform import system
from re import search
from socket import gethostbyname, gethostname
from subprocess import PIPE, SubprocessError, run

class IPV4Scan:

    IPV4 = []

    def get_ipv4():

        network = []

        try:
            #get host IP
            host_name = gethostname()
            host_ipv4 = gethostbyname(host_name)
            pass

            ip_split = host_ipv4.split(".")
            host_netadress = (f"{ip_split[0]}.{ip_split[1]}.{ip_split[2]}")

            #IPV4
            for num in range (255):
                network.append(f"{host_netadress}.{num}")
            IPV4Scan.ping_ipv4(network, host_ipv4)
            print("*************************")
            print("Complete Network Scanned")

            pass

        except Exception as exception:
            return exception

    #gather networkinfo with ipv4
    def ping_ipv4(network,host_ipv4):

        try:
            for ip in network:
               
                command = [f"ping {ip}",f"ping {ip} -n 4"]
                
                if system().lower() == "windows":
                    command = command[0]
                else:
                    command = command[1]
                
                out = run(command, stdout=PIPE).stdout

                target = "Host" if ip == host_ipv4 else "Client"
            
                #Sucessfull ping show TTL(time to live)
                if search("TTL",str(out)):
                    msg = f"{target}, {ip} is up, ping sucessfull"
                else:
                    msg = f"{target}, {ip} ist down, check connection or unblock ping from firewall"

                IPV4Scan.IPV4.append(msg)
                print(msg)

            print(IPV4Scan.IPV4)

        except SubprocessError:
            exit(1)

IPV4Scan.get_ipv4()