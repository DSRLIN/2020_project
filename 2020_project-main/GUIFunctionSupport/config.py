import json

from deprecated.sphinx import deprecated
from jsonpath import jsonpath

from Classes import ConfigError
from gl import dbc, db_dict


@deprecated(reason="No need to generate a uri for db-conn")
def gen_uri(username: str, password: str, dbs_ip: str, instance: str = "YDA_RES"):
    return r"mysql://" + username + ":" + password + "@" + dbs_ip + r"/" + instance + r"?charset=utf8"


def __check_config_file():
    with open("./config.json", "r") as conf_file:
        conf_res = json.load(conf_file)
    if conf_res["user"] == "" or conf_res["password"] == "" or conf_res["host"] == "" or conf_res["instance"] == "":
        raise ConfigError("配置文件缺失属性")


def read_config_file():
    try:
        __check_config_file()
    except ConfigError:
        return False
    else:
        with open("./config.json", "r") as conf_file:
            conf_res = json.load(conf_file)
        return conf_res


def set_config_file(user,
                    password,
                    host="localhost",
                    instance="YDA_RES"):
    def_conf_dic = {"user": user,
                    "password": password,
                    "host": host,
                    "instance": instance}

    with open("./config.json", "w") as conf_file:
        json.dump(def_conf_dic, conf_file)

    try:
        __check_config_file()
    except ConfigError:
        return False
    else:
        return True


def db_conn_with_input():
    dbc.set_conn_info(db_dict["user"],
                      db_dict["password"],
                      db_dict["host"],
                      db_dict["instance"])
    return dbc.get_connection_status()


def db_conn_with_conf():
    if read_config_file() is not False:
        dbc.set_conn_info(
            jsonpath(read_config_file(), "$.user")[0],
            jsonpath(read_config_file(), "$.password")[0],
            jsonpath(read_config_file(), "$.host")[0],
            jsonpath(read_config_file(), "$.instance")[0]
        )
        return dbc.get_connection_status()
    else:
        return False


def save_conf_to_file():
    res = dbc.get_conn_info()
    try:
        set_config_file(res[0], res[1], res[2], res[3])
    except ConfigError:
        return False
    else:
        return True
