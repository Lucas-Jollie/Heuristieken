from collections import deque
import heapq

start = [5,4,3,2,1]
solution = [1,2,3,4,5]



__all__ = ['State', 'path_cost', 'greedy_best_first', 'beam', 'astar']

class State:
  """
  Interface for state of environment, and state transitions.
  """
  def successors(self):
    """
    Get iterable of successor states.
    """
    raise NotImplementedError

  def cost(self, other):
    """
    Cost of state self -> other (only needed for uniform_cost_search).
    """
    raise NotImplementedError

  def is_goal(self):
    """
    True iff self is a goal state.
    """
    solution = [1,2,3,4,5]

  def heuristic(start):
    """
    Estimated distance from self to goal (or other heuristic).
    """
    numberCorrect = 0
    for i in range(len(start)):
        if (start[i] == i + 1):
            numberCorrect += 1
    return numberCorrect


def path_cost(path):
  """
  Sum of edge costs for a given path (iterable) of states.
  """
  return sum([path[i].cost(path[i+1]) for i in xrange(len(path)-1)])


def flatten(L):
  """
  Given linked list of the form [[[[],1],2],3], return [1,2,3].
  """
  ans = []
  while len(L) > 0:
    ans.append(L[-1])
    L = L[0]
  return ans[::-1]


def greedy_best_first(initial_state, graph=False):
  """
  Greedy best-first search.
  """
  return beam(initial_state, None, graph)


def beam(initial_state, beam_width=None, graph=False):
  """
  Beam search: BFS, expand beam_width best nodes at each layer.
  """
  q = [(initial_state.heuristic(start), ((),initial_state))]
  if not graph:
    while True:
      (cost, path) = heapq.heappop(q)
      state = path[-1]
      if state.is_goal():
        return flatten(path)
      for x in state.successors():
        heapq.heappush(q, (x.heuristic(), (path, x)))
      if beam_width is not None:
        q = q[:beam_width]
  else:
    visited = set()
    while True:
      (cost, path) = heapq.heappop(q)
      state = path[-1]
      if not state in visited:
        visited.add(state)
        if state.is_goal():
          return flatten(path)
        for x in state.successors():
          if x not in visited:
            heapq.heappush(q, (x.heuristic(), (path, x)))
      if beam_width is not None:
        q = q[:beam_width]

print beam(start,2)

def astar(initial_state, graph=False):
  """
  A* search.

  For A* to be optimal in tree search mode, the state's heuristic()
  must be <= the cost of the minimal path to the goal node.  For A* to
  be optimal in graph search mode, for all states a and successors b:

    0 <= a.heuristic() - b.heuristic() <= a.cost(b)

  It suffices for vertices to be in a normed vector space, with
  a.cost(b) == norm(a - b) and a.heuristic() == norm(a - goal).
  """
  q = [(initial_state.heuristic(), 0, ((),initial_state))]
  if not graph:
    while True:
      (total, precost, path) = heapq.heappop(q)
      state = path[-1]
      if state.is_goal():
        return flatten(path)
      for x in state.successors():
        precost2 = precost + state.cost(x)
        heapq.heappush(q, (precost2 + x.heuristic(), precost2,
                           (path, x)))
  else:
    visited = set()
    while True:
      (total, precost, path) = heapq.heappop(q)
      state = path[-1]
      if not state in visited:
        visited.add(state)
        if state.is_goal():
          return flatten(path)
        for x in state.successors():
          if x not in visited:
            precost2 = precost + state.cost(x)
            heapq.heappush(q, (precost2 + x.heuristic(), precost2,
                               (path, x)))
