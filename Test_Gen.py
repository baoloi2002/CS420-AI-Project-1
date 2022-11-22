import random


def main(path, size):

    if size > 40:
        capacity = random.randint(30*size, 40*size)
        numClasses = random.randint(5, 10)
        weights = [random.randint(1,100) for i in range(size)]
    else:
        capacity = random.randint(10*size, 20*size)
        numClasses = min(random.randint(3, 5), size)
        weights = [random.randint(1,50) for i in range(size)]

    values = [random.randint(1,500) for i in range(size)]
    classes = [random.randint(1,numClasses) for i in range(size)]
    for i in range(numClasses):
        classes[i] = i+1
    random.shuffle(classes)
    
    
    f = open(path, 'w')
    f.write(str(capacity) + "\n")
    f.write(str(numClasses) + "\n")
    f.write(", ".join([str(u) for u in weights]) + "\n")
    f.write(", ".join([str(u) for u in values]) + "\n")
    f.write(", ".join([str(u) for u in classes]) + "\n")
    f.close()

def bigtest(path, size):

    capacity = random.randint(5*size, 6*size)
    numClasses = 10
    weights = [random.randint(5,10) for i in range(size)]
    values = [random.randint(1,10) for i in range(size)]
    classes = [random.randint(1,numClasses) for i in range(size)]

    for i in range(numClasses):
        classes[i] = i+1
    random.shuffle(classes)
    
    
    f = open(path, 'w')
    f.write(str(capacity) + "\n")
    f.write(str(numClasses) + "\n")
    f.write(", ".join([str(u) for u in weights]) + "\n")
    f.write(", ".join([str(u) for u in values]) + "\n")
    f.write(", ".join([str(u) for u in classes]) + "\n")
    f.close()


if __name__ == '__main__':
    index = 0
    for i in range(5):
        bigtest("BigTest/INPUT_" + str(index) + ".txt", 1000)
        index += 1

"""
    for i in range(10):
        main("INPUT/INPUT_" + str(index) + ".txt", i*4 + 4)
        index += 1
    for i in range(10):
        main("INPUT/INPUT_" + str(index) + ".txt", i*100 + 100)
        index += 1
"""
    