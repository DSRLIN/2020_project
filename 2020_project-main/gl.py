from DAO import *
from Classes import *

dbc = ConnectionManager()

input_conn = False
cur_se = 0  # 1代表vd，2代表cn
db_dict = {
    "user": "",
    "password": "",
    "host": "",
    "instance": ""
}
cn_dict = {}
vd_dict = {}
# 用后需销毁
cn_in = ""
vd_in = ""
# 完
cur_cn: Channel = None
cur_vd: Video = None
apiKey = "AIzaSyBLxHr8njhibZlupJrtNi7Pxgan8LRtYxc"
