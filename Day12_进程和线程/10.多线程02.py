"""线程：是可以共享全局变量的"""import threadingfrom time import sleepticket = 1000def func1():    global ticket    for i in range(100):        sleep(0.1)        ticket -= 1## def func2():#     global ticket#     for i in range(100):#         ticket -= 1if __name__ == '__main__':    t1 = threading.Thread(target=func1, name='th1')    t2 = threading.Thread(target=func1, name='th2')    t1.start()    t2.start()    t1.join()    t2.join()    print('最后money：', ticket)