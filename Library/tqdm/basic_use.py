# [Description] ==================================================
# 진행도 시각화
# 1. iterable을 감싸서 사용
# 2. 수동사용
# pip install tqdm

# [import] ==================================================
from tqdm import tqdm

# [Template] ==================================================
def iterable_template():
    for i in tqdm(range(10)):
        ...

def manual_template():
    with tqdm(total=10) as pbar: # 객체 선언
        ... # 반복 내용 작성
        pbar.update(1) # 수동 갱신

# [Example] ==================================================
# 0.1초씩 sleep하며 진행도 갱신
import time #sleep
# ============================================================

def iterable_example():
    for i in tqdm(range(10)):
        time.sleep(0.1)

def manual_example():
    with tqdm(total=10) as pbar: # 객체 선언
        for i in range(10):
            time.sleep(0.1)
            pbar.update(1) # 수동 갱신

if __name__ == "__main__":
    iterable_example()
    manual_example()

# ============================================================