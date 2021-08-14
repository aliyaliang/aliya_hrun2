import time


def register_user():
    """随机生成注册账号"""
    # print(int(time.time()))
    time.sleep(0.1)
    username = "test"+str(int(time.time()*100))
    return username


def goods_code():
    """随机生成商品编码goodscode"""
    # print(int(time.time()))
    time.sleep(0.1)
    goodscode = "sp_"+str(int(time.time()*100))
    return goodscode

if __name__ == '__main__':
    print(register_user())
    print(goods_code())