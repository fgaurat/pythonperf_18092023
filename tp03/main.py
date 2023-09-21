import traceback
# ZeroDivisionError => UpperCamelCase
# zeroDivisionError => camelCase
# zero_division_error => snake_case
# zero-division-error => kebab-case


class DivBy12Error(Exception):

    def __init__(self,) -> None:
        super().__init__("Division par 12 !!!!!")

def div(a,b):
    if b==12:
        # raise Exception('Division par 12 !!!!!')
        raise DivBy12Error()
    
    return a/b

def call_div(a,b):
    try:
        print("open log")
        r = div(a,b)
    finally:    
        print("close log")
    
    return r

def main():
    try:
        a=2
        # b=int(input("Valeur de b: "))
        b= 12
        c=call_div(a,b)
        print(c)
    except ZeroDivisionError as e:
        traceback.print_exc()
        print(e)
    except TypeError as e:
        traceback.print_exc()
        print(e)
    except ValueError as e:
        traceback.print_exc()
        print(e)
    except DivBy12Error as e:
        traceback.print_exc()
        print(e)
    except Exception as e:
        traceback.print_exc()
        print(e)
    else:
        print("pas d'erreur")
    print("après")

if __name__=='__main__':
    main()
