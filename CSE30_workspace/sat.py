def has_pos_and_neg(l):
    return len(set(l)) > len({abs(x) for x in l})

### Defining Clauses

class Clause(object):

    def __init__(self, clause):
        """Initializes a clause.  Here, the input clause is either a list or set
        of integers, or is an instance of Clause; in the latter case, a shallow
        copy is made, so that one can modify this clause without modifying the
        original clause.
        Store the list of literals as a frozenset."""
        # YOUR CODE HERE
        if isinstance(clause,Clause):
          self.literals = clause.literals
        else:
          self.literals = frozenset(clause) 

    def __repr__(self):
        return repr(self.literals)

    def __eq__(self, other):
        return self.literals == other.literals

    def __hash__(self):
        """This will be used to be able to have sets of clauses,
        with clause equality defined on the equality of their literal sets."""
        return hash(self.literals)

    def __len__(self):
        return len(self.literals)

    @property
    def istrue(self):
        """A clause is true if it contains both a predicate and its complement."""
        # YOUR CODE HERE
        return has_pos_and_neg(self.literals)

    @property
    def isfalse(self):
        """A clause is false if and only if it is empty."""
        # YOUR CODE HERE
        return True if len(self.literals) == 0 else False

### Exercise: define simplify

def clause_simplify(self, i):
    """Computes the result simplify the clause according to the
    truth assignment i."""
    # YOUR CODE HERE
    if i in self.literals:
      return True
    elif -i in self.literals:
      return Clause(self.literals - {-i})
    else:
      return self
Clause.simplify = clause_simplify

class SAT(object):
  
    def __init__(self, clause_list):
        """clause_list is a list of lists (or better, an iterable of
        iterables), to represent a list or set of clauses."""
        raw_clauses = {Clause(c) for c in clause_list}
        # We do some initial sanity checking.
        # If a clause is empty, then it
        # cannot be satisfied, and the entire problem is False.
        # If a clause is true, it can be dropped.
        self.clauses = set()
        for c in raw_clauses:
            if c.isfalse:
                # Unsatisfiable.
                self.clauses = {c}
                break
            elif c.istrue:
                pass
            else:
                self.clauses.add(c)

    def __repr__(self):
        return repr(self.clauses)

    def __eq__(self, other):
        return self.clauses == other.clauses

### istrue, isfalse, for SAT.

def sat_istrue(self):
    # YOUR CODE HERE
    return len(self.clauses) == 0

def sat_isfalse(self):
    # YOUR CODE HERE
    for x in self.clauses:
      if x.isfalse:
        return True
    return False

SAT.istrue = property(sat_istrue)
SAT.isfalse = property(sat_isfalse)

### Definition of `generate_candidate_assignments`

def sat_generate_candidate_assignments(self):
    """Generates candidate assignments.
    Picks one of the shortest clauses, and return as candidate assignments
    a list of sets, one for each of the literals of the chosen clause."""
    # YOUR CODE HERE
    return min(self.clauses, key=len).literals
    

SAT.generate_candidate_assignments = sat_generate_candidate_assignments

### Exercise: define `apply_assignment`

def sat_apply_assignment(self, assignment):
    """Applies the assignment to every clause.
    If the result of the simplification is True (the boolean True),
    the clause is discarded. The function returns a SAT problem
    consisting of the simplified, non-True, clauses."""
    # YOUR CODE HERE
    final_clauses = []
    for c in self.clauses:
      simplified = c.simplify(assignment)
      if isinstance(simplified, bool) and simplified == True:
        pass
      else:
        final_clauses.append([i for i in simplified.literals])
    return SAT(final_clauses)

SAT.apply_assignment = sat_apply_assignment

### Exercise: define `solve`

def sat_solve(self):
    """Solves a SAT instance.
    First, it checks whether the instance is false (in which case
    it returns False) or true (in which case it returns an empty
    assignment).
    If neither of these applies, generates a list of candidate
    assignments, and for each of them, applies them to the current SAT
    instance, generating a new SAT instance, and solves it.
    If the new SAT instance has a solution, merges it with the assignment,
    and returns it.  If it has no solution, tries the next candidate
    assignment.  If no candidate assignment works, returns False, as
    the SAT problem cannot be satisfied."""
    # YOUR CODE HERE

    if self.istrue:
      return set()
    elif self.isfalse:
      return False
    else:
      candidates = self.generate_candidate_assignments()
      for cand in candidates:
        new_sat = self.apply_assignment(cand)
        solv_sat = new_sat.solve()
        if isinstance(solv_sat, set):
          s = set()
          s.add(cand)
          return solv_sat.union(s)
  

SAT.solve = sat_solve
### Here you can test your code.
s = SAT([[1, 2], [-2, 3], [-3, 4], [-4, 5], [8, -1]])
a = s.solve()
print(a)