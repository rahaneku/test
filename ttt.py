# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading, time

def print_cube(num): 
    while True:
        print("Cube: {}".format(num * num * num))
        time.sleep(1)

def print_square(num):
    while True:
        print("Square: {}".format(num * num))
        time.sleep(1)

if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_square, args=(20,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()


    print("Done!")

