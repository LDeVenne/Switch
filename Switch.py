import wmi
import os


def menu():
    print("""OPTIONS 
    1) Set Static IP menu
    2) Set DHCP Address
    3) Configuration Profiles menu
    4) Test Network Connectivity""")
    select = int(input("Choose an option: "))

    if select == 1:
        select = None
        StaticInput()
    elif select == 2:
        select = None
        DHCP()
    elif select == 3:
        select = None
        Profile()
    elif select == 4:
        select = None
        NetTest()
    else:
        select = None
        print("Invalid Entry")
        menu()

def StaticInput():

    # Take Static info from user
    ip = input(u"Please Insert Desired IP address: ")
    subnetmask = input(u"Please Insert Desired Subnet Mask: ") 
    gateway = input(u"Please Insert Desired Gateway: ")
    DNSServer = input(u'Please Input Desired DNS Server: ')
    Static(ip,subnetmask,gateway,DNSServer)

def NewIntConfig(ip,subnetmask,gateway,DNSServer):
    # Display of specified IP information
    print('\n',"-----NEW INTERFACE CONFIGURATION-----",'\n',"IP ADDRESS = ",ip,'\n',"SUBNETMASK = ",subnetmask,'\n',"DEFAULT GATEWAY = ",gateway,'\n',"DNS SERVER = ",DNSServer)
    Userin = int(input("""Are these settings correct?
    1) Yes
    2) No
    Choose an option: """))
    try:
        if Userin == 1:
            print("Settings confirmed!")
            menu()

        elif Userin == 2:
            ip = None
            subnetmask = None
            gateway = None
            DNSServer = None
            print("Resetting values. Please Try again")
            StaticInput()
    except:
        print("Invalid Entry... Please Try Again!")


def Static(ip,subnetmask,gateway,DNSServer):
    NewIntConfig(ip,subnetmask,gateway,DNSServer)
    Nics = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    interface = Nics[0]

    # Put static info into place
    interface.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    interface.SetGateways(DefaultIPGateway=[gateway])
    interface.SetDNSServerSearchOrder([DNSServer])

    
    


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
    SaveOrLoad = int(input("""Would you like to save or load your configuration
    1) Save
    2) Load
    Choose an option: """))
    
    # Process User Input
    if SaveOrLoad == 2:
        # This section is for loading a configuration
        # select file to load from
        # Do not include file extensions
        ProfileSelect = input("Please specify name of the file containing the profile: ")

        # Attempt profile load
        try:
            Profile = open(ProfileSelect+".txt","r")
            print('\n',"The file ",ProfileSelect," contains the following Profile;")

            # Add items to list for profile display
            for i in Profile:
                print(i)
                Profiles.append(i)
            Profile.close()
            Profiles = [i for item in Profiles for i in item.split()]
            # print(Profiles)

            ip = Profiles[1]
            subnetmask = Profiles[2]
            gateway = Profiles[3]
            DNSServer = Profiles[4]

            Static(ip,subnetmask,gateway,DNSServer)


        except:
            print("This file does not exist Please try again")
            menu()

    
    elif SaveOrLoad == 1:
        #  This Section is for saving a configuration
        # Save location of new profile
        # print("""Profile saving syntax: IP SUBNETMASK DEFAULTGATEWAY DNSSERVER
        # Not following this syntax will result in misconfigured network settings!!! '\n'""")
        SaveLocation = input("Please specify file to save to: ")
      
        try:
            ProfileName = input(u"Enter a Name for this Profile:")
            ip = input(u"Please Insert Desired IP address: ")
            subnetmask = input(u"Please Insert Desired Subnet Mask: ") 
            gateway = input(u"Please Insert Desired Gateway: ")
            DNSServer = input(u'Please Input Desired DNS Server: ')

            # prep items for appending
            appending = ["---"+ProfileName+"---",ip,subnetmask,gateway,DNSServer]

            ProcessedProfile = " ".join(appending)
            # print(ProcessedProfile)

            file = open(SaveLocation+".txt","a")
            file.write(ProcessedProfile)
            file.close()

        except:
            # Error checking invalid or incomplete inputs from user
            print("ERROR: please try again!")
            ip = None
            subnetmask = None
            gateway = None
            DNSServer = None
            menu()
          

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
   




        

def main():
    menu()


main()
