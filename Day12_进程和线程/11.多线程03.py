"""GIL:全局解释器锁只要涉及到共享数据，就需要加锁，线程安全。"""from threading import Threadn = 0def task1():    global n    for i in range(1000000):        n += 1    print('------>task1中的n值是：', n)def task2():    global n    for i in range(1000000):        n += 1    print('------>task2中的n值是：', n)if __name__ == '__main__':    t1 = Thread(target=task1)    t2 = Thread(target=task1)    t1.start()    t2.start()    t1.join()    t2.join()    print('最后打印n:', n)