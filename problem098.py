from collections import defaultdict
from math import sqrt
from itertools import combinations

def squares_of_len(word):
    n = len(word)
    x = int(sqrt(10**(n-1))) + 1
    squares = set()
    while x*x < 10**n:
        squares.add(x*x)
        x += 1
    return squares
    
def find_mapping(word, square):
    mapping = dict()
    sq = str(square)
    
    for c, v in zip(word, sq):
        if (c not in mapping or mapping[c] == v) and v not in mapping.values():
            mapping[c] = v
        else:
            return None
    return mapping
    
def check_mapping(mapping, word, squares):
    sq = int(''.join(mapping[c] for c in word))
    if sq in squares:
        return sq
    

def solve():
    words = open('resources/p042_words.txt').readline().strip().split(',')
    words = map(lambda x: x[1:-1], words)
    anagrams = defaultdict(list)
    
    for w in words:
        anagrams[tuple(sorted(w))].append(w)
        
    anagram_pairs = [pair for k, v in anagrams.iteritems() if len(v) > 1 for pair in combinations(v, 2)]
    
    result = []
    for word1, word2 in anagram_pairs:
        squares = squares_of_len(word1)
        for sq in squares:
            mapping = find_mapping(word1, sq)
            if mapping != None and check_mapping(mapping, word2, squares) != None:
                result.append(sq)
                result.append(check_mapping(mapping, word2, squares))
    
    return max(result)
        

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
