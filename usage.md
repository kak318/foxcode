Usage
---
`var [name] [:str | :int] = [value]` - create variable</br>
`var [name] :input = [string]` - create input</br>
`print [:var | :str] [name | string]` - print something</br>
`math [variable] [+ | - | / | * | =] [:int | :var] [value]` - math operations</br>
`mem()` - display variables in the memory</br>
`exit()` - exit the program</br>
All Tokens</br>
---
```
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
```