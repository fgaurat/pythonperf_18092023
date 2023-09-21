

def make_inc(inc_value):
    print(f"make_inc({inc_value})")
    def inc_function(value):
        print(f"inc_function({value}) / {inc_value}")
        return inc_value+value
    def mult_function(value):
        print(f"mult_function({value}) * {inc_value}")
        return inc_value*value

    return inc_function,mult_function

def main():
    do_inc,do_mult = make_inc(2)
    v = do_inc(3) 
    print(v) #5
    v = do_inc(12) 
    print(v)
    v = do_inc(30) 
    print(v)

if __name__=='__main__':
    main()
