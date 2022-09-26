class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        """
        Rtorna representacao textual
        no formato (x, y)
        """
        repr = f'({self.x},{self.y})'
        return repr
    
    def __add__(self, other):
        """
        Retorna a soma de dois vetores
        AA soma de dois vetores e feita da seguinte forma
        v1 + v2 = v1.x + v2.x. v1.y + v2.y
        """
        x = self.x + other.x
        y = self.y + other.y
        
        return vector(x, y)
    
    def move(self, other):
        """
        Movimenta o vector tomando como referencia
        o parametro other
        """
        self.x = self.x + other.x
        self.y = self.y + other.y
