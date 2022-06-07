Welcome to Switch!

Switch is a program to streamline switching between DHCP and static addressing on windows servers
and also allows network tests to be conducted from any windows device


--How to use Switch--
launch program follow prompts, just that easy

--Static IP addresses--
You can set a static IP address manually using option 1 OR you can save addresses in profiles.csv (or another file of choice) using option 3 and loading a saved IP configuration
to save a configuration you must select option 3, option 2 and then follow the prompts to configure the profile

--Profiles--
Profiles allow you to save a static IP address to be used later, instead of needing to manually reconfigure them

Profiles can be set through the save option in the Profile configuration menu or manuallt add them to the profiles.csv file (ip,netmask,gateway,DNS Server) on a new line


---Network Testing--
Create a text file with a list of IP Addresses with one address per line;
x.x.x.x
y.y.y.y
z.z.z.z

select option 3
program will prompt for the name of the textx file, do not include the file extension as it is added automatically
wait for script to complete

Logs are saved in the NetTestResults.txt file


--Prereqs--

python3
https://www.python.org/

wmi
https://github.com/tjguk/wmi

-OR-

pip install wmi

Windows OS*

*Windows Server is needed for full functionality
*Test segments have been included for simulated use without a server environment