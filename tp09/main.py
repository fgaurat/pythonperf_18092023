import time
import requests
from bs4 import BeautifulSoup

def main():
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_logs = [a['href'] for a in soup.find_all('a') if '.log' in a['href']] 
    
    
    
    for log in all_logs:
        url_log = url+log
        response = requests.get(url_log)

        path_log = f".\logs\{log}"
        with open(path_log,"w") as log_file:
            log_file.write(response.text)
        



if __name__=='__main__':
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(end-start)
