def arithmetic_arranger(problems, solve = False):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  first = ""
  second = ''
  lines = ''
  sumx = ''
  for problem in problems:
    fn = problem.split()[0]
    op = problem.split()[1]
    sn = problem.split()[2]
    if len(fn) > 4 or len(sn) > 4:
      return "Error: Numbers cannot be more than four digits."
    if op == '*' or op == '/':
      return "Error: Operator must be '+' or '-'."
    try:
      num1 = int(fn)
      num2 = int(sn)
    except:
      return "Error: Numbers must only contain digits."

    summ = ''
    if op == '+':
      summ = str(int(fn) + int(sn))
    elif op == '-':
      summ = str(int(fn) - int(sn))

    length = max(len(fn), len(sn)) + 2
    top = str(fn).rjust(length)
    bottom = op + str(sn).rjust(length - 1)
    line = ''
    res = str(summ).rjust(length)
    for s in range (length):
      line += '-'

    if problem != problems[-1]:
      first += top + "    "
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      first += top
      second += bottom
      lines += line
      sumx += res
  if solve:
    string = first + '\n' + second + '\n' + lines + '\n' + sumx
  else:
    string = first + '\n' + second + '\n' + lines
  return string
