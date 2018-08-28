from utils import * 
import socket
import time
import math

hostname_list = ['www.facebook.com','www.google.com','www.uiowa.edu'] #list of the hostnames used
serverip_list = [['Australia Melbourne','168.1.79.229'],['USA Virginia','156.154.70.1'],['USA NewYork','138.197.25.214'],['UAE Dubai','94.206.181.22'],['India NewDelhi','122.176.20.6'],['Italy Arezzo','217.73.226.120'],['Japan Tokyo','27.34.140.46'],['ChinaShenzhen','110.165.44.152'],['Brazil Cascavel','187.86.59.3'],['USA UIowa','128.255.1.3']] #list of lists [location, ip]
total_data_dictionary = {} #this will house a dictionary with hostnames as keys and values of form [location, NEW ip, mean RTT]
RTT_list_individual = [] #this will be used to keep track of the 10 RTTs
for host in hostname_list: 
    datalist = [] #clear datalist between hosts
    packet = create_DNS_query(host) #create packet
    clientSocketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #create UDP socket (SOCK_DGRAM)
    for server in serverip_list:
        counter = 10 #this counter will assure that we take 10 RTT measurements
        RTT_list_individual = [] #This will clear the individual RTT list between servers
        location = server[0] #This addresses the location of the server
        address = server[1]  #This addresses the original ip of the server
        clientSocketUDP.sendto(packet,(address,53)) #send the packet to the original ip
        try: #just in case you don't receieve the encoded ip back
            message, serverAddress = clientSocketUDP.recvfrom(2000) #receive the encoded ip back
            ip = decode_dns_message(message) #decode to get the new ip
        except Exception as E:
            print ("There was an Error in receiving message") #tell user that there was an error, print error, and continue. Eventually, we will see that if there is an error there will not be enough items associated with server name... this is why! Assume that there was an error in this case. 
            print (E)
            continue
        while counter > 0: #because you need to do 10 RTTs
            try:
                clientSocketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create TCP socket (SOCK_STREAM)
                time1 = time.time() #get t1
                clientSocketTCP.connect((ip,80)) #connect to new ip
                time2 = time.time() #get t2
                RTT = time2 - time1  #get difference between t1 and t2
                RTT_list_individual.append(RTT) #do this so that avg may be taken of all 10 RTT
                counter -= 1 #keep track of how many RTTs are left to calculate
                clientSocketTCP.close() #close the socket
            except Exception as E:#tell user that there was an error, print error, and continue. Eventually, we will see that if there is an error there will not be enough items associated with server name... this is why! Assume that there was an error in this case. 
                print ("There was an Error in finding mean RTT")
                print(E)
                continue
        mean_RTT = sum(RTT_list_individual) / len(RTT_list_individual)  #get the mean of the individual 10 RTT values
        mean_RTT_rounded = round(mean_RTT,5)  #round the mean to 5 decimal points
        datalist.append([location,ip,mean_RTT_rounded]) 
    total_data_dictionary[host] = datalist #dictionary in form key= hostname and value = [location of server, new server ip, value of 10 RTT's rounded for that server and IP]
print(total_data_dictionary) 


            

