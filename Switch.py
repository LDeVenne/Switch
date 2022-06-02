import os
import csv

# WMI IS REQUIRED FOR THIS PROGRAM TO WORK PROPERLY
# THIS SECTION CAN BE COMMENTED FOR TESTING ON NON SERVER SYSTEMS
# import wmi




def menu():
    print("""OPTIONS 
    1) Set Static IP menu
    2) Set DHCP Address
    3) Configuration Profiles menu
    4) Test Network Connectivity""")
    select = int(input("Choose an option: "))

    if select == 1:
        select = None
        info = StaticInput()
        Static(info[0],info[1],info[2],info[3])
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
    return ip,subnetmask,gateway,DNSServer




def Static(ip,subnetmask,gateway,DNSServer):


   
    # return info

     # Display of specified IP information
    print('\n',"-----NEW INTERFACE CONFIGURATION-----",'\n',"IP ADDRESS = ",ip,'\n',"SUBNETMASK = ",subnetmask,'\n',"DEFAULT GATEWAY = ",gateway,'\n',"DNS SERVER = ",DNSServer)

    cont = confirm()

    if cont == 1:
        print("Settings confirmed!")
            # THIS SECTION IS FOR TESTING PURPOSES ONLY
     # ADDRESS WILL BE DISPLAYED IN TEXT IF SIMULATED LOADING IS SUCCESSFUL
    # COMMENT THIS SECTION TO USE
        Configs = [ip,subnetmask,gateway,DNSServer]
        # print(Configs)
        info = " ".join(Configs)
        print(info)

        # FOR USE UNCOMMENT THIS SECTION 
        # Nics = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
        # interface = Nics[0]

        # # Put static info into place
        # interface.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
        # interface.SetGateways(DefaultIPGateway=[gateway])
        # interface.SetDNSServerSearchOrder([DNSServer])
        menu()

    else:
        print("Cancelling please try again!")
        menu()

  


def DHCP():
    # Switches between Static and DHCP addressing

    # Select interface
    print("ATTEMPTING TO ENABLE DHCP ADDRESSING!")
    cont = confirm()
    if cont == 1:
        Nics = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
        nic = Nics[0]
        try:
            nic.EnableDHCP()
            print("Successfully changed to DHCP addressing")
            menu()
        except:
            print("ERROR Failed to Switch to DHCP addressing")
            menu()

    else:
         print("Cancelling please try again!")
         menu()

    # appempt config change
   



def Profile():
    print("""Would you like to create a new profile or load an existing profile?
    1) Save
    2) Load """)
    select = int(input("Choose an option: "))

    if select == 1:
        SaveProfile()
    elif select == 2:
        LoadProfile()
    else:
        print("Invalid input please try again!")
        Profile()




def SaveProfile():
    ProfileSaving = str(input("Enter the name of the file you would like to save to: "))
    profiles = open(ProfileSaving+".csv")
    ProfileProcessing = csv.writer(profiles)

    inputs = StaticInput()
    save = [i for i in inputs]

    print(",".join(save),"is now saved as an IP configuration profile.")

    with open(ProfileSaving+".csv",'a',newline='') as writing:
        write = csv.writer(writing)
        # write.writerow("\n")
        write.writerow(save)
        writing.close()
    
    menu()




def LoadProfile():
    
    # Load CSV for processing
    ProfileStorage = str(input("Enter the name of the file you would like to load from: "))
    profiles = open(ProfileStorage+".csv")
    ProfileProcessing = csv.reader(profiles)

    # list comprehension, adds every item to the CSV file to the contents
    Contents = [row for row in ProfileProcessing]

    # Takes input from the while loop, this is what the user would 
    Processed = []

    x = 0 
    y = 0
    # loop through contents, print from processed inputs
    while y in range(len(Contents)):
        FormattedIndex = ", ".join(Contents[y])
    
        # Filter out repeat entries, add it first then add it to processed list,
        # This means that if there is a duplicate profile it will only pass the if statement on the first pass
        if Contents[y] not in Processed:
            print("Profile",x+1,"-",FormattedIndex)
            Processed.append(Contents[y])
            x += 1

        y += 1
    

    # print(Contents)
    # print('\n',"Input is single interger value")
    SelectedList = int(input("Please enter the profile you would like to load: ")) - 1

    # print(Processed[SelectedList][0])
    ip = Processed[SelectedList][0]
    subnetmask = Processed[SelectedList][1]
    gateway = Processed[SelectedList][2]
    DNSServer = Processed[SelectedList][3]

    information = Static(ip, subnetmask, gateway, DNSServer)
    print(information)
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
        send = os.system("ping "+ i)

        # if send == 0:
        #     print(i ,"is alive")
        # else:
        #     print(i ,"is dead")
    menu()
   



def confirm():
    try:
        Userin = int(input("""Are these settings correct?
        1) Yes
        2) No
        Choose an option: """))
        return Userin
    except:
        print("Invalid input please try again!")
        menu()

    


def main():
    menu()


main()
