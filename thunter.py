#!/usr/bin/env python
# -*- coding: utf-8 -*-
#CODED BY ISURUWA

##################### importing modules ################################

import os,sys,time
try:
    import requests
    from requests import get
    from art import *
    print("\033[35m  [\033[33m*\033[35m]\033[1;32m Required Modules Found")
    time.sleep(1)
except ModuleNotFoundError:
	print("\033[35m  [\033[33m*\033[35m]\033[31m Required Module Not Found !")
	time.sleep(1)
	print("\033[1;32m Installing !")
	os.system('pip install requests art ')
	print("\033[35m  [\033[33m*\033[35m]\033[35m Module Installed!")
	import requests
	from requests import get
	from art import *


############## Request & IP ########################

def requestdetails(url):
	request = requests.get(url)
	response = request.text
	print(response)


def ip():
    url = "http://ipinfo.io/ip"
    request = requests.get(url)
    response = request.text
    print("\033[35m  [\033[33m*\033[35m]\033[36mYour IP : " , response)
    print("")

################### CREDIT ###########################
def credit():
    print("\033[35m            ------ Sri \033[1;32mLanka \033[36m2021 -----")
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mCODED \033[31mBY \033[36mISURUWA")
    print("")


############# Banners ########################

def mainbanner():
    os.system('clear')
    print("\033[1;32m")
    tprint("""  Target
  Hunter""")
    credit()

def whoisbanner():
    os.system('clear')
    tprint(""" WHOIS""")
    credit()

def dnslookupbanner():
    os.system('clear')
    tprint(""" DNS""")
    credit()

def geoipbanner():
    os.system('clear')
    tprint(""" GEO-IP""")
    credit()

def portbanner():
    os.system('clear')
    tprint(""" PORT
 SCANNER""")
    credit()

def reverseipbanner():
    os.system('clear')
    tprint(""" REVERSE
 IP""")
    credit()

def traceroutebanner():
    os.system('clear')
    tprint(""" TRACE
 ROUTE""")
    credit()

def pingbanner():
    os.system('clear')
    tprint(""" PING
 SCAN""")
    credit()

def zonebanner():
    os.system('clear')
    tprint(""" Zone
 transfer""")
    credit()

def dnshostbanner():
    os.system('clear')
    tprint(""" DNS
 HOST""")
    credit()

def shareddnsbanner():
    os.system('clear')
    tprint(""" SHARED
 DNS""")
    credit()

def reverseipbanner():
    os.system('clear')
    tprint(""" REVERSE
 IP""")
    credit()

def tcpbanner():
    os.system('clear')
    tprint(""" TCP
 PORT""")
    credit()

def subnetbanner():
    os.system('clear')
    tprint(""" SUBNET
 LOOKUP""")
    credit()

def headerbanner():
    os.system('clear')
    tprint(""" HEADER
 CHECK""")
    credit()

def pagelinkbanner():
    os.system('clear')
    tprint(""" PAGE
 LINK""")
    credit()

################## Update ###########################

def update():
    banner()
    credit()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32m Updating ... ")
    os.system('cd')
    os.system('rm -rf THunter')
    os.system('git clone https://github.com/isuruwa/THunter')
    os.system('cd THunter')
    os.system('pip install -r requirements.txt')
    os.system('python thunter.py')

############## About #####################################

def about():
    os.system('clear')
    mainbanner()
    credit()
    print("")
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32m 1.Target Hunter is a python based scanner which  interact with the Hacker Target API for All IP Tools .")
    print("")
    print("More info at Readme.md")
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[34m 1.Support me on github"+'\n')
    print("\033[35m  [\033[33m*\033[35m]\033[36m Support me & Report Bugs >> Github - https://github.com/isuruwa")
    print("\033[35m  [\033[33m*\033[35m]\033[34m          >>Facebook - https://www.facebook.com/isuru.umayanga.37819 ")
    print("\033[35m  [\033[33m*\033[35m]\033[33m          >>Telegram - https://t.me/STATUSINVALIDED ")
    print("\033[35m  [\033[33m*\033[35m]\033[35m          >>Telegram - https://t.me/technolk ")
    print("\033[35m  [\033[33m*\033[35m]\033[37m          >>Whatsapp - https://wa.me/+447441467464 ")
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32m STAY SAFE .")
    print("")
    inp = input("\033[35m  [\033[33m*\033[35m]\033[1;32m Press Enter To Continue : ")
    if inp == "":
        menu()


################### Exit ###############################################
def exit():
    mainbanner()
    credit()
    print("\033[35m  [\033[33m*\033[35m]\033[35m Thank You . Stay Safe")
    time.sleep(1)
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mCODED \033[33mBY \033[36mISURUWA")
    print("")
    quit()


##################### Traceout #####################

def traceoutfunc():
    traceroutebanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/mtr/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()


##################### Ping Test #####################

def pingtest():
    pingbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/nping/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()


##################### DNS LOOKUP #####################

def dnslookup():
    dnslookupbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32msScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/dnslookup/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()




##################### Reverse DNS #####################
def reversedns():
    reverseipbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/reversedns/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()




##################### DNS HSOT SCAN #####################

def dnshost():
    dnshostbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32msScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/hostsearch/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()



##################### Shared DNS #####################

def shareddns():
    shareddnsbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/findshareddns/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()



##################### Zone Transfer #####################

def zonetransfer():
    zonebanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/zonetransfer/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()



##################### Whois #####################

def whois():
    whoisbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/whois/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()



##################### Geoip #####################

def geoip():
    geoipbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/geoip/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()

##################### Reverse IP #####################

def reverseip():
    reverseipbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/reverseiplookup/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()

##################### TCP PORT SCAN #####################

def tcpport():
    tcpbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/nmap/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()

##################### Subnet Calc #####################

def subnet():
    subnetbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/subnetcalc/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()

##################### Http Header #####################

def httpheader():
    headerbanner()
    ip()
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/httpheaders/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()

##################### Page Link #####################

def pagelink():
    pagelinkbanner()
    ip()
    print("")
    print("\033[35m  [\033[33m*\033[35m]\033[1;32mScript Loaded..")
    print("")
    target = input("\033[35m  [\033[33m*\033[35m]\033[36mTarget IP or Domain  : ")
    print("")
    url = "https://api.hackertarget.com/pagelinks/?q=" + target
    print("")
    requestdetails(url)
    print("")
    inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Press Enter To Continue  >>> ")
    menu()


############### Menu ###########################
def menu():
        mainbanner()
        ip()
        print("\033[35m  [\033[33m*\033[35m]\033[31m 1.Ping Test")
        print("\033[35m  [\033[33m*\033[35m]\033[1;32m 2.Whois Lookup")
        print("\033[35m  [\033[33m*\033[35m]\033[34m 3.Geo Ip Lookup")
        print("\033[35m  [\033[33m*\033[35m]\033[34m 4.Reverse IP LOOKUP")
        print("\033[35m  [\033[33m*\033[35m]\033[35m 5.DNS Lookup")
        print("\033[35m  [\033[33m*\033[35m]\033[36m 6.Reverse DNS")
        print("\033[35m  [\033[33m*\033[35m]\033[37m 7.DNS HSOT Finder")
        print("\033[35m  [\033[33m*\033[35m]\033[31m 8.Shared DNS finder")
        print("\033[35m  [\033[33m*\033[35m]\033[1;32m 9.Tcp Port Scan")
        print("\033[35m  [\033[33m*\033[35m]\033[33m 10.SubNet Lookup")
        print("\033[35m  [\033[33m*\033[35m]\033[34m 11.Header Check")
        print("\033[35m  [\033[33m*\033[35m]\033[35m 12.Zone Transfer")
        print("\033[35m  [\033[33m*\033[35m]\033[36m 13.Page Link Extractor")
        print("\033[35m  [\033[33m*\033[35m]\033[37m 14.Traceoute")
        print("\033[35m  [\033[33m*\033[35m]\033[31m 15.About")
        print("\033[35m  [\033[33m*\033[35m]\033[1;32m 16.Update")
        print("\033[35m  [\033[33m*\033[35m]\033[34m 17.More Tools")
        print("\033[35m  [\033[33m*\033[35m]\033[31m 18. Exit")
        print("")
        try:
            inp=input("\033[35m  [\033[33m*\033[35m]\033[36m Enter Your Option  >>> ")
            if inp == "1":
              pingtest()
            if inp == "2":
              whois()
            if inp == "3":
              geoip()
            if inp == "4":
              reverseip()
            if inp == "5":
              dnslookup()
            if inp == "6":
              reversedns()
            if inp == "7":
              dnshost()
            if inp == "8":
              shareddns()
            if inp == "9":
              tcpport()
            if inp == "10":
              subnet()
            if inp == "11":
              headercheck()
            if inp == "12":
              zonetransfer()
            if inp == "13":
              pagelink()
            if inp == "14":
              traceout()
            if inp == "15":
              about()
            if inp == "16":
              update()
            if inp == "17":
              os.system('am start -a android.intent.action.VIEW -d https://github.com/isuruwa')
            if inp == "18":
              exit()
            if inp == "":
              menu()
            else:
              print("\033[35m  [\033[33m*\033[35m]\033[31m Invalid Choice")
              time.sleep(1)
              menu()
        except:
           print("\033[35m  [\033[33m*\033[35m]\033[31m SCRIPT STOPING ...")
           time.sleep(1)
           quit()


menu()



