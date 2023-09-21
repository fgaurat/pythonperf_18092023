import time
import requests
from bs4 import BeautifulSoup
from threading import Thread
import concurrent.futures


def download(p):
    url = p[0]
    log = p[1]
    url_log = url+log
    response = requests.get(url_log)
    path_log = f".\logs\{log}"
    with open(path_log,"w") as log_file:
        log_file.write(response.text)

def main():
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_logs = [a['href'] for a in soup.find_all('a') if '.log' in a['href']] 
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:    
        executor.map(download,[(url,u) for u in all_logs])
    



if __name__=='__main__':
    start = time.perf_counter()
    print("avant")
    main()
    print("après")
    end = time.perf_counter()
    print(end-start)
