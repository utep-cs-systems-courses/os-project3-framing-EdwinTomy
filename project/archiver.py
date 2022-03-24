def files_to_bytes(file_lst):

    # first section stores pointers of to each file
    bytes_arr = [bin(len(file_lst))]
    for i in range(len(file_lst)):
        bytes_arr.append(0)

    for j, file_name in enumerate(file_lst):

        # establishing where this file will be stored
        init_address = len(bytes_arr)
        bytes_arr[j+1] = bin(init_address)

        # stores byte representation of file name and its length
        bytes_arr.append(0)
        file_name_len = 0
        for i in file_name.encode():
            file_name_len += 1
            bytes_arr.append(bin(i))
        bytes_arr[init_address] = bin(init_address+file_name_len)

        # stores byte representation of file content
        content_address = len(bytes_arr)
        bytes_arr.append(0)
        file_content_len = 0
        for i in open(file_name, "rb").read():
            file_content_len += 1
            bytes_arr.append(bin(i))
        bytes_arr[content_address] = bin(file_content_len+content_address)


    return bytes_arr


def bytes_to_files(bytes_arr):

    for j in range(int(bytes_arr[0], 2)):
        init_address = int(bytes_arr[j+1], 2)
        content_address = int(bytes_arr[init_address], 2) + 1

        # read file name
        filename = "new_"
        print('init_address', init_address)
        print('begin', (init_address + 1))
        print('end', (init_address + int(bytes_arr[init_address], 2) + 1))

        for i in bytes_arr[init_address + 1: content_address]:
            filename += chr(int(i, 2))
        print(filename)

        # read file content
        f = open(filename, "w")
        for i in bytes_arr[content_address + 1: int(bytes_arr[content_address], 2) + 1]:
            f.write(chr(int(i, 2)))


byte_arr = files_to_bytes(["hola.txt", "como.txt", "sasageyo.txt", "photo.png"])
bytes_to_files(byte_arr)
