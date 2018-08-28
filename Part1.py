import socket

ip_list = ['31.13.74.36','53.163.225.50','40.97.142.194','132.163.4.107']

for ip in ip_list:
    print("Scanning IP: " + ip + ".")
    try:
        for port in range(1,1001):
            the_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            the_socket.settimeout(2)
            result = the_socket.connect_ex((ip,port))
            if result == 0:
                print("Port Number "+ str(port) + " is OPEN!")
            else: 
                print("Port Number "+ str(port) + " is closed.")
            the_socket.close()
    except socket.timeout:
        print("Timeout Occurred!")
    except socket.error:
        print("Trouble Connecting to Server!")
        
print("Port Scanning complete.")
        
            
    