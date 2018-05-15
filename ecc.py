class FieldElement:

    def __init__(self, num, prime):
        self.num = num
        self.prime = prime
        if self.num >= self.prime or self.num < 0:
            error = 'Num {} not in field range 0 to {}'.format(
                self.num, self.prime-1)
            raise RuntimeError(error)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        if other is None:
            return True
        return self.num != other.num or self.prime != other.prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __add__(self, other):
        if self.prime != other.prime:
            raise RuntimeError('Primes must be the same')
        # self.num and other.num are the actual values
        # self.prime is what you'll need to mod against
        # You need to return an element of the same class
        # use: self.__class__(num, prime)
        raise NotImplementedError

    def __sub__(self, other):
        if self.prime != other.prime:
            raise RuntimeError('Primes must be the same')
        # self.num and other.num are the actual values
        # self.prime is what you'll need to mod against
        # You need to return an element of the same class
        # use: self.__class__(num, prime)
        raise NotImplementedError

    def __mul__(self, other):
        if self.prime != other.prime:
            raise RuntimeError('Primes must be the same')
        # self.num and other.num are the actual values
        # self.prime is what you'll need to mod against
        # You need to return an element of the same class
        # use: self.__class__(num, prime)
        raise NotImplementedError

    def __pow__(self, n):
        # remember fermat's little theorem:
        # self.num**(p-1) % p == 1
        # you might want to use % operator on n
        raise NotImplementedError

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise RuntimeError('Primes must be the same')
        # self.num and other.num are the actual values
        # self.prime is what you'll need to mod against
        # use fermat's little theorem:
        # self.num**(p-1) % p == 1
        # this means:
        # 1/n == pow(n, p-2, p)
        # You need to return an element of the same class
        # use: self.__class__(num, prime)
        raise NotImplementedError
