def main():
    l = [10,98,65,32,47,54,196,5]

    to_find = 47
    found = False
    for i in l:
        print(i)
        if i == to_find:
            found = True
            print("found !!!!!")
            break
    else:
        print('not found !')
    

    if found:
        print("found")
    else:
        print("not found")

    
if __name__=='__main__':
    main()

