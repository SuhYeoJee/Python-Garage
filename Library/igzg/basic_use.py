from igzg.mySQL import getInsertQuery
from igzg.utils import write_error
from igzg.configManager import ConfigManager
# [Description] ==================================================
# description

# [Example] ==================================================
# example description
# ============================================================
def igzg_mySQL_example():
    res = getInsertQuery('myTable',{'k1':'v1','k2':'v2','k3':'v3'})
    print(res)

def igzg_utils_example():
    try:
        _ = 1/0
    except Exception as e:
        write_error(e,console_logging=True)

def igzg_ConfigManager_example():
    cm = ConfigManager()
    cm.new_item('s1',{'k1':'v1'})
    cm.new_item('s1',{'k2':'v2'})
    print(cm.get_section_items('s1'))
    print(cm.get_section_keys('s2'))

if __name__ == "__main__":
    igzg_ConfigManager_example()

# ============================================================