# coding:utf8
""" URL参数集
【详细说明】https://lbs.amap.com/api/webservice/guide/api/search#text
"""
url_param = {
    # 【keywords】与【types】至少填一种
    'keywords' : '',
        # 【必选】查询关键字：多个关键字用“|”分割
    'types' : '港口码头',
        # 【必选】类型：分类代码或汉字（格式：amap_code/amap_poicode）
    'city' : '福建省',
        # 【可选】查询城市：城市中文、中文全拼、citycode、adcode
    'citylimit' : 'true',
        # 【可选】仅返回指定城市数据：true/false
    'output' : 'json',
    'key' : '4fac3db866dcc3b8a735651d3a7db1c7'
}

""" 保存的字段
"""
save_field = [
    ["poiid", "TEXT", 250],
    ["name", "TEXT", 250],
    ["type", "TEXT", 250],
    ["pname", "TEXT", 250],
]

# 输出的文件夹
out_dir = r"D:\mycode\GISandPython\3AMap\poi\data"
# 输出的名字
out_name = u"福建省港口.shp"

# 爬取的最大页数
MAX_PAGE = 100000