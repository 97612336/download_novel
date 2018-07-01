import json
import os

user_home = os.environ.get("HOME")

conf_base_path = user_home + "/conf"

mysql_conf_path = conf_base_path + "/mysql.conf"

with open(mysql_conf_path, "r") as f1:
    res_str = f1.read()

mysql_dict = json.loads(res_str)
