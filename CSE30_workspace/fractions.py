# Definition of Fraction class

# Here is the gcd function, as it may well be useful to you.
def gcd(m, n):
    # This is the "without loss of generality" part.
    m, n = (m, n) if m > n else (n, m)
    m, n = abs(m), abs(n)
    return m if n == 0 else gcd(m % n, n)

class Fraction(object):

    def __init__(self, numerator, denominator):
        assert isinstance(numerator, int)
        assert isinstance(denominator, int)
        assert denominator != 0
        # YOUR CODE HERE

        d = gcd(numerator, denominator)

        self.numerator = numerator / d
        self.denominator = denominator / d

        if self.denominator < 0 and self.numerator > 0:
          self.numerator = -1 * self.numerator
          self.denominator = -1 * self.denominator

        if self.denominator < 0 and self.numerator < 0:
          self.numerator = -1 * self.numerator
          self.denominator = -1 * self.denominator

        if self.numerator == 0:
          self.denominator = 1

    def __repr__(self):
        """Pretty print a fraction."""
        return "{}/{}".format(self.numerator, self.denominator)

    ## Here, implement the methods for +, -, *, /, =, and <.
    ## Done quite at leisure, with spaces and all, this can be done in about
    ## 25 lines of code.
    # YOUR CODE HERE


    def __add__(self, other):
      numerator1 = self.numerator * other.denominator
      numerator2 = self.denominator * other.numerator
      num = numerator1 + numerator2
      denom = self.denominator * other.denominator
      return Fraction(int(num), int(denom))

    def __sub__(self, other):
      numerator1 = self.numerator * other.denominator
      numerator2 = self.denominator * other.numerator
      num = numerator1 - numerator2
      denom = self.denominator * other.denominator
      return Fraction(int(num), int(denom))

    def __mul__(self,other):
      return Fraction(int(self.numerator * other.numerator), int( self.denominator * other.denominator))
    
    def __truediv__(self,other):
      return Fraction( int(self.numerator * other.denominator), int(self.denominator * other.numerator))
    
    def __eq__(self, other):
      if (self.numerator == other.numerator and self.denominator == other.denominator):
        return True
      return False

    def __lt__(self, other):
      common_denom = ((self.numerator * other.denominator) - (self.denominator * other.numerator)) / (self.denominator * other.denominator)
      if common_denom < 0 :
        return True
      return False