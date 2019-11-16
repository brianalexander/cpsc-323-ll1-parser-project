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


# parse table
table = {
    NonTerminals.STATEMENT: {
        Terminals.BEGIN: 'S->begin',
        Terminals.IF: 'S->if',
        Terminals.THEN: None,
        Terminals.ELSE: 'S->Epsilon',
        Terminals.ENDIF: 'S->Epsilon',
        Terminals.WHILE: 'S->while',
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: 'S->D',
        Terminals.FLOAT: 'S->D',
        Terminals.BOOL: 'S->D',
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 'S->A',
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.MORESTATEMENTS: {
        Terminals.BEGIN: "Ms->S_Ms",
        Terminals.IF: "Ms->S_Ms",
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: "Ms->S_Ms",
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: "Ms->Epsilon",
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: "Ms->S_Ms",
        Terminals.FLOAT: "Ms->S_Ms",
        Terminals.BOOL: "Ms->S_Ms",
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: "Ms->S_Ms",
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: "Ms->Epsilon",
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.CONDITIONAL: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 'C->E_Cp',
        Terminals.NUM: 'C->E_Cp',
        Terminals.LEFT_PAREN: 'C->E_Cp',
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.CONDITIONAL_PRIME: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: 'Cp->Epsilon',
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: 'Cp->Epsilon',
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 'Cp->R_E',
        Terminals.LT: 'Cp->R_E',
        Terminals.GTE: 'Cp->R_E',
        Terminals.LTE: 'Cp->R_E',
        Terminals.EQUALEQUALS: 'Cp->R_E',
        Terminals.NOTEQUAL: 'Cp->R_E',
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 'Cp->Epsilon',
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.DECLARATIVE: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: 'D->Ty_id_Mi_;',
        Terminals.FLOAT: 'D->Ty_id_Mi_;',
        Terminals.BOOL: 'D->Ty_id_Mi_;',
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.TYPES: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: 'Ty->int',
        Terminals.FLOAT: 'Ty->float',
        Terminals.BOOL: 'Ty->bool',
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.MOREIDS: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 'Mi->Epsilon',
        Terminals.COMMA: 'Mi->,_id_Mi',
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.ASSIGNMENT: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 'A->id_=_C_;',
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.EXPRESSION: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 'E->T_Ep',
        Terminals.NUM: 'E->T_Ep',
        Terminals.LEFT_PAREN: 'E->T_Ep',
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.EXPRESSION_PRIME: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: 'Ep->Epsilon',
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: 'Ep->Epsilon',
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 'Ep->Epsilon',
        Terminals.LT: 'Ep->Epsilon',
        Terminals.GTE: 'Ep->Epsilon',
        Terminals.LTE: 'Ep->Epsilon',
        Terminals.EQUALEQUALS: 'Ep->Epsilon',
        Terminals.NOTEQUAL: 'Ep->Epsilon',
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 'Ep->Epsilon',
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: 'Ep->Epsilon',
        Terminals.EOF: None,
        Terminals.ADDITION: 'Ep->+_T_Ep',
        Terminals.SUBTRACTION: 'Ep->-_T_Ep',
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.TERM: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 'T->F_Tp',
        Terminals.NUM: 'T->F_Tp',
        Terminals.LEFT_PAREN: 'T->F_Tp',
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.TERM_PRIME: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: 'Tp->Epsilon',
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: 'Tp->Epsilon',
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 'Tp->Epsilon',
        Terminals.LT: 'Tp->Epsilon',
        Terminals.GTE: 'Tp->Epsilon',
        Terminals.LTE: 'Tp->Epsilon',
        Terminals.EQUALEQUALS: 'Tp->Epsilon',
        Terminals.NOTEQUAL: 'Tp->Epsilon',
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 'Tp->Epsilon',
        Terminals.COMMA: None,
        Terminals.ID: 'Tp->Epsilon',
        Terminals.NUM: 'Tp->Epsilon',
        Terminals.LEFT_PAREN: 'Tp->Epsilon',
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: 'Tp->Epsilon',
        Terminals.SUBTRACTION: 'Tp->Epsilon',
        Terminals.MULTIPLICATION: 'Tp->*_F_Tp',
        Terminals.DIVISION: 'Tp->/_F_Tp',
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.FACTOR: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 'F->id',
        Terminals.NUM: 'F->num',
        Terminals.LEFT_PAREN: 'F->(_E_)',
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
    NonTerminals.RELATIONAL_OPERATOR: {
        Terminals.BEGIN: None,
        Terminals.IF: None,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 'R->>',
        Terminals.LT: 'R-><',
        Terminals.GTE: 'R->>=',
        Terminals.LTE: 'R-><=',
        Terminals.EQUALEQUALS: 'R->==',
        Terminals.NOTEQUAL: 'R-><>',
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: None,
        Terminals.SUBTRACTION: None,
        Terminals.MULTIPLICATION: None,
        Terminals.DIVISION: None,
        Terminals.ASSIGNEQUALS: None,
    },
}


RULES = {
    'S->Epsilon': [],
    'S->A': [NonTerminals.ASSIGNMENT],
    'S->D': [NonTerminals.DECLARATIVE],
    'S->if': [Terminals.IF, NonTerminals.CONDITIONAL,
              Terminals.THEN, NonTerminals.STATEMENT,
              Terminals.ELSE, NonTerminals.STATEMENT,
              Terminals.ENDIF],
    'S->while': [Terminals.WHILE, NonTerminals.CONDITIONAL,
                 Terminals.DO, NonTerminals.STATEMENT,
                 Terminals.WHILEEND],
    'S->begin': [Terminals.BEGIN, NonTerminals.MORESTATEMENTS, Terminals.END],
    'Ms->S_Ms': [NonTerminals.STATEMENT, NonTerminals.MORESTATEMENTS],
    'Ms->Epsilon': [],
    'C->E_Cp': [NonTerminals.EXPRESSION, NonTerminals.CONDITIONAL_PRIME],
    'Cp->R_E': [NonTerminals.RELATIONAL_OPERATOR, NonTerminals.EXPRESSION],
    'Cp->Epsilon': [],
    'D->Ty_id_Mi_;': [NonTerminals.TYPES, Terminals.ID,
                      NonTerminals.MOREIDS, Terminals.SEMICOLON],
    'Ty->int': [Terminals.INT],
    'Ty->float': [Terminals.FLOAT],
    'Ty->bool': [Terminals.BOOL],
    'Mi->,id_Mi': [Terminals.COMMA, Terminals.ID, NonTerminals.MOREIDS],
    'Mi->Epsilon': [],
    'A->id_=_C_;': [Terminals.ID, Terminals.ASSIGNEQUALS,
                    NonTerminals.CONDITIONAL, Terminals.SEMICOLON],
    'R->>': [Terminals.GT],
    'R-><': [Terminals.LT],
    'R->>=': [Terminals.GTE],
    'R-><=': [Terminals.LTE],
    'R->==': [Terminals.EQUALEQUALS],
    'R-><>': [Terminals.NOTEQUAL],
    'E->T_Ep': [NonTerminals.TERM, NonTerminals.EXPRESSION_PRIME],
    'Ep->+_T_Ep': [Terminals.ADDITION, NonTerminals.TERM,
                   NonTerminals.EXPRESSION_PRIME],
    'Ep->-_T_Ep': [Terminals.SUBTRACTION, NonTerminals.TERM,
                   NonTerminals.EXPRESSION_PRIME],
    'Ep->Epsilon': [],
    'T->F_Tp': [NonTerminals.FACTOR, NonTerminals.TERM_PRIME],
    'Tp->*_F_Tp': [Terminals.MULTIPLICATION, NonTerminals.FACTOR,
                   NonTerminals.TERM_PRIME],
    'Tp->/_F_Tp': [Terminals.DIVISION, NonTerminals.FACTOR,
                   NonTerminals.TERM_PRIME],
    'Tp->Epsilon': [],
    'F->(_E_)': [Terminals.LEFT_PAREN, NonTerminals.EXPRESSION,
                 Terminals.RIGHT_PAREN],
    'F->id': [Terminals.ID],
    'F->num': [Terminals.NUM]
}


def syntactic_analysis(tokens):
    stack = [Terminals.EOF, NonTerminals.MORESTATEMENTS]

    tokens.append(Terminals.EOF)

    position = 0
    while len(stack) > 0:
        stack_item = stack.pop()
        token = tokens[position]
        if isinstance(stack_item, Terminals):
            if stack_item == token:
                position += 1
                # print('pop', stack_item)
                if token == Terminals.EOF:
                    print('input accepted')
            else:
                print('bad term on input:', token)
                break
        elif isinstance(stack_item, NonTerminals):
            # print('stack_item', stack_item, 'token', token)

            rule = table[stack_item][token]
            # print('rule', rule)
            for r in reversed(RULES[rule]):
                stack.append(r)
        # print('stack', stack)


assignment_production = [
    Terminals.ID, Terminals.ASSIGNEQUALS, Terminals.NUM, Terminals.SEMICOLON]

multiple_assignment_production = [
    Terminals.ID, Terminals.ASSIGNEQUALS, Terminals.NUM, Terminals.SEMICOLON,
    Terminals.ID, Terminals.ASSIGNEQUALS, Terminals.NUM, Terminals.SEMICOLON,
    Terminals.ID, Terminals.ASSIGNEQUALS, Terminals.NUM, Terminals.SEMICOLON
]

declarative_production = [Terminals.INT, Terminals.ID, Terminals.SEMICOLON]

multiple_declarative_production = [
    Terminals.INT, Terminals.ID, Terminals.SEMICOLON,
    Terminals.INT, Terminals.ID, Terminals.SEMICOLON,
    Terminals.INT, Terminals.ID, Terminals.SEMICOLON
]

begin_end_production = [Terminals.BEGIN, Terminals.ID,
                        Terminals.ASSIGNEQUALS, Terminals.NUM,
                        Terminals.SEMICOLON, Terminals.END]

if_single_production = [Terminals.IF, Terminals.NUM, Terminals.GT,
                        Terminals.NUM, Terminals.THEN, Terminals.INT,
                        Terminals.ID, Terminals.SEMICOLON, Terminals.ELSE,
                        Terminals.INT, Terminals.ID, Terminals.SEMICOLON, Terminals.ENDIF]

if_multiple_production = [Terminals.IF, Terminals.NUM, Terminals.GT,
                          Terminals.NUM, Terminals.THEN, Terminals.BEGIN,
                          Terminals.INT, Terminals.ID, Terminals.SEMICOLON,
                          Terminals.ID, Terminals.ASSIGNEQUALS, Terminals.NUM, Terminals.SEMICOLON,
                          Terminals.END, Terminals.ELSE, Terminals.BEGIN,
                          Terminals.INT, Terminals.ID, Terminals.SEMICOLON,
                          Terminals.ID, Terminals.ASSIGNEQUALS, Terminals.NUM, Terminals.SEMICOLON,
                          Terminals.END, Terminals.ENDIF]

if_empty_production = [Terminals.IF, Terminals.NUM, Terminals.GT,
                       Terminals.NUM, Terminals.THEN, Terminals.ELSE, Terminals.ENDIF]

if_begin_end_production = [Terminals.IF, Terminals.NUM, Terminals.GT,
                           Terminals.NUM, Terminals.THEN, Terminals.BEGIN,
                           Terminals.END, Terminals.ELSE, Terminals.BEGIN,
                           Terminals.END, Terminals.ENDIF]

while_production = [Terminals.WHILE, Terminals.ID, Terminals.LTE, Terminals.NUM, Terminals.DO,
                    Terminals.ID, Terminals.ASSIGNEQUALS, Terminals.NUM, Terminals.SEMICOLON,
                    Terminals.WHILEEND
                    ]


def test_suite():
    syntactic_analysis(assignment_production)
    syntactic_analysis(multiple_assignment_production)
    syntactic_analysis(declarative_production)
    syntactic_analysis(multiple_declarative_production)
    syntactic_analysis(begin_end_production)
    syntactic_analysis(if_begin_end_production)
    syntactic_analysis(if_empty_production)
    syntactic_analysis(if_multiple_production)
    syntactic_analysis(if_single_production)
    syntactic_analysis(while_production)


test_suite()