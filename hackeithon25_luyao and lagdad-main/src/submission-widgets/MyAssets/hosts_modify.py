import os
from urllib.parse import urlparse
import shutil

class hosts_modify:
    hosts_path:str=""
    urlMode :str=""
    url_list  = []
    def __init__(self,data):

        try: #split the url_list by comma
            self.url_list = str(data["url_list"]).split(",")
        except:
            self.url_list[0] = data["url_list"]
        print(self.url_list)
        for i in self.url_list:# check if the url is valid
            if all([urlparse(i).scheme,urlparse(i).netloc]):
                raise ValueError("Invalid URL")
        
        if os.name == 'nt':
            host_path = "C:\Windows\System32\drivers\etc\hosts"
        else: 
            host_path = "/etc/hosts"
        
    def change_hosts(self,action="stop"):
        if action == "start":            
            shutil.copy2(self.hosts_path, "hosts_backup")
            hosts_file = open(self.hosts_path,"a")
            for i in self.url_list:# bloock the url
                hosts_file.write(f"\n127.0.0.1 {i}")
            hosts_file.close()
        else:
            shutil.copy2("hosts_backup",self.hosts_path)#restore the hosts file
            os.remove("hosts_backup")
        





        
    

if __name__ == "__main__":
    pass