import random


def main(path, size):

    if size > 40:
        capacity = random.randint(5*size, 10*size)
        numClasses = random.randint(5, 10)
        weights = [random.randint(1,100) for i in range(size)]
    else:
        capacity = random.randint(5*size, 15*size)
        numClasses = random.randint(1, 5)
        weights = [random.randint(1,40) for i in range(size)]

    values = [random.randint(1,500) for i in range(size)]
    classes = [random.randint(1,numClasses) for i in range(size)]
    
    f = open(path, 'w')
    f.write(str(capacity) + "\n")
    f.write(str(numClasses) + "\n")
    f.write(", ".join([str(u) for u in weights]) + "\n")
    f.write(", ".join([str(u) for u in values]) + "\n")
    f.write(", ".join([str(u) for u in classes]) + "\n")
    f.close()



if __name__ == '__main__':
    index = 0
    for i in range(10):
        main("INPUT/INPUT_" + str(index) + ".txt", i*4 + 4)
        index += 1
    for i in range(10):
        main("INPUT/INPUT_" + str(index) + ".txt", i*100 + 100)
        index += 1