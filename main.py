from bs4 import BeautifulSoup
import urllib3
import lxml

def main():
    print "PyBeuatifulCode beta";
    isFromWeb = input("isFromWeb = ");
    url = None;
    if isFromWeb == True :
        url = raw_input("url = ");
    else: 
        url = raw_input("code = ");
    
    filename = raw_input("filename = ");
    # urlDef = "http://info.cern.ch/hypertext/WWW/TheProject.html";
    if isFromWeb == True:
       http = urllib3.PoolManager();
       req = http.request("GET",url)
       bs = BeautifulSoup(req.data,"lxml");
    else:
       bs = BeautifulSoup(url, "lxml");
    bsBody = bs;
    filee = open(filename,"w+");
    filee.write(str(bsBody.find_all(True)[0]));
    print "ok"
    
main();