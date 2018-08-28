'''
Got the following code snippet from 
http://stackoverflow.com/questions/2953462/pinging-servers-in-python

This is used to identify whether a host ip address is "up" or not.
You need to run the "check_host" function with administrator privileges since it employs ping function call
'''
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command

def check_host(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that some hosts may not respond to a ping request even if the host name is valid.
    """

    # Ping parameters as function of OS
    parameters = "-n 1 >nul 2>nul" if system_name().lower()=="windows" else "-c 1 >/dev/null 2>&1"

    # Pinging
    return system_call("ping " + parameters + " " + host) == 0