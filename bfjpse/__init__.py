from itertools import product
import networkx as nx

def suma(a,b):
  return a+b

def is_hamltonian_cycle(graph, cycle):
  """Checks if cycle is a hamiltonian cycle in graph
  graph is a Networkx graph, and cycle is a list of verticex"""
  n = len(set(cycle))
  if n != graph.order:
    return False
  for i in range(n-1):
    if not graph.has_edge(cycle[i], cycle[i+1]):
      return False
  if not graph.has_edge(cycle[n-1], cycle[0]):
    return False
  return True

def is_hamiltonian(graph):
  vertices=list(graph.nodes())
  if len(vertices) < 3:
    return False
  perms = itertools.permutations(vertices)
  for perm in perms:
    if is_hamltonian_cycle(graph, perm):
      return perm
  return False

def is_proper_coloring(graph, coloring):
  for edge in graph.edges():
    if coloring[edge[0]] == coloring[edge[1]]:
      return False
  return True

def is_3_coloring(graph):
  n = graph.order()
  colorings = product([0,1,2], repeat = n)
  for coloring in colorings:
    if is_proper_coloring(graph, coloring):
      return coloring
  return False

def knapsack_problem(profits,weights , capacity, desired_value ):
    n = len(weights)

    options = [0, 1]

    # Generamos todas las combinaciones
    v = list(itertools.product(options, repeat=n))

   
    for i in range(len(v)):
      current_weight = sum(x * w for x, w in zip(v[i], weights))
      current_profit = sum(x * p for x, p in zip(v[i], profits))
      if current_weight <= capacity and current_profit >= desired_value:
        print("un vector que cumple es:" , v[i])
        print("peso:" , current_weight)
        print("beneficio:" , current_profit)
        break
      return False
  
