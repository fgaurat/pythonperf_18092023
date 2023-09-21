

def do_log(prefix):
    def wrapper_f(func):
        def wrapper(*args,**kwargs):
            print(f"{prefix} LOG BEFORE",args,kwargs)
            r = func(*args,**kwargs)
            print(f"{prefix} LOG AFTER",r)
            return r
        
        return wrapper
    return wrapper_f

@do_log('MAIN')
def say_hello(name):
    return f"Hello {name}"


def main():
    r = say_hello('Fred')
    print(r)

if __name__=='__main__':
    main()


