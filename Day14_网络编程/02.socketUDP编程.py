"""udp协议：User Data Protocol 用户数据报协议，是一个无连接的简单的面向数据报的传输层协议。不提供可靠性，没有超时重发机制，传输速度快。缺点：容易丢包，易遭受黑客攻击用途：—— 可以简单理解为写信    语音广播    视频    QQ    TFTP（简单文件传输）TCP和UDP的区别：1、基于连接与无连接，TCP是有连接的2、对系统资源的要求，（TCP较多，UDP较少）3、UDP程序结构较简单4、流模式和数据报模式5、TCP保证数据正确性，UDP可能丢包，TCP保证数据顺序，UDP不保证"""# import socket## s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)from socket import *import osimport chardet# print(os.getpid())s = socket(AF_INET, SOCK_DGRAM)s.bind(("", 8882))  # 绑定一个IP和端口号addr = ('192.168.2.103', 8881)while True:    data = s.recvfrom(1024)  # 一次接受最大的字节数    print(data[0].decode())    ss = input('请输入聊天内容：')    s.sendto(ss.encode('utf-8'), addr) # python3需要对字符串进行编码变成bytes类型对象s.close()