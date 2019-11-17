from enum import auto, Enum

class ProductionFactory():
    def __init__(self, production_chain=None):
        if production_chain is not None:
            self.chain = production_chain

        self.chain = []

    @property
    def Finish(self):
        result = ''.join(self.chain)
        self.chain = []
        return result

    @property
    def To(self):
        self.chain.append(' -> ')
        return self

    @property
    def Statement(self):
        self.chain.extend(['<', 'Statement', '>'])
        return self

    @property
    def MoreStatements(self):
        self.chain.extend(['<', 'MoreStatements', '>'])
        return self

    @property
    def Conditional(self):
        self.chain.extend(['<', 'Conditional', '>'])
        return self

    @property
    def ConditionalPrime(self):
        self.chain.extend(['<', 'ConditionalPrime', '>'])
        return self

    @property
    def Declarative(self):
        self.chain.extend(['<', 'Declarative', '>'])
        return self

    @property
    def Type(self):
        self.chain.extend(['<', 'Type', '>'])
        return self

    @property
    def Id(self):
        self.chain.extend(['<', 'Id', '>'])
        return self

    @property
    def MoreIds(self):
        self.chain.extend(['<', 'MoreIds', '>'])
        return self

    @property
    def Relop(self):
        self.chain.extend(['<', 'Relop', '>'])
        return self

    @property
    def Expression(self):
        self.chain.extend(['<', 'Expression', '>'])
        return self

    @property
    def Assignment(self):
        self.chain.extend(['<', 'Assignment', '>'])
        return self

    @property
    def ExpressionPrime(self):
        self.chain.extend(['<', 'ExpressionPrime', '>'])
        return self

    @property
    def Term(self):
        self.chain.extend(['<', 'Term', '>'])
        return self

    @property
    def TermPrime(self):
        self.chain.extend(['<', 'TermPrime', '>'])
        return self

    @property
    def Factor(self):
        self.chain.extend(['<', 'Factor', '>'])
        return self

    @property
    def Begin(self):
        self.chain.extend(['<', 'Begin', '>'])
        return self

    @property
    def If(self):
        self.chain.extend(['<', 'If', '>'])
        return self

    @property
    def Then(self):
        self.chain.extend(['<', 'Then', '>'])
        return self

    @property
    def Else(self):
        self.chain.extend(['<', 'Else', '>'])
        return self

    @property
    def Endif(self):
        self.chain.extend(['<', 'Endif', '>'])
        return self

    @property
    def While(self):
        self.chain.extend(['<', 'While', '>'])
        return self

    @property
    def Do(self):
        self.chain.extend(['<', 'Do', '>'])
        return self

    @property
    def Whileend(self):
        self.chain.extend(['<', 'Whileend', '>'])
        return self

    @property
    def End(self):
        self.chain.extend(['<', 'End', '>'])
        return self

    @property
    def GreaterThan(self):
        self.chain.extend(['<', 'GreaterThan', '>'])
        return self

    @property
    def GreaterThanEqual(self):
        self.chain.extend(['<', 'GreaterThanEqual', '>'])
        return self

    @property
    def LessThan(self):
        self.chain.extend(['<', 'LessThan', '>'])
        return self

    @property
    def LessThanEqual(self):
        self.chain.extend(['<', 'LessThanEqual', '>'])
        return self

    @property
    def Equalequal(self):
        self.chain.extend(['<', 'Equalequal', '>'])
        return self

    @property
    def Notequal(self):
        self.chain.extend(['<', 'Notequal', '>'])
        return self

    @property
    def Int(self):
        self.chain.extend(['<', 'Int', '>'])
        return self

    @property
    def Float(self):
        self.chain.extend(['<', 'Float', '>'])
        return self

    @property
    def Bool(self):
        self.chain.extend(['<', 'Bool', '>'])
        return self

    @property
    def Semicolon(self):
        self.chain.extend(['<', 'Semicolon', '>'])
        return self

    @property
    def Comma(self):
        self.chain.extend(['<', 'Comma', '>'])
        return self

    @property
    def Num(self):
        self.chain.extend(['<', 'Num', '>'])
        return self

    @property
    def LeftParenthesis(self):
        self.chain.extend(['<', 'LeftParenthesis', '>'])
        return self

    @property
    def RightParenthesis(self):
        self.chain.extend(['<', 'RightParenthesis', '>'])
        return self

    @property
    def EOF(self):
        self.chain.extend(['<', 'EOF', '>'])
        return self

    @property
    def Addition(self):
        self.chain.extend(['<', 'Addition', '>'])
        return self

    @property
    def Subtraction(self):
        self.chain.extend(['<', 'Subtraction', '>'])
        return self

    @property
    def Multiplication(self):
        self.chain.extend(['<', 'Multiplication', '>'])
        return self

    @property
    def Division(self):
        self.chain.extend(['<', 'Division', '>'])
        return self

    @property
    def Assignequals(self):
        self.chain.extend(['<', 'Assignequals', '>'])
        return self

    @property
    def Epsilon(self):
        self.chain.extend(['<', 'Epsilon', '>'])
        return self

class Terminals(Enum):
    BEGIN = auto()
    IF = auto()
    THEN = auto()
    ELSE = auto()
    ENDIF = auto()
    WHILE = auto()
    DO = auto()
    WHILEEND = auto()
    END = auto()
    GT = auto()
    LT = auto()
    GTE = auto()
    LTE = auto()
    EQUALEQUALS = auto()
    NOTEQUAL = auto()
    INT = auto()
    FLOAT = auto()
    BOOL = auto()
    SEMICOLON = auto()
    COMMA = auto()
    ID = auto()
    NUM = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    EOF = auto()
    ADDITION = auto()
    SUBTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()
    ASSIGNEQUALS = auto()
    EPSILON = auto()


class NonTerminals(Enum):
    STATEMENT = auto()
    MORESTATEMENTS = auto()
    CONDITIONAL = auto()
    CONDITIONAL_PRIME = auto()
    DECLARATIVE = auto()
    TYPES = auto()
    MOREIDS = auto()
    ASSIGNMENT = auto()
    EXPRESSION = auto()
    EXPRESSION_PRIME = auto()
    TERM = auto()
    TERM_PRIME = auto()
    FACTOR = auto()
    RELATIONAL_OPERATOR = auto()
