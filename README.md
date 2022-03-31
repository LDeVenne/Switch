Welcome to Switch!

Switch is a program to streamline switching between DHCP and static addressing on windows servers
and also allows network tests to be conducted from any windows device

--How to use Switch--
launch program follow prompts, just that easy

--Static IP addresses--
Select The set static IP option and enter information as Prompted

--DHCP Addressing--
Select DHCP

--Profiles--
--Saving--
Select Profiles
choose save profile
enter file to save to
enter information as prompted
--Loading--
Select Profiles
Select Load
Choose file to load from
confirm settings


---Network Testing--
Create a text file with a list of IP Addresses with one address per line;
x.x.x.x
y.y.y.y
z.z.z.z

select option 3
program will prompt for the name of the text file, do not include the file extension as it is added automatically
wait for script to complete

--Prereqs--

python3
https://www.python.org/

wmi
https://github.com/tjguk/wmi

-OR-

pip install wmi

Windows OS*

*Windows Server is needed for full functionality
