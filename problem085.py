from operator import itemgetter

TARGET = 2000000

def num_rectangles(size_x, size_y):
    total = 0
    for x in xrange(1, size_x + 1):
        total += (size_x - x + 1)
    return total * (size_y * (size_y+1)/2)
            

def solve():
    d = dict()
    for x in xrange(1, 1000):
        for y in xrange(x, 1000):
            d[(x, y)] = abs(TARGET - num_rectangles(x, y))
    
    x, y = min(d.iteritems(), key=itemgetter(1))[0]
    return x * y
    

def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
