def files_to_bytes(file_lst):

    # first section stores pointers of to each file
    int_arr = [len(file_lst)]
    for i in range(len(file_lst)):
        int_arr.append(0)

    for j, file_name in enumerate(file_lst):

        # establishing where this file will be stored
        init_address = len(int_arr)
        int_arr[j+1] = init_address

        # stores byte representation of file name and its length
        int_arr.append(0)
        file_name_len = 0
        for i in file_name.encode():
            file_name_len += 1
            int_arr.append(i)
        int_arr[init_address] = init_address+file_name_len

        # stores byte representation of file content
        content_address = len(int_arr)
        int_arr.append(0)
        file_content_len = 0
        for i in open(file_name, "rb").read():
            file_content_len += 1
            int_arr.append(i)
        int_arr[content_address] = file_content_len+content_address

    bytes_arr = bytearray()
    for i in int_arr:
        bytes_arr += i.to_bytes(2, 'big')
    return bytes_arr


def bytes_to_files(int_arr):

    bytes_arr = []
    for i in range(len(int_arr)//2):
        bytes_arr.append(int_arr[2*i] * 2**8 + int_arr[2*i+1])

    for j in range(bytes_arr[0]):
        init_address = bytes_arr[j+1]
        content_address = bytes_arr[init_address]+ 1

        # read file name
        filename = "new_"
        for i in bytes_arr[init_address + 1: content_address]:
            filename += chr(i)

        # read file content
        f = open(filename, "w")
        for i in bytes_arr[content_address + 1: bytes_arr[content_address]+ 1]:
            f.write(chr(i))


byte_arr = files_to_bytes(["fiesta_salsa.txt", "francesco.txt", "sasageyo.txt"])
bytes_to_files(byte_arr)
