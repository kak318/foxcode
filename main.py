f = open("main.fox", "r")
main = f.read()
f.close()

cMain = ""
cur = ""
pos = 0

mem = {}

cMain = main.split()

T_VAR = "var"
T_STR = ":str"
T_INT = ":int"
T_BOOL = ":bool"
T_INPUT = ":input"
T_VARIND = ":var"
T_PRINT = "print"
T_MATH = "math"
T_EXIT = "exit()"
T_MEM = "mem()"

try:
  for i in cMain:
    #if pos == len(cMain):
    #  exit(0)
    cur = cMain[pos]
    if cur == T_VAR:
      if cMain[pos + 3] == T_EQ:
        update = cMain[pos + 2]
        if update == T_STR:
          M = str(cMain[pos + 4])
        elif update == T_INT:
          M = int(cMain[pos + 4])
        elif update == T_BOOL:
          M = bool(cMain[pos + 4])
        elif update == T_INPUT:
          M = input(cMain[pos + 4])
        else:
          print(f"ERROR: POS {pos}: variable must be bool, str or int not '{cMain[pos + 2]}'")
          exit()
        mem.update({
          cMain[pos + 1]: M 
        })
        pos += 4
    elif cur == T_PRINT:
      if cMain[pos + 1] == T_VARIND:
        print(mem[cMain[pos + 2]])
      if cMain[pos + 1] == T_STR:
        print(cMain[pos + 2])
      pos += 2
    elif cur == T_MEM:
      print(mem)
    elif cur == T_EXIT:
      exit(0)
    elif cur == T_MATH:
      var = cMain[pos + 1]
      operator = cMain[pos + 2]
      operation = cMain[pos + 3]
      var_int = int(cMain[pos + 4])
      if operator == "+":
        if operation == T_INT:
          mem[var] += var_int
        elif operation == T_VARIND:
          mem[var] += mem[var_int]
        pos += 4
      if operator == "-":
        if operation == T_INT:
          mem[var] -= var_int
        elif operation == T_VARIND:
          mem[var] -= mem[var_int]
        pos += 4
      if operator == "*":
        if operation == T_INT:
          mem[var] *= var_int
        elif operation == T_VARIND:
          mem[var] *= mem[var_int]
        pos += 4
      if operator == "/":
        if operation == T_INT:
          mem[var] /= var_int
        elif operation == T_VARIND:
          mem[var] /= mem[var_int]
        pos += 4
      if operator == "-":
        if operation == T_INT:
          mem[var] = var_int
        elif operation == T_VARIND:
          mem[var] = mem[var_int]
        pos += 4
    else:
      print(f"ERROR: POS {pos}: syntax error: {cur}")
      exit()
    pos += 1
except IndexError:
  exit(0)
except KeyError as e:
  print(f"ERROR: POS {pos}: unknown variable {e}")
  exit(1)