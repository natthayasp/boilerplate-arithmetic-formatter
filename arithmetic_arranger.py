import re

def arithmetic_arranger(problems, show = False):
  first = ""
  second = ""
  answer = ""
  lines = ""
  if len(problems) > 5:
    return "Error: Too many problems."
    
  for problem in problems:
    firstnum = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondnum = problem.split(" ")[2]
    try:
      int(firstnum)
      int(secondnum)
    except:
      return "Error: Numbers must only contain digits."
      
    if ((operator) == "/" or (operator) == "*"):
      return "Error: Operator must be '+' or '-'."

    if (len(firstnum) >= 5 or len(secondnum) >= 5):
      return "Error: Numbers cannot be more than four digits."
      
    sum = ""
    if (operator=="+"):
      sum = str(int(firstnum)+int(secondnum))
    elif(operator=="-"):
      sum = str(int(firstnum)-int(secondnum))

    length = max(len(firstnum),len(secondnum))+2
    
    line1 = str(firstnum).rjust(length)
    line2 = operator + str(secondnum).rjust(length-1)
    ans = str(sum).rjust(length)
    line =""
    for l in range(length):
      line += "-"

    if problem != problems[-1]:
      first += line1 + '    '
      second += line2 + '    '
      lines += line + '    '
      answer += ans + '    '
    else:
      first += line1
      second += line2
      lines += line
      answer += ans
      
  if show:
    arithmetic_problems = first + "\n" + second + "\n" + lines + "\n" + answer
  else:
    arithmetic_problems = first + "\n" + second + "\n" + lines
    
  return arithmetic_problems
