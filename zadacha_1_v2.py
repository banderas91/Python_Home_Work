# вариант с использованием алгоритма обратной польской нотации и т.д.

def opz(program: str):
    stack = []
    for token in program.split():
        if token == '+':
            if len(stack) < 2:
                raise ValueError(f"Выражение написано неправильно")
            b = stack.pop()
            a = stack.pop()
            result = a + b
            stack.append(result)
        elif token == '-':
            if len(stack) < 2:
                raise ValueError(f"Выражение написано неправильно")
            b = stack.pop()
            a = stack.pop()
            result = a - b
            stack.append(result)
        elif token == '*':
            if len(stack) < 2:
                raise ValueError(f"Выражение написано неправильно")
            b = stack.pop()
            a = stack.pop()
            result = a * b
            stack.append(result)  
        elif token == '/':
            if len(stack) < 2:
                raise ValueError(f"Выражение написано неправильно")
            b = stack.pop()
            a = stack.pop()
            result = a / b
            stack.append(result)                              
        else:
            try:
                stack.append(int(token))
            except ValueError:
                print(f"{token!r} не удалось перевести в целое число)")

    if len(stack) != 1:
        print("Ошбика")
         
    return stack.pop() 

def parse_str_infix(infix: str):
    token_list = []
    token = ''
    last_was_digit = False
    stack = []
# 32 + 11
    for i in infix:
        if i == ' ':
            continue
        elif i in {'0','1','2','3','4','5','6','7','8','9'}:
            if not last_was_digit:
                token = ''
            token += i
            last_was_digit = True        
        else:
            if last_was_digit:
                value = int(token)
                token_list.append(value)
                token = ''
            last_was_digit = False
            
            if i in {'+','-'}:
                
                if len(stack) >= 1:
                    print(stack)
                    
                    if stack[len(stack) - 1] in {'/','*','-','+'}:
                        token = stack.pop()
                        stack.append(i)
                        token_list.append(token)
                else:
                    stack.append(i)
            elif i in {'/','*'}:
                if len(stack) >= 1:
                    if stack[len(stack) - 1] in {'-','+'}:
                        stack.append(i)
                    else:
                        token = stack.pop()
                        stack.append(i)
                        token_list.append(token)
                else:
                    stack.append(i)                        
    else:
        if token != '':
            value = int(token)
            token_list.append(value)
            token = ''
        if len(stack) > 0:
            while len(stack) > 0:
                token = stack.pop()
                token_list.append(token)
    postfix = ''
    for i in token_list:
        postfix += str(i) + ' '


    return postfix

text = ''



postfix = parse_str_infix('42 + 11 * 2 + 1 / 2')
print(postfix)
print(opz(postfix))