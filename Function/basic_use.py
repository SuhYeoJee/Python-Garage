# [Description] ==================================================
# 여러가지 함수 정의
# [Template] ==================================================
#
# [Example] ==================================================
# parameter_example: 가변인자, 키워드 가변인자
# literal_example: 리터럴 타입힌트
# ============================================================
def parameter_example(a,*args,**kwargs):
    print(a)
    for i in args:
        print(i)
    for k,v in kwargs.items():
        print(f"{k}:{v}")
# --------------------------
from typing import Literal
def literal_example(yes_or_no: Literal["yes","no"]):
    print(yes_or_no)
# --------------------------
if __name__ == "__main__":
    parameter_example("a",[1,2],3,'3f',q=1,w=2,e=3,r='4')


# ============================================================