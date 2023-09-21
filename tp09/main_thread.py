import threading


the_lock = threading.Lock()

def traitement_long_1():
    with the_lock:
        for i in range(5):
            print(threading.current_thread().name,i)


def traitement_long_2():
    with the_lock:
        for i in range(5):
            print(threading.current_thread().name,i)

def main():
    th1 = threading.Thread(target=traitement_long_1)
    th2 = threading.Thread(target=traitement_long_2)

    th1.start()
    th2.start()

if __name__=='__main__':
    main()
