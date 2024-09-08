#!/usr/bin/python3
import urllib.error
import urllib.request
from optparse import OptionParser
def adminpanel(url):
    try:
        urllib.request.urlopen(url)
        a_list=open("/usr/share/wordlists/admin.txt","r",encoding="utf-8")
        for i in a_list :
            end_url=url+"/"+i
            try:
                urllib.request.urlopen(end_url)
                print(end_url+":: found[++]")
            except urllib.error.HTTPError as a:
                print(end_url,a)
    except urllib.error.URLError as a:
        print(url)
        print(a)
# adminpanal("https://www.google.com")
pars= OptionParser("""
   #    ######  #     #   ###   #     # ######     #    #     # ####### #
  # #   #     # ##   ##    #    ##    # #     #   # #   ##    # #       #
 #   #  #     # # # # #    #    # #   # #     #  #   #  # #   # #       #
#     # #     # #  #  #    #    #  #  # ######  #     # #  #  # #####   #
####### #     # #     #    #    #   # # #       ####### #   # # #       #
#     # #     # #     #    #    #    ## #       #     # #    ## #       #
#     # ######  #     #   ###   #     # #       #     # #     # ####### #######

---------------------------
adminpanal -u + url
Developed by: Ibrahem abo kila
""")
pars.add_option("-u",dest="e_url",type="string",help="enter url")
(options ,args) = pars.parse_args()
if options.e_url == None:
    print(pars.usage)
else:
    adminpanel(options.e_url)
