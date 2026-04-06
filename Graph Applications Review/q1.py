# generateGraph function takes a list of nodes and list of edges and creates & returns a graph.
# Feel free to modify the function as you like.
def generateGraph(nodes, edges):
    G = {}
    for i in nodes:
        G[i] = []
    for i in edges:
        G[i[0]].append(i[1])
        G[i[1]].append(i[0])
    return G


def marriageLinks(G, family):
    # WRITE YOUR CODE HERE
    pass


def commonLink(G, f1, f2):
    # WRITE YOUR CODE HERE
    pass


def mostcentralfamily(G):
    # WRITE YOUR CODE HERE
    pass
        

#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":
    
    nodes = ['Acciaiuoli', 'Medici', 'Castellani', 'Peruzzi', 'Strozzi', 
             'Barbadori', 'Ridolfi', 'Tornabuoni', 'Albizzi', 'Salviati', 
             'Pazzi', 'Bischeri', 'Guadagni', 'Ginori', 'Lamberteschi']
    
    edges = [
                ('Acciaiuoli', 'Medici'), ('Medici', 'Barbadori'), 
                ('Medici', 'Ridolfi'), ('Medici', 'Tornabuoni'), 
                ('Medici', 'Albizzi'), ('Medici', 'Salviati'), 
                ('Castellani', 'Peruzzi'), ('Castellani', 'Strozzi'), 
                ('Castellani', 'Barbadori'), ('Peruzzi', 'Strozzi'), 
                ('Peruzzi', 'Bischeri'), ('Strozzi', 'Ridolfi'), 
                ('Strozzi', 'Bischeri'), ('Ridolfi', 'Tornabuoni'), 
                ('Tornabuoni', 'Guadagni'), ('Albizzi', 'Ginori'), 
                ('Albizzi', 'Guadagni'), ('Salviati', 'Pazzi'), 
                ('Bischeri', 'Guadagni'), ('Guadagni', 'Lamberteschi')
            ]

    G = generateGraph(nodes, edges)
    print(sorted(marriageLinks(G , "Bischeri")))
    # Should print: ['Guadagni', 'Peruzzi', 'Strozzi']
    
    print(sorted(commonLink(G, "Bischeri" , "Strozzi")))
    # Should print: ['Peruzzi']

    print(mostcentralfamily(G))
    # Should print: Medici

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py