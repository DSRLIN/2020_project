def convert_time(json_time_str: str) -> str:
    """2019-03-05 01:53:56
    :rtype: str
    """
    """此为mysql的Datetime串"""
    """2020-12-20T06:14:35Z"""
    """此为json原生时间串"""
    res_str = json_time_str
    if len(res_str) == 27:
        res_str = res_str[0:-8]
    res_str = res_str.replace("T", " ")
    res_str = res_str.replace("Z", "")
    return res_str


def channel_time(json_time_str: str) -> str:
    """2019-03-05 01:53:56
    :rtype: str
    """
    """此为mysql的Datetime串"""
    """2020-12-20T06:14:35.xxxxxxZ"""
    """此为json原生时间串"""
    res_str = json_time_str
    if len(res_str) == 27:
        res_str = res_str[0:-8]
    res_str = res_str.replace("T", " ")
    res_str = res_str.replace("Z", "")
    return res_str

