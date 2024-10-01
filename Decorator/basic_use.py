# [Description] ==================================================
# Decorator(데코레이터,장식자)
# 함수를 내부 함수로 감싸서 실행하고 결과를 반환
# 함수를 수정하지 않고 추가기능 구현
# 인자로 전달된 함수의 앞, 뒤에 동작을 추가

# [Template] ==================================================
def decorator_template(func):
    def wrapper(self, *args, **kwargs):
        ...  # 확장 내용 작성
        result = func(self, *args, **kwargs)
        ...  # 확장 내용 작성
        return result
    return wrapper

# [Example] ==================================================
# my_func 함수의 앞, 뒤에 print 동작을 추가하는 예제
# ============================================================
def my_decorator(func): # 데코레이터 정의
    def wrapper(*args, **kwargs):
        print("before func")
        result = func(*args, **kwargs)
        print("after func")
        return result
    return wrapper

@my_decorator # 데코레이터 사용
def my_func():
    print('hi')

if __name__ == "__main__":
    my_func()

# ============================================================