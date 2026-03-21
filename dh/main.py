from multiprocessing import Process, Queue
import random
from sympy import primitive_root
import dh

def a_proc(q_a_b, q_b_a):
    print("Generating n and g...")
    n = dh.get_prime()
    g = primitive_root(n)
    print(f"A sending n ({n}) and g ({g}) to B...")

    q_a_b.put(n)
    q_a_b.put(g)

    x = random.randint(100000, 999999)
    X = pow(g,x,n)
    print(f"A sending X ({X}) to B...")
    q_a_b.put(X)

    Y = q_b_a.get()
    k = pow(Y,x,n)
    print(f"A session key: {k}")

def b_proc(q_a_b, q_b_a):
    n = q_a_b.get()
    g = q_a_b.get()
    X = q_a_b.get()

    y = random.randint(100000, 999999)
    Y = pow(g, y, n)
    print(f"B sending Y ({Y}) to A...")
    q_b_a.put(Y)

    k = pow(X,y,n)
    print(f"B session key: {k}")

def main():
    q_a_b = Queue()
    q_b_a = Queue()

    a = Process(target=a_proc, args=(q_a_b, q_b_a))
    b = Process(target=b_proc, args=(q_a_b, q_b_a))

    a.start()
    b.start()

    a.join()
    b.join()

if __name__ == "__main__":
    main()
