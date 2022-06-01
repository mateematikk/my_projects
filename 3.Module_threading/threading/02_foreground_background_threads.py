import threading

from multithreading.count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('started main')

    ints = read_ints('..\\data\\1Kints.txt')
    t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)
    t1.start()
   # count_three_sum(ints)

    #print('What are we waiting for?')
    #print(input('How are you? [y,n]'))
    print(input('What is your name?'))

    t1.join()
    print('ended main')