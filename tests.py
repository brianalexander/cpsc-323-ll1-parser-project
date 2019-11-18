from ll_parser import syntactic_analysis
from Constants import Terminals, NonTerminals

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


def add_fillers(my_array):
    return [('token', 'lexeme', item, 1) for item in my_array]


if __name__ == "__main__":
    syntactic_analysis(add_fillers(assignment_production), verbose=False)
    syntactic_analysis(add_fillers(multiple_assignment_production), verbose=False)
    syntactic_analysis(add_fillers(declarative_production), verbose=False)
    syntactic_analysis(add_fillers(multiple_declarative_production), verbose=False)
    syntactic_analysis(add_fillers(begin_end_production), verbose=False)
    syntactic_analysis(add_fillers(if_begin_end_production), verbose=False)
    syntactic_analysis(add_fillers(if_empty_production), verbose=False)
    syntactic_analysis(add_fillers(if_multiple_production), verbose=False)
    syntactic_analysis(add_fillers(if_single_production), verbose=False)
    syntactic_analysis(add_fillers(while_production), verbose=False)
