from copy import deepcopy


def rebuild_message(parts):
    array = deepcopy(parts)
    out=""
    for i in range(len(array)):

        if len(array) == len(parts):
            match = [s for s in array if 'A' in s]
            out+=match[0]
            array.remove(match[0])

        elif len(array) == 1 and 'Z' in array[0]:
            out = out[:-1]
            out+=array[0]

        else:
            match =  [s for s in array if out[-1] in s]
            out = out[:-1]
            out+=match[0]
            array.remove(match[0])
    print(out)



def main():
    msg1 = ['Ab', 'bcZ']
    msg2 = ['*______#', 'X-+-+-+-+Z','A.....*', '#------------X']
    msg3 = ['E--------------Z', 'A________E']


    rebuild_message(msg1)
    rebuild_message(msg2)
    rebuild_message(msg3)

if __name__ == '__main__':
    main()
