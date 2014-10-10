import os.path
import socket
from urllib2 import Request, urlopen, URLError, HTTPError
from threading import Thread
import httplib, sys
from Queue import Queue

concurrent = 200

def doWork():
    while True:
        url = q.get()
        save_html_content(url)
        q.task_done()

def save_html_content(url):
    # Using the newer with construct to close the file automatically.
        save_path = 'C:/Users/srv.sngh92/Desktop/home/'
        list_of_visted_urls =[]
        name_of_file = url.split(".")
        completeName = os.path.join(save_path, name_of_file[1]+".html")         
        file1 = open(completeName, "w")    
        if url not in list_of_visted_urls:
            req = Request(url)
            
            response = urlopen(req)
            html_content = response.read()
            print  html_content 
            
            file1.write(html_content)
    
            file1.close()
        else:
            pass
        
if __name__ == '__main__':
    
    filename = 'C:/Users/srv.sngh92/Desktop/urls_list.txt'
    
    q = Queue(concurrent * 2)
    for i in range(concurrent):
        t = Thread(target=doWork)
        t.daemon = True
        t.start()
    try:
        with open(filename) as f:
             data = f.readlines()
        for row in data:
            url = row.split("\n")
            q.put(url[0])
        q.join()
    except KeyboardInterrupt:
        sys.exit(1)
