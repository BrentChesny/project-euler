import sys
from math import factorial
from collections import defaultdict

sys.setrecursionlimit(1000000)

def is_prime(x):
    """ Returns true if x is a prime number.
    """
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in xrange(3, int(x**0.5)+1, 2):
            if x % i == 0:
                return False
        return True

def gen_primes(limit=None):
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while not limit or q < limit:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def list_primes(limit):
    """ Returns a list of primes smaller than limit.
    """
    sieve = [True] * (limit/2)
    for i in xrange(3,int(limit**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((limit-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,limit/2) if sieve[i]]

def list_divisors(n):
    """ Return a list of all divisors of a number.
    """
    return list(gen_divisors(n))

def gen_divisors(n):
    """ Generate all divisors of a number.
    """
    x = 1
    while x <= n**0.5:
        if n % x == 0:
            yield x
            if x != n/x:
                yield n/x
        x += 1

def list_prime_factors(n):
    """ Return a list of all prime factors of a number.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n /= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def gen_triangle_nums(limit=None):
    """ Generate an infinite sequence of triangle numbers
    """
    n = 1
    while not limit or n < limit:
        yield n*(n+1)/2
        n += 1

def gen_pentagonal_nums(limit=None):
    """ Generate an infinite sequence of pentagonal numbers
    """
    n = 1
    while not limit or n < limit:
        yield n*(3*n-1)/2
        n += 1

def gen_generalized_pentagonal_nums(limit=None):
    """ Generate an infinite sequence of generalized pentagonal numbers
    """
    n = 1
    while not limit or n < limit:
        yield n*(3*n-1)/2
        if n < 0:
            n = (n * -1) + 1
        else:
            n *= -1

def gen_hexagonal_nums(limit=None):
    """ Generate an infinite sequence of hexagonal numbers
    """
    n = 1
    while not limit or n < limit:
        yield n*(2*n-1)
        n += 1

def sum_of_digits(n):
    """ Return the sum of the digits of n
    """
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def is_pandigital(s, n=9, start=1):
    """ Return true if s is a string representation of a 1 to 9 pandigital number.
    """
    return sorted(s) == range(start, n+1)

def n_choose_k(n, k):
    """ Number of ways to choose k items from n.
    """
    return factorial(n) / (factorial(k) * factorial(n-k))

def totient(n):
    result = n
    for p in set(list_prime_factors(n)):
        result *= 1.0 - (1.0/p)
    return int(result)
    
def gen_pythagorean_triples(limit=None):
    c, m = 0, 2
    seen = set()
 
    while not limit or c < limit:
        for n in range(1, m):
            k = 1
            while k*c <= limit:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                triple = tuple(sorted((k*a, k*b, k*c)))

                if triple not in seen:
                    yield triple
                    seen.add(triple)
                k += 1
        m += 1
    
def dijkstra(graph, initial):
	costs = {initial: 0}
	path = {}

	nodes = set(graph.nodes)

	while nodes:
		min_node = None
		for node in nodes:
			if node in costs:
				if min_node is None:
					min_node = node
				elif costs[node] < costs[min_node]:
					min_node = node

		if min_node is None:
			break

		nodes.remove(min_node)
		current_weight = costs[min_node]

		for edge in graph.edges[min_node]:
			try:
				weight = current_weight + graph.distances[(min_node, edge)]
			except:
				continue
			if edge not in costs or weight < costs[edge]:
				costs[edge] = weight
				path[edge] = min_node

	return costs, path

class Memoize:
    """ Memoization wrapper class.
    """
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

class MillerRabin(object):
    """Wrapper for the Miller-Rabin primality test."""
    def __init__(self):
        super(MillerRabin, self).__init__()
        self._known_primes = [2, 3]

    def _try_composite(self, a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n  is definitely composite

    def is_prime(self, n, _precision_for_huge_n=16):
        if n in self._known_primes or n in (0, 1):
            return True
        if any((n % p) == 0 for p in self._known_primes):
            return False
        d, s = n - 1, 0
        while not d % 2:
            d, s = d >> 1, s + 1
        # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
        if n < 1373653:
            return not any(self._try_composite(a, d, n, s) for a in (2, 3))
        if n < 25326001:
            return not any(self._try_composite(a, d, n, s) for a in (2, 3, 5))
        if n < 118670087467:
            if n == 3215031751:
                return False
            return not any(self._try_composite(a, d, n, s) for a in (2, 3, 5, 7))
        if n < 2152302898747:
            return not any(self._try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
        if n < 3474749660383:
            return not any(self._try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
        if n < 341550071728321:
            return not any(self._try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
        # otherwise
        return not any(self._try_composite(a, d, n, s)
                       for a in self._known_primes[:_precision_for_huge_n])
                       
class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)
		self.distances = {}

	def add_node(self, value):
		self.nodes.add(value)

	def add_edge(self, from_node, to_node, distance):
		self.edges[from_node].append(to_node)
		self.edges[to_node].append(from_node)
		self.distances[(from_node, to_node)] = distance
