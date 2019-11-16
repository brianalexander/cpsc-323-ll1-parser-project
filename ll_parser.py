from enum import auto, Enum


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
    END = auto()
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


# parse table
table = [[1, -1, 0, -1, -1, -1],
         [-1, -1, 2, -1, -1, -1]]

RULES = {
    'S->A': [NonTerminals.ASSIGNMENT],
    'S->D': [NonTerminals.DECLARATIVE],
    'S->IF': [Terminals.IF, NonTerminals.CONDITIONAL,
              Terminals.THEN, NonTerminals.STATEMENT,
              Terminals.ELSE, NonTerminals.STATEMENT,
              Terminals.ENDIF],
    'S->WHILE': [Terminals.WHILE, NonTerminals.CONDITIONAL,
                 Terminals.DO, NonTerminals.STATEMENT,
                 Terminals.WHILEEND],
    'S->BEGIN': [Terminals.BEGIN, NonTerminals.STATEMENT,
                 NonTerminals.MORESTATEMENTS, Terminals.END],
    'Ms->;_S_Ms': [Terminals.SEMICOLON, NonTerminals.STATEMENT, NonTerminals.MORESTATEMENTS],
    'Ms->Epsilon': [Terminals.EPSILON],
    'C->E_R_E': [NonTerminals.EXPRESSION, NonTerminals.RELATIONAL_OPERATOR,
                 NonTerminals.EXPRESSION],
    'C->E': [NonTerminals.EXPRESSION],
    'D->Ty_id_Mi_;': [NonTerminals.TYPES, Terminals.ID,
                      NonTerminals.MORESTATEMENTS, Terminals.SEMICOLON],
    'D->Epsilon': [Terminals.EPSILON],
    'Ty->int': [Terminals.INT],
    'Ty->float': [Terminals.FLOAT],
    'Ty->bool': [Terminals.BOOL],
    'Mi->,id_Mi': [Terminals.COMMA, Terminals.ID, NonTerminals.MOREIDS],
    'Mi->Epsilon': [Terminals.EPSILON],
    'A->id_=_C_;': [Terminals.ID, Terminals.ASSIGNEQUALS,
                    NonTerminals.CONDITIONAL, Terminals.SEMICOLON],
    'R->>': [Terminals.LT],
    'R-><': [Terminals.GT],
    'R->>=': [Terminals.LTE],
    'R-><=': [Terminals.GTE],
    'R->==': [Terminals.EQUALEQUALS],
    'R-><>': [Terminals.NOTEQUAL],
    'E->T_Ep': [NonTerminals.TERM, NonTerminals.EXPRESSION_PRIME],
    'Ep->+_T_Ep': [Terminals.ADDITION, NonTerminals.TERM,
                   NonTerminals.EXPRESSION_PRIME],
    'Ep->-_T_Ep': [Terminals.SUBTRACTION, NonTerminals.TERM,
                   NonTerminals.EXPRESSION_PRIME],
    'Ep->Epsilon': [Terminals.EPSILON],
    'T->F_Tp': [NonTerminals.FACTOR, NonTerminals.TERM_PRIME],
    'Tp->*_F_Tp': [Terminals.MULTIPLICATION, NonTerminals.FACTOR,
                   NonTerminals.TERM_PRIME],
    'Tp->/_F_Tp': [Terminals.DIVISION, NonTerminals.FACTOR,
                   NonTerminals.TERM_PRIME],
    'Tp->Epsilon': [Terminals.EPSILON],
    'F->(_E_)': [Terminals.LEFT_PAREN, NonTerminals.EXPRESSION,
                 Terminals.RIGHT_PAREN],
    'F->id': [Terminals.ID],
    'F->num': [Terminals.NUM]
}

stack = [Terminals.END, NonTerminals.MORESTATEMENTS]


# def lexical_analysis(inputstring):
#     print('Lexical analysis')
#     tokens = []
#     for c in inputstring:
#         if c == '+':
#             tokens.append(T_PLUS)
#         elif c == '(':
#             tokens.append(T_LPAR)
#         elif c == ')':
#             tokens.append(T_RPAR)
#         elif c == 'a':
#             tokens.append(T_A)
#         else:
#             tokens.append(T_INVALID)
#     tokens.append(T_END)
#     print(tokens)
#     return tokens


def syntactic_analysis(tokens):
    print('Syntactic analysis')
    position = 0
    while len(stack) > 0:
        svalue = stack.pop()
        token = tokens[position]
        if isinstance(svalue, Terminals):
            if svalue == token:
                position += 1
                print('pop', svalue)
                if token == Terminals.END:
                    print('input accepted')
            else:
                print('bad term on input:', token)
                break
        elif isinstance(svalue, NonTerminals):
            print('svalue', svalue, 'token', token)
            rule = table[svalue][token]
            print('rule', rule)
            for r in reversed(RULES[rule]):
                stack.append(r)
        print('stack', stack)


inputstring = '(a+a)'
# syntactic_analysis(lexical_analysis(inputstring))
