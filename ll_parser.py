import sys
from Constants import NonTerminals, Terminals, ProductionFactory
from lexer import lexer, token_to_terminal


# parse table
table = {
    NonTerminals.STATEMENT: {
        Terminals.BEGIN: 5,
        Terminals.IF: 3,
        Terminals.THEN: None,
        Terminals.ELSE: 0,
        Terminals.ENDIF: 0,
        Terminals.WHILE: 4,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: 2,
        Terminals.FLOAT: 2,
        Terminals.BOOL: 2,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 1,
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
        Terminals.BEGIN: 6,
        Terminals.IF: 6,
        Terminals.THEN: None,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: 6,
        Terminals.DO: None,
        Terminals.WHILEEND: None,
        Terminals.END: 7,
        Terminals.GT: None,
        Terminals.LT: None,
        Terminals.GTE: None,
        Terminals.LTE: None,
        Terminals.EQUALEQUALS: None,
        Terminals.NOTEQUAL: None,
        Terminals.INT: 6,
        Terminals.FLOAT: 6,
        Terminals.BOOL: 6,
        Terminals.SEMICOLON: None,
        Terminals.COMMA: None,
        Terminals.ID: 6,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: 7,
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
        Terminals.ID: 8,
        Terminals.NUM: 8,
        Terminals.LEFT_PAREN: 8,
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
        Terminals.THEN: 10,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: 10,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 9,
        Terminals.LT: 9,
        Terminals.GTE: 9,
        Terminals.LTE: 9,
        Terminals.EQUALEQUALS: 9,
        Terminals.NOTEQUAL: 9,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 10,
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
        Terminals.INT: 11,
        Terminals.FLOAT: 11,
        Terminals.BOOL: 11,
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
        Terminals.INT: 12,
        Terminals.FLOAT: 13,
        Terminals.BOOL: 14,
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
        Terminals.SEMICOLON: 16,
        Terminals.COMMA: 15,
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
        Terminals.ID: 17,
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
        Terminals.ID: 24,
        Terminals.NUM: 24,
        Terminals.LEFT_PAREN: 24,
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
        Terminals.THEN: 27,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: 27,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 27,
        Terminals.LT: 27,
        Terminals.GTE: 27,
        Terminals.LTE: 27,
        Terminals.EQUALEQUALS: 27,
        Terminals.NOTEQUAL: 27,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 27,
        Terminals.COMMA: None,
        Terminals.ID: None,
        Terminals.NUM: None,
        Terminals.LEFT_PAREN: None,
        Terminals.RIGHT_PAREN: 27,
        Terminals.EOF: None,
        Terminals.ADDITION: 25,
        Terminals.SUBTRACTION: 26,
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
        Terminals.ID: 28,
        Terminals.NUM: 28,
        Terminals.LEFT_PAREN: 28,
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
        Terminals.THEN: 31,
        Terminals.ELSE: None,
        Terminals.ENDIF: None,
        Terminals.WHILE: None,
        Terminals.DO: 31,
        Terminals.WHILEEND: None,
        Terminals.END: None,
        Terminals.GT: 31,
        Terminals.LT: 31,
        Terminals.GTE: 31,
        Terminals.LTE: 31,
        Terminals.EQUALEQUALS: 31,
        Terminals.NOTEQUAL: 31,
        Terminals.INT: None,
        Terminals.FLOAT: None,
        Terminals.BOOL: None,
        Terminals.SEMICOLON: 31,
        Terminals.COMMA: None,
        Terminals.ID: 31,
        Terminals.NUM: 31,
        Terminals.LEFT_PAREN: 31,
        Terminals.RIGHT_PAREN: None,
        Terminals.EOF: None,
        Terminals.ADDITION: 31,
        Terminals.SUBTRACTION: 31,
        Terminals.MULTIPLICATION: 29,
        Terminals.DIVISION: 30,
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
        Terminals.ID: 33,
        Terminals.NUM: 34,
        Terminals.LEFT_PAREN: 32,
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
        Terminals.GT: 18,
        Terminals.LT: 19,
        Terminals.GTE: 20,
        Terminals.LTE: 21,
        Terminals.EQUALEQUALS: 22,
        Terminals.NOTEQUAL: 23,
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
p = ProductionFactory()
index_to_rules = [
    p.Statement.To.Epsilon.Finish,
    p.Statement.To.Assignment.Finish,
    p.Statement.To.Declarative.Finish,
    p.Statement.To.If.Conditional.Then.Statement.Else.Statement.Endif.Finish,
    p.Statement.To.While.Conditional.Do.Statement.Whileend.Finish,
    p.Statement.To.Begin.MoreStatements.End.Finish,
    p.MoreStatements.To.Statement.MoreStatements.Finish,
    p.MoreStatements.To.Epsilon.Finish,
    p.Conditional.To.Expression.ConditionalPrime.Finish,
    p.ConditionalPrime.To.Relop.Expression.Finish,
    p.ConditionalPrime.To.Epsilon.Finish,
    p.Declarative.To.Type.Id.MoreIds.Semicolon.Finish,
    p.Type.To.Int.Finish,
    p.Type.To.Float.Finish,
    p.Type.To.Bool.Finish,
    p.MoreIds.To.Comma.Id.MoreIds.Finish,
    p.MoreIds.To.Epsilon.Finish,
    p.Assignment.To.Id.Assignequals.Conditional.Semicolon.Finish,
    p.Relop.To.GreaterThan.Finish,
    p.Relop.To.LessThan.Finish,
    p.Relop.To.GreaterThanEqual.Finish,
    p.Relop.To.LessThanEqual.Finish,
    p.Relop.To.Equalequal.Finish,
    p.Relop.To.Notequal.Finish,
    p.Expression.To.Term.ExpressionPrime.Finish,
    p.ExpressionPrime.To.Addition.Term.ExpressionPrime.Finish,
    p.ExpressionPrime.To.Subtraction.Term.ExpressionPrime.Finish,
    p.ExpressionPrime.To.Epsilon.Finish,
    p.Term.To.Factor.TermPrime.Finish,
    p.TermPrime.To.Multiplication.Factor.TermPrime.Finish,
    p.TermPrime.To.Division.Factor.TermPrime.Finish,
    p.TermPrime.To.Epsilon.Finish,
    p.Factor.To.LeftParenthesis.Expression.RightParenthesis.Finish,
    p.Factor.To.Id.Finish,
    p.Factor.To.Num.Finish
]
RULES = {
    0: [],
    1: [NonTerminals.ASSIGNMENT],
    2: [NonTerminals.DECLARATIVE],
    3: [Terminals.IF, NonTerminals.CONDITIONAL,
        Terminals.THEN, NonTerminals.STATEMENT,
        Terminals.ELSE, NonTerminals.STATEMENT,
        Terminals.ENDIF],
    4: [Terminals.WHILE, NonTerminals.CONDITIONAL,
        Terminals.DO, NonTerminals.STATEMENT,
        Terminals.WHILEEND],
    5: [Terminals.BEGIN, NonTerminals.MORESTATEMENTS, Terminals.END],
    6: [NonTerminals.STATEMENT, NonTerminals.MORESTATEMENTS],
    7: [],
    8: [NonTerminals.EXPRESSION, NonTerminals.CONDITIONAL_PRIME],
    9: [NonTerminals.RELATIONAL_OPERATOR, NonTerminals.EXPRESSION],
    10: [],
    11: [NonTerminals.TYPES, Terminals.ID,
         NonTerminals.MOREIDS, Terminals.SEMICOLON],
    12: [Terminals.INT],
    13: [Terminals.FLOAT],
    14: [Terminals.BOOL],
    15: [Terminals.COMMA, Terminals.ID, NonTerminals.MOREIDS],
    16: [],
    17: [Terminals.ID, Terminals.ASSIGNEQUALS,
         NonTerminals.CONDITIONAL, Terminals.SEMICOLON],
    18: [Terminals.GT],
    19: [Terminals.LT],
    20: [Terminals.GTE],
    21: [Terminals.LTE],
    22: [Terminals.EQUALEQUALS],
    23: [Terminals.NOTEQUAL],
    24: [NonTerminals.TERM, NonTerminals.EXPRESSION_PRIME],
    25: [Terminals.ADDITION, NonTerminals.TERM,
         NonTerminals.EXPRESSION_PRIME],
    26: [Terminals.SUBTRACTION, NonTerminals.TERM,
         NonTerminals.EXPRESSION_PRIME],
    27: [],
    28: [NonTerminals.FACTOR, NonTerminals.TERM_PRIME],
    29: [Terminals.MULTIPLICATION, NonTerminals.FACTOR,
         NonTerminals.TERM_PRIME],
    30: [Terminals.DIVISION, NonTerminals.FACTOR,
         NonTerminals.TERM_PRIME],
    31: [],
    32: [Terminals.LEFT_PAREN, NonTerminals.EXPRESSION,
         Terminals.RIGHT_PAREN],
    33: [Terminals.ID],
    34: [Terminals.NUM]
}


def syntactic_analysis(tokens):
    # tokens[0] token_type
    # tokens[1] lexeme
    # tokens[2] terminal type
    # tokens[3] line number
    old_position = -1

    rules_array = []
    stack = [Terminals.EOF, NonTerminals.MORESTATEMENTS]

    tokens.append(('EOF', '$', Terminals.EOF))

    position = 0
    while len(stack) > 0:
        stack_item = stack.pop()

        token_type = tokens[position][0]
        lexeme = tokens[position][1]
        terminal_type = tokens[position][2]
        line_number = tokens[position][3]

        if isinstance(stack_item, Terminals):
            if stack_item == terminal_type:
                position += 1
                # print('pop', stack_item)
                if terminal_type == Terminals.EOF:
                    print('input accepted')
            else:
                print('Syntax Error:')
                print('Expected', stack_item, ', got', terminal_type, "on line", line_number)
                print('Lexeme:', lexeme)
                print('Token:', token_type)
                break
        elif isinstance(stack_item, NonTerminals):
            if(old_position != position):
                print('Token:', token_type, '\t', 'Lexeme:', lexeme)
                old_position = position

            rule = table[stack_item][terminal_type]
            print('\t', index_to_rules[rule])

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

while_parens_production = [Terminals.WHILE, Terminals.LEFT_PAREN,
                           Terminals.ID, Terminals.LTE, Terminals.NUM, Terminals.RIGHT_PAREN,
                           Terminals.DO, Terminals.ID, Terminals.ASSIGNEQUALS, Terminals.NUM,
                           Terminals.SEMICOLON, Terminals.WHILEEND
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


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Please specify a file path to lex as the first argument.")
        sys.exit()

    # To lex a file, please pass the path as the first argument
    # Example usage: python3 lexer.py [path]
    path = sys.argv[1]

    tokens, illegal_tokens = lexer(path)
    # print(tokens)
    terminal_string = token_to_terminal(tokens)
    # token_type, lexeme, terminal_type
    # print(terminal_string)
    syntactic_analysis(terminal_string)

    # print("TOKENS\t\t\tLexemes")
    # for token in tokens:
    #     print("{0:10}\t\t{1}".format(token[0], token[1]))
    # if(len(illegal_tokens) > 0):
    #     print("\nILLEGAL TOKENS")
    #     print("Line\t\t\tIllegal Token")
    #     for token in illegal_tokens:
    #         print("{0}\t\t\t{1}".format(token[0], token[1]))
