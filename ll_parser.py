import sys
from Constants import NonTerminals, Terminals, INDEX_TO_RULES, TABLE, RULES
from lexer import lexer


def token_to_terminal(tokens):
    terminal_string = []
    # tokens[0] -> token
    # tokens[1] -> lexeme
    # tokens[2] -> line number
    for i in range(len(tokens)):
        to_append = []
        current_token = tokens[i][0]
        current_lexeme = tokens[i][1]

        # Add the token in position 0
        to_append.append(current_token)

        # Add the lexeme in position 1
        to_append.append(str.lower(current_lexeme))

        # Add the Terminal in position 2
        if(current_token == "KEYWORD"):
            if(current_lexeme == 'begin'):
                to_append.append(Terminals.BEGIN)
            elif(current_lexeme == 'end'):
                to_append.append(Terminals.END)
            elif(current_lexeme == 'while'):
                to_append.append(Terminals.WHILE)
            elif(current_lexeme == 'whileend'):
                to_append.append(Terminals.WHILEEND)
            elif(current_lexeme == 'do'):
                to_append.append(Terminals.DO)
            elif(current_lexeme == 'if'):
                to_append.append(Terminals.IF)
            elif(current_lexeme == 'then'):
                to_append.append(Terminals.THEN)
            elif(current_lexeme == 'else'):
                to_append.append(Terminals.ELSE)
            elif(current_lexeme == 'endif'):
                to_append.append(Terminals.ENDIF)
            elif(current_lexeme == 'int'):
                to_append.append(Terminals.INT)
            elif(current_lexeme == 'float'):
                to_append.append(Terminals.FLOAT)
            elif(current_lexeme == 'bool'):
                to_append.append(Terminals.BOOL)
        elif(current_token in ['INT', 'REAL']):
            to_append.append(Terminals.NUM)
        elif (current_token == 'IDENTIFIER'):
            to_append.append(Terminals.ID)
        elif(current_token == 'SEPARATOR'):
            if (current_lexeme == "("):
                to_append.append(Terminals.LEFT_PAREN)
            elif (current_lexeme == ")"):
                to_append.append(Terminals.RIGHT_PAREN)
            elif(current_lexeme == ','):
                to_append.append(Terminals.COMMA)
            elif(current_lexeme == ';'):
                to_append.append(Terminals.SEMICOLON)
        elif(current_token == 'OPERATOR'):
            if (current_lexeme == "+"):
                to_append.append(Terminals.ADDITION)
            elif (current_lexeme == "-"):
                to_append.append(Terminals.SUBTRACTION)
            elif(current_lexeme == '*'):
                to_append.append(Terminals.MULTIPLICATION)
            elif(current_lexeme == '>'):
                to_append.append(Terminals.GT)
            elif(current_lexeme == '>='):
                to_append.append(Terminals.GTE)
            elif(current_lexeme == '<'):
                to_append.append(Terminals.LT)
            elif(current_lexeme == '<='):
                to_append.append(Terminals.LTE)
            elif(current_lexeme == '=='):
                to_append.append(Terminals.EQUALEQUALS)
            elif(current_lexeme == '='):
                to_append.append(Terminals.ASSIGNEQUALS)
            elif(current_lexeme == '<>'):
                to_append.append(Terminals.NOTEQUAL)

        # add line number in position 3
        to_append.append(tokens[i][2])
        terminal_string.append(to_append)

    return terminal_string


def syntactic_analysis(tokens, verbose=True):
    # tokens[0] token_type
    # tokens[1] lexeme
    # tokens[2] terminal type
    # tokens[3] line number
    old_position = -1

    stack = [Terminals.EOF, NonTerminals.MORESTATEMENTS]

    tokens.append(('EOF', '$', Terminals.EOF, 0))

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
                print('Expected', stack_item, ', got',
                      terminal_type, "on line", line_number)
                print('Lexeme:', lexeme)
                print('Token:', token_type)
                break
        elif isinstance(stack_item, NonTerminals):
            if(old_position != position):
                if verbose:
                    print('Token:', token_type, '\t', 'Lexeme:', lexeme)
                old_position = position

            rule = TABLE[stack_item][terminal_type]
            if verbose:
                print('\t', INDEX_TO_RULES[rule])

            for r in reversed(RULES[rule]):
                stack.append(r)
        # print('stack', stack)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Please specify a file path to lex as the first argument.")
        sys.exit()

    # To lex a file, please pass the path as the first argument
    # Example usage: python3 lexer.py [path]
    path = sys.argv[1]

    tokens, illegal_tokens = lexer(path)

    terminal_string = token_to_terminal(tokens)

    syntactic_analysis(terminal_string)
