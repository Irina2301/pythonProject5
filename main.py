sequence = input("Введите последовательность чисел от 1 до 100 через пробел: ")
sequence_conf = [int(a) for a in sequence.split()]
print(sequence_conf)
def bSort(sequence_conf):
    lengh = len(sequence_conf)
    for i in range(lengh):
        for j in range(0, lengh-i-1):
            if sequence_conf[j] > sequence_conf[j+1]:
                temp = sequence_conf[j]
                sequence_conf[j] = sequence_conf[j+1]
                sequence_conf[j+1] = temp
bSort(sequence_conf)
print(sequence_conf)
def binary_search(sequence_conf,element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if sequence_conf[middle] == element:
        return middle
    elif element < sequence_conf[middle]:
        return binary_search(sequence_conf, element, left, middle - 1)
while True:
    try:
        element = int(input("Введите число от 1 до 100: "))
        if element < 1 or element > 100:
            raise Exception
        break
    except ValueError:
        print("Введены некорректные данные!")
    except Exception:
        print("Введено число больше 100!")
print(binary_search(sequence_conf, element, 0, len(sequence_conf)))









