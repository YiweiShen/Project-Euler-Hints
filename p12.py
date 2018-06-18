from queue import Queue
from threading import Thread


def generate_triangle_num(seq):
    sum = 0
    for a in range(1, seq):
        sum += a
    return sum


def do_stuff(q):
    while True:
        b = generate_triangle_num(q.get())
        print(b)
        if cal_divisor_num(b) > 500:
            print(str(b) + ':' + str(cal_divisor_num(b)))
            break
        q.task_done()


q = Queue(maxsize=0)
num_threads = 1000


def cal_divisor_num(num):
    sum = 0
    for a in range(2, num):
        if num % a == 0:
            sum += 1
    return sum + 2


def worker():
    for a in range(3500, 99999999):
        b = generate_triangle_num(a)
        print(b)
        if cal_divisor_num(b) > 500:
            print(str(b) + ':' + str(cal_divisor_num(b)))
            break


if __name__ == '__main__':
    for i in range(num_threads):
        worker = Thread(target=do_stuff, args=(q,))
        worker.setDaemon(True)
        worker.start()

    for x in range(3500, 999999):
        q.put(x)

    q.join()




