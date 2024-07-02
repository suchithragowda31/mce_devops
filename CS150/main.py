from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def main():
    print("Simple Calculator Program")
    
    a = 12
    b = 15
    
    print(f"Addition of {a} and {b}: {add(a, b)}")
    print(f"Subtraction of {a} and {b}: {subtract(a, b)}")
    print(f"Multiplication of {a} and {b}: {multiply(a, b)}")
    print(f"Division of {a} and {b}: {divide(a, b)}")

if __name__ == "__main__":
    main()
