"""
코드 작성 일잘 : 2024 - 01 - 20
코드 작성자 : 김병찬
코드 이름 : utils.py
코드 목적 : 유용한 함수를 따로 저장해 두고 나중에 불러와 사용하기 위해.
"""


def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)


def gugudan(x):
    for i in range(9):
        print((i+1) * x)

