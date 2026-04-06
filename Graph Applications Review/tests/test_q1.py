import pytest
from q1 import *

q1_testcases  = [
    [
        ['Acciaiuoli', 'Medici', 'Castellani', 'Peruzzi', 'Strozzi', 
         'Barbadori', 'Ridolfi', 'Tornabuoni', 'Albizzi', 'Salviati',
         'Pazzi', 'Bischeri', 'Guadagni', 'Ginori', 'Lamberteschi'], 
        [
            ('Acciaiuoli', 'Medici'), ('Medici', 'Barbadori'), ('Medici', 'Ridolfi'), 
            ('Medici', 'Tornabuoni'), ('Medici', 'Albizzi'), ('Medici', 'Salviati'), 
            ('Castellani', 'Peruzzi'), ('Castellani', 'Strozzi'), ('Castellani', 'Barbadori'), 
            ('Peruzzi', 'Strozzi'), ('Peruzzi', 'Bischeri'), ('Strozzi', 'Ridolfi'), 
            ('Strozzi', 'Bischeri'), ('Ridolfi', 'Tornabuoni'), ('Tornabuoni', 'Guadagni'), 
            ('Albizzi', 'Ginori'), ('Albizzi', 'Guadagni'), ('Salviati', 'Pazzi'), 
            ('Bischeri', 'Guadagni'), ('Guadagni', 'Lamberteschi')
        ],
        "Bischeri",
        "Bischeri",
        "Strozzi",
        ['Guadagni', 'Peruzzi', 'Strozzi'],
        ['Peruzzi'],
        "Medici"
    ]
]


@pytest.mark.parametrize("nodes, edges, node1_ml, node1_cl, node2_cl, o1, o2, o3",q1_testcases)
def test_q1(nodes, edges, node1_ml, node1_cl, node2_cl, o1, o2, o3):
    G = generateGraph(nodes, edges)
    assert sorted(marriageLinks(G , node1_ml)) == o1
    print(sorted(commonLink(G, node1_cl, node2_cl))) == o2
    print(mostcentralfamily(G)) == o3