import queue
# [Description] ==================================================
# 선입선출 자료구조


# [Example] ==================================================
# example description
# ============================================================

def fifo_example(q:queue.Queue):
    q.put(1)        # [1]
    q.put(2)        # [1,2]
    q.put(3)        # [1,2,3]
    print(q.get())  # [2,3]
    print(q.get())  # [3]
    q.put(4)        # [3,4]
    print(q.get())  # [4]
    print(q.get())  # []

# --------------------------

def put_list_data(q:queue.Queue,datas:list):
    [q.put(x) for x in datas]

def print_all_item(q:queue.Queue):
    while not q.empty():
        print(q.get())

def put_all_and_print_all(q:queue.Queue):
    my_list = [1,4,2,5,3,7,2,5]
    put_list_data(q,my_list)
    print_all_item(q)

# --------------------------
if __name__ == "__main__":
    q = queue.Queue()
    fifo_example(q)
    # --------------------------
    # put_all_and_print_all(q)

# ============================================================