import re

def to_bin_str(x:int):
    return str(bin(x))[2:]

def ori_encode(s):
    ret = ""
    # 将输入转换成bytes格式
    b = bytes(s, encoding="utf-8")
    #转换为GE加密格式
    for x in b:
        x_bin = to_bin_str(x)
        ret += x_bin.replace("0", "\u200b").replace("1", "\u200c")
    return ret

def ori_decode(b):
    if len(b)%8:
        raise ValueError("输入有误")
    b_bin = b.replace("\u200b", "0").replace("\u200c", "1")
    b_list = []
    for i in range(0, len(b_bin),8):
        b_list.append(int(b_bin[i:i+8], 2))
    return str(bytes(b_list), encoding="utf-8")

def unpack(s):
    try:
        re_obj = re.search("\u200d.+?\u200d", s, flags=0)
        return re_obj.group(0)[1:-1]
    except Exception as e:
        print(f"输入有误:{e}")
        exit(0)

def pack(ori_s):
    return f"G\u200d{ori_s}\u200dE"

def encode(s):
    return pack(ori_encode(s))

def decode(s):
    return ori_decode(unpack(s))

if __name__ == "__main__":
    print('''
  ____ _               _   _____                     _ _
 / ___| |__   ___  ___| |_| ____|_ __   ___ ___   __| (_)_ __   __ _
| |  _| '_ \ / _ \/ __| __|  _| | '_ \ / __/ _ \ / _` | | '_ \ / _` |
| |_| | | | | (_) \__ \ |_| |___| | | | (_| (_) | (_| | | | | | (_| |
 \____|_| |_|\___/|___/\__|_____|_| |_|\___\___/ \__,_|_|_| |_|\__, |
                                                               |___/
    将一句话隐藏到两个字符中间
    v0.0.1 - python3.6+
''')
    method = input("请选择要进行的操作：\n1.加密\n2.解密\n请输入序号：")
    if method == "1":
        s = input("请输入需要加密的句子:")
        # TODO 验证输入是否正确
        with open("out.txt", "w", encoding="utf-8") as f:
            f.write(encode(s))
        print("成功加密，已输出到out.txt中")
    elif method == "2":
        s = input("请粘贴需要解密的句子:")
        # TODO 验证输入是否正确
        print(decode(s))
    else:
        print("无法识别")
