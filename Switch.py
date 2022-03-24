import wmi
import os


def menu():
    print("""OPTIONS 
    1) Set Static IP menu
    2) Set DHCP Address
    3) Configuration Profiles menu
    4) Test Network Connectivity""")
    select = input("Choose an option: ")

    if select == "1":
        select = None
        Static()
    elif select == "2":
        select = None
        DHCP()
    elif select =="3":
        select = None
        Profile()
    elif select == '4':
        select = None
        NetTest()
    else:
        select = None
        print("Invalid Entry")
        menu()


def Static():
    Nics = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    interface = Nics[0]

    # Take Static info from user
    ip = input(u"Please Insert Desired IP address: ")
    subnetmask = input(u"Please Insert Desired Subnet Mask: ") 
    gateway = input(u"Please Insert Desired Gateway: ")
    DNSServer = input(u'Please Input Desired DNS Server: ')

    # Put static info into place
    interface.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    interface.SetGateways(DefaultIPGateway=[gateway])
    interface.SetDNSServerSearchOrder([DNSServer])

    print('\n',"-----NEW INTERFACE CONFIGURATION-----",'\n',"IP ADDRESS = ",ip,'\n',"SUBNETMASK = ",subnetmask,'\n',"DEFAULT GATEWAY = ",gateway,'\n',"DNS SERVER = ",DNSServer)
    confirm()


def DHCP():
    # Switches between Static and DHCP addressing

    # Select interface
    Nics = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    nic = Nics[0]
    
    # appempt config change
    try:
        nic.EnableDHCP()
        print("Successfully changed to DHCP addressing")
        menu()
    except:
        print("ERROR Failed to Switch to DHCP addressing")
        menu()


def Profile():
    Profiles = []

    # Choose save or load profile
    SaveOrLoad = input("Would you like to save or load your configuration S/L: ")

    if SaveOrLoad == "L" or "l":
        
        # select file to load from
        ProfileSelect = input("Please specify name of the file containing the profile: ")

        # Attempt profile load
        try:
            Profile = open(ProfileSelect+".txt","r")
            print("The file ",Profile," contains the following Profiles;")
            for i in Profile:
                print(i)
                Profiles.append(i)
        except:
            print("This file does not exist Please try again")
            Profile()
    
    elif SaveOrLoad == "S" or "s":
        
        # Save location of new profile
        SaveLocation = input("Please specify file to save to: ")
        print("""Profile saving syntax: IP SUBNETMASK DEFAULTGATEWAY DNSSERVER
        Not following this syntax will result in misconfigured network settings!!!""")
        
        try:
            # Gather items for appending to list
            ip = input(u"Please Insert Desired IP address: ")
            subnetmask = input(u"Please Insert Desired Subnet Mask: ") 
            gateway = input(u"Please Insert Desired Gateway: ")
            DNSServer = input(u'Please Input Desired DNS Server: ')

            # prep items for appending
            appending = []
            appending.append(ip,subnetmask,gateway,DNSServer)

            ProcessedProfile = " ".join(appending)
            print(ProcessedProfile)

            # file = open(SaveLocation+".txt","a")
            # file.write(append)
            
        except:
            print("ERROR")
            ip = None
            subnetmask = None
            gateway = None
            DNSServer = None
            Profile()
    menu()


def NetTest():
    TestCases = []
    Results = []

    # This is the list of addresses to test
    testlist = input("Please specify the name of the address file: ")
    IpList = open(testlist+".txt","r")

    # Append Text to list
    print("This may Take a while... Please Wait!")
    for i in IpList:
        TestCases.append(i)
    IpList.close()

    # Send Pings to specified hosts
    for i in TestCases:
        send = os.system("ping "+ i +" >/dev/null 2>&1")

        if send == 0:
            print(i ,"is alive")
        else:
            print(i ,"is dead")
    menu()
   

def confirm():
    Userin = input("Are these settings correct?: Y/N: ")
    if Userin == "Y" or "y":
        print("Settings confirmed!")
        menu()

    elif Userin == "N" or "n":
        ip = None
        subnetmask = None
        gateway = None
        DNSServer = None
        print("Resetting values. Please Try again")
        Static()
    else:
        print("Invalid entry")
        confirm()

def main():
    menu()

main()
