from collections import defaultdict
from math import log10 
import time 

class XorBreaker(): 
    def __init__(self):
        ''' Sets the initial values for the XOR Cipher Breaker ''' 
        self.key_size = 0 
        self.min_val = 97 
        self.max_val = 122 
        self.fname = "null"
        # Taken from https://en.wikipedia.org/wiki/Letter_frequency
        self.character_frequencies_dict = {"a": .08167, "b": .01492, "c": .02782, "d": .04253, "e": .12702,
                              "f": .02228, "g": .02015, "h": .06094, "i": .06966, "j": .00153,
                              "k": .00772, "l": .04025, "m": .02406, "n": .06749, "o": .07507,
                              "p": .01929, "q": .00095, "r": .05987, "s": .06327, "t": .09056,
                              "u": .02758, "v": .00978, "w": .0236, "x": .00150, "y": .01974, 
                              "z": .00074}

        # Create a default dict and copy over the characters from the 
        # Character frequencies dictionary 
        self.character_frequencies = defaultdict(int)
        for key in character_frequencies_dict: 
            self.character_frequencies[key] = character_frequencies_dict[key]


# Taken from https://en.wikipedia.org/wiki/Letter_frequency
character_frequencies_dict = {"a": .08167, "b": .01492, "c": .02782, "d": .04253, "e": .12702,
                              "f": .02228, "g": .02015, "h": .06094, "i": .06966, "j": .00153,
                              "k": .00772, "l": .04025, "m": .02406, "n": .06749, "o": .07507,
                              "p": .01929, "q": .00095, "r": .05987, "s": .06327, "t": .09056,
                              "u": .02758, "v": .00978, "w": .0236, "x": .00150, "y": .01974, 
                              "z": .00074}

character_frequencies = defaultdict(int)
for key in character_frequencies_dict: 
    character_frequencies[key] = character_frequencies_dict[key]
MAX_ASCII_RANGE = 500 

def main(fname = "null", key_size_min=0, key_size_max=3, min_val=97, max_val=122): 
    ''' 
    XOR Cipher Breaker for ASCII text.
    Takes in filename for input text, the keysize, and the 
    minimum and maximum ascii values to check for the
    key 
    ''' 
    open('out.txt', 'w').close() 

    # TODO: catch error where file does not exist
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

                # Go through all possible key sizes
                for key_size in range(key_size_min, key_size_max, 1):

                    key = [MIN_VAL] * key_size
                    
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


def compare_probabilities(): 
    ''' 
    Calculate the probability of each string of text occuring, 
    and then compare them 
    ''' 
    count = 0 
    prob_list = [] 
    with open("out.txt", "r") as f:
        text = f.readlines()
        for line in text: 
            print(f"Count: {count}", end="\r")
            prob_list += [(calculate_probality(line), count)]
            count += 1     
        
    print("\n")

    with open('probabilities.txt', 'w') as f: 
        f.write(str(sorted(prob_list)))
            

def calculate_probality(s): 
    ''' 
    Based on the frequencies of characters count 
    in the english language, figures out the probabilit
    of a particular string being generated 

    Note: these probabilities should only be used for 
    comparisons
    ''' 
    # First, iterate through all of the characters x`W`
    # in the list 
    char_count = defaultdict(int)
    for char in s: 
        char_count[char] += 1 
    
    probability = 0 
    # Then, calculate the probability by iterating 
    # through the dictionary keys 
    for key in char_count.keys(): 

        char_probability = character_frequencies[key]
        if char_probability == 0: 
            char_probability = 1

        probability += char_count[key]*log10(char_probability) 

    return probability

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
    '''
    Goes through each element in the input list and XORs it with the key.
    If the list is longer than the key, the key will be repeadted as
    necessary.     
    '''
    counter = 0
    output = []
    num_keys = len(key_list)
    output = [L[el_index] ^ key_list[el_index % num_keys] for el_index in range(len(L))]
    return output 

if __name__ == "__main__": 
    fname = input("File Name: ")
    while True:
        try: 
            key_size = int(input("Key Size (Enter for Default): ")) 
            if key_size.strip() == "": 
                key_size = 3
            elif key_size < 0: 
                raise ValueError()
        except: 
            print("Must be a number")

    while True: 
        try: 
            min_val = input("Min ASCII Value (Enter for Default): ")
            if min_val.strip() == "": 
                min_val = -1  
            else: 
                min_val = int(min_val)
                # ASCII key codes must be positive 
                if min_val < 0:
                    raise ValueError() 
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
                if max_val > MAX_ASCII_RANGE: 
                    raise ValueError()
            break 
        except: 
            print("Must be a number")
            
    breaker = XorBreaker()
    main(fname, key_size, min_val, max_val) 
    compare_probabilities() 