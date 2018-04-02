''' 
This problem refers to an XOR C
'''

def main(fname = "null", key_size=0): 
    ''' 
    XOR Cipher Breaker 
    ''' 
    if fname != "null": 
        with open(fname, 'r') as f: 
            with open("out.txt", "w") as f2: 
                count = 0 
                done = False 
                MAX_VAL = 127
                MAX_VAL_LENGTH = len(str(MAX_VAL))
                L = [int(x) for x in f.read().split(",")]
                key = [0] * int(key_size) 
                while not done: 
                    for key_index in range(len(key)): 
                        key[key_index] += 1
                        if key[key_index] > MAX_VAL: 
                            if key_index == len(key) - 1: 
                                done = True 
                            key[key_index] = 0
                            continue 
                        else:  
                            break 
                    key_repr = ['0'*(MAX_VAL_LENGTH-len(str(x))) + str(x) for x in key]
                    print(f"Key {key_repr}...", end="\r")
                    out = do_xor(L, key)
                    out2 = " "
                    for x in out: 
                        out2 += " " + chr(x) 
                    f2.write(out2)
                    f2.write('\n')

def do_xor(L, key_list):
    output = []
    num_keys = len(key_list)
    counter = 0
    for element in L: 
        output += [element ^ key_list[counter % num_keys]]
        counter += 1          
    return output 
    

if __name__ == "__main__": 
    print("File Name: ")
    fname = input()
    print("Key Size (0 for Unknown)")
    key_size = input() 
    main(fname, key_size) 