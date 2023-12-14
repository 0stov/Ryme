#!/usr/bin/env python
import sys, os
import pronouncing, re

#two words tyme if their final stressed vowel and all following sounds are identical.
def isRyme(word1, word2):
    return re.search(r" ([A-Z]+)$",pronouncing.phones_for_word(word1)[0])[0].strip() == re.search(r" ([A-Z]+)$",pronouncing.phones_for_word(word2)[0])[0].strip()
    
    
def main(argv):
    debug = True
    debug = False
    
    if len(argv) > 1:
        file1_in = argv[1]
  
    else:
        #file1_in = input("please input file path to  file; (If its in the same folder as this program just the name will do) : ")
        pass
    print(isRyme("bin", "shin"))



if __name__ == "__main__":
    main(sys.argv)