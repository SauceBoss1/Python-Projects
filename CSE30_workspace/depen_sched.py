from collections import defaultdict
import networkx as nx # Library for displaying graphs.
import matplotlib.pyplot as plt

class AND_OR_Scheduler(object):
  def __init__(self):
    self.tasks = set()

    self.and_predecessors = defaultdict(set)
    self.or_predecessors = defaultdict(set)

    self.successors = defaultdict(set)

    self.completed_tasks = set()
  
  def add_and_task(self, t, dependencies):
    """Adds an AND task t with given dependencies."""
    # YOUR CODE HERE
    self.tasks.update(t, dependencies)
    self.and_predecessors[t] = set(dependencies)
    for u in dependencies:
      self.successors[u] = set(t)
  
  def add_or_task(self, t, dependencies):
    """Adds an OR task t with given dependencies."""
    # YOUR CODE HERE
    self.tasks.update(t, dependencies)
    self.or_predecessors[t] = set(dependencies)
    for u in dependencies:
      self.successors[u] = set(t)

  @property
  def done(self):
    return self.completed_tasks == self.tasks
  
  @property
  def available_tasks(self):
    """Returns the set of tasks that can be done in parallel.
    A task can be done if:
    - It is an AND task, and all its predecessors have been completed, or
    - It is an OR task, and at least one of its predecessors has been completed.
    And of course, we don't return any task that has already been
    completed."""
    # YOUR CODE HERE

    uncompleted_tasks = self.tasks - self.completed_tasks
    final_tasks = set()
    '''
    PSUEDOCODE:

    '''
    for u in uncompleted_tasks:
      if u in self.and_predecessors and self.and_predecessors[u].issubset(self.completed_tasks):
        final_tasks.add(u)
      elif u in self.or_predecessors:
        for v in self.or_predecessors[u]:
          if v in self.completed_tasks:
            final_tasks.add(u)
      elif u not in self.or_predecessors and u not in self.and_predecessors:
        final_tasks.add(u)
    return final_tasks

    # for u in self.tasks:
    #   if u in self.and_predecessors and u not in self.completed_tasks:
    #     completed = True
    #     for v in self.and_predecessors[u]:
    #       if v not in self.completed_tasks and (self.and_predecessors[v] == set()):
    #         final_tasks.add(v)
    #         completed = False
    #     if completed:
    #       final_tasks.add(u)
    #   elif u not in self.completed_tasks:
    #     if u not in self.completed_tasks and (self.or_predecessors[u] == set()):
    #       final_tasks.add(u)
    #     for x in self.or_predecessors[u]:
    #       if x in self.completed_tasks:
    #         final_tasks.add(u)
    #       if x not in self.completed_tasks:
    #         final_tasks.add(x)
    
    return final_tasks

  def mark_completed(self, t):
    """Marks the task t as completed, and returns the additional
    set of tasks that can be done (and that could not be
    previously done) once t is completed."""
    # YOUR CODE HERE
    new_tasks = set()
    self.completed_tasks.add(t)
    for u in self.successors[t]:
      if u in self.and_predecessors:
        completed = True
        for v in self.and_predecessors[u]:
          if v not in self.completed_tasks:
            completed = False
        if completed:
          new_tasks.add(u)
      elif u in self.or_predecessors:
        for v in self.or_predecessors[u]:
          if v in self.completed_tasks and u not in self.completed_tasks:
            new_tasks.add(u)
    return new_tasks

  def show(self):
    """You can use the nx graph to display the graph.  You may want to ensure
    that you display AND and OR nodes differently."""
    # YOUR CODE HERE
    g = nx.DiGraph()
    g.add_nodes_from(self.tasks)
    g.add_edges_from([(u, v) for u in self.tasks for v in self.successors[u]])
    node_colors = []
    for v in self.tasks:
      if v in self.completed_tasks:
        node_colors.append('green')
      elif v not in self.completed_tasks and v in self.and_tasks:
        node_colors.append('blue')
      elif v not in self.completed_tasks and v in self.or_tasks:
        node_colors.append('yellow')
      else:
        node_colors.append('red')
    #node_colors = ''.join([('g' if v in self.completed_tasks else 'r') for v in self.tasks])
    nx.draw(g, with_labels=True, node_color=node_colors)
    plt.show()

s = AND_OR_Scheduler()
s.add_and_task('a', ['b', 'c'])
s.add_or_task('b', ['b1', 'b2'])
s.add_or_task('c', ['c1', 'c2'])
r = s.mark_completed('b1')
print(s.available_tasks, {'b', 'b2', 'c1', 'c2'})