"""
사칙계산기 프로그램
덧셈, 뺄셈, 곱셈, 나눗셈을 수행하는 간단한 계산기
"""

def add(a, b):
    """두 수의 덧셈"""
    return a + b

def subtract(a, b):
    """두 수의 뺄셈"""
    return a - b

def multiply(a, b):
    """두 수의 곱셈"""
    return a * b

def divide(a, b):
    """두 수의 나눗셈"""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다!")
    return a / b

def calculator():
    """메인 계산기 함수"""
    print("=" * 40)
    print("사칙계산기")
    print("=" * 40)
    
    while True:
        try:
            print("\n연산을 선택하세요:")
            print("1. 덧셈 (+)")
            print("2. 뺄셈 (-)")
            print("3. 곱셈 (*)")
            print("4. 나눗셈 (/)")
            print("5. 종료")
            
            choice = input("\n선택 (1-5): ").strip()
            
            if choice == '5':
                print("계산기를 종료합니다.")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("잘못된 선택입니다. 1-5 사이의 숫자를 입력하세요.")
                continue
            
            num1 = float(input("첫 번째 숫자를 입력하세요: "))
            num2 = float(input("두 번째 숫자를 입력하세요: "))
            
            if choice == '1':
                result = add(num1, num2)
                operator = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operator = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operator = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operator = "/"
            
            print(f"\n결과: {num1} {operator} {num2} = {result}")
            
        except ValueError as e:
            print(f"오류: {e}")
        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    calculator()

