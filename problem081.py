from common import Graph, dijkstra

def solve():
    matrix = [map(int, line.strip().split(',')) for line in open('resources/p081_matrix.txt')]
    
    g = Graph()
    g.add_node('source')
    g.add_node('target')
    
    for r in xrange(len(matrix)):
        for c in xrange(len(matrix[r])):
            g.add_node((r, c))
            
    for r in xrange(len(matrix)):
        for c in xrange(len(matrix[r])):
            if r > 0:
                g.add_edge((r-1,c), (r,c), matrix[r][c])
            if c > 0:
                g.add_edge((r,c-1), (r,c), matrix[r][c])
    g.add_edge('source', (0, 0), matrix[0][0])
    g.add_edge((len(matrix)-1, len(matrix[0])-1), 'target', 0)
    
    costs, _ = dijkstra(g, 'source')

    return costs['target']
    
def main():
    print 'Solution:', solve()

if __name__ == '__main__':
    main()
