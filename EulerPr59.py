import time 

class XorBreaker(): 
    def __init__(self):
        #TODO  
        ''' Sets the initial values for the XOR Cipher Breaker ''' 
        self.key_size = 0 
        self.min_val = 97 
        self.max_val = 122 
        self.fname = "null"

def main(fname = "null", key_size=0, min_val=97, max_val=122): 
    ''' 
    XOR Cipher Breaker 
    ''' 
    open('out.txt', 'w').close() 

    if fname != "null": 
        with open(fname, 'r') as f: 
            with open("out.txt", "w") as f2: 
                st = time.time() 

                count = 0 
                matches = 0 
                done = False 
                if min_val == -1: 
                    MIN_VAL = 97
                else: 
                    MIN_VAL = min_val
                
                if max_val == -1: 
                    MAX_VAL = 122
                else: 
                    MAX_VAL = max_val

                MAX_VAL_LENGTH = len(str(MAX_VAL))
                L = [int(x) for x in f.read().split(",")]
                key = [MIN_VAL] * int(key_size) 
                
                while not done: 
                    
                    count += 1

                    for key_index in range(len(key)): 
                        key[key_index] += 1
                        if key[key_index] > MAX_VAL: 
                            if key_index == len(key) - 1: 
                                done = True 
                            key[key_index] = MIN_VAL
                            continue 
                        else:  
                            break 
                    
                    key_repr = ['0'*(MAX_VAL_LENGTH-len(str(x))) + str(x) for x in key]

                    dif = time.time() - st  
                    try:
                        thing = round(count / dif) 
                    except: 
                        thing = "NaN"

                    output = do_xor(L, key)
                    out = "".join([chr(x) for x in output])
                    matches += 1 
                    print(f"Key {key_repr}... {thing} Keys Per Second...{count} counts {matches} matches", end="\r")

                    f2.write(out)
                    f2.write('\n')
        
    print("\nDone!")

def check_alpha_num(L): 
    ''' 
    Takes a list where each element is number. 
    Then, checks if the number is in the correct range for 'a->z' in the ASCII table 
    '''
    for element in L: 
        if element < 32 or element > 127: 
            return False 
    return True 
    
def do_xor(L, key_list):
    counter = 0
    output = []
    num_keys = len(key_list)
    output = [L[el_index] ^ key_list[el_index % num_keys] for el_index in range(len(L))]
    return output 

if __name__ == "__main__": 
    fname = input("File Name: ")
    key_size = input("Key Size (Enter for Default): ") 

    while True: 
        try: 
            min_val = input("Min ASCII Value (Enter for Default): ")
            if min_val.strip() == "": 
                min_val = -1  
            else: 
                min_val = int(min_val)
            break 
        except: 
            print("Must be a number")
            
    while True: 
        try: 
            max_val = input("Min ASCII Value (Enter for Default): ")
            if max_val.strip() == "": 
                max_val = -1  
            else: 
                max_val = int(max_val)
            break 
        except: 
            print("Must be a number")
            
    breaker = XorBreaker()

    main(fname, key_size, min_val, max_val) 