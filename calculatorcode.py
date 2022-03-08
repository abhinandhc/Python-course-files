from art import calcu

def add(n1,n2):
  return n1+n2

def subt(n1,n2):
  return n1-n2

def mul(n1,n2):
  return n1*n2

def divs(n1,n2):
  return n1/n2

aop={
  "+":add,
  "-":subt,
  "*":mul,
  "/":divs,
}
def calculator():
  print(calcu)
  num1=float(input("Input the first number :"))
  for symb in aop:
    print(symb)
  contnue =True
  while contnue:
    
    uinp=input("Select the operation to be performed :")
    num2=float(input("Input the next number :"))
    calculations = aop[uinp]
    fans = calculations(num1,num2)
    print(f"{num1} {uinp} {num2} = {fans}")
    if input(f"Enter 'y' to continue with {fans} or 'n' to quit :") == 'y':
      num1=fans
    else:
      contnue = False
      calculator()
calculator()
