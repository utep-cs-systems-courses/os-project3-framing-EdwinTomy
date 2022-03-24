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
        bytes_arr[init_address] = bin(file_name_len)


        # stores byte representation of file content
        content_address = len(bytes_arr)
        bytes_arr.append(0)
        file_content_len = 0
        for i in open(file_name, "rb").read():
            file_content_len += 1
            bytes_arr.append(bin(i))
        bytes_arr[content_address] = bin(file_content_len)

    print(chr(int((bytes_arr[1969]), 2)))
    return bytes_arr


def bytes_to_files(bytes_arr):

    for j in range(int(bytes_arr[0], 2)):
        init_address = int(bytes_arr[j+1], 2)

        # read file name
        filename = "new_"
        print('init_address', init_address)
        print('begin', (init_address + 1))
        print('end', (init_address + int(bytes_arr[init_address], 2) + 1))

        for i in bytes_arr[init_address + 1: init_address + int(bytes_arr[init_address], 2) + 1]:
            filename += chr(int(i, 2))
        print(filename)


        # read file content
        f = open(filename, "w")
        end_content = len(byte_arr) if j == int(bytes_arr[0], 2)-1 else int(bytes_arr[j+2], 2)

        print('begin', (init_address + int(bytes_arr[init_address], 2) + 1), chr(int(byte_arr[init_address + int(bytes_arr[init_address], 2) + 1], 2)))
        print('end', (end_content), chr(int((byte_arr[end_content-1]), 2)))


        for i in bytes_arr[init_address + int(bytes_arr[init_address], 2) + 1:end_content]:
            f.write(chr(int(i, 2)))


byte_arr = files_to_bytes(["fiesta_salsa.txt", "francesco.txt", "sasageyo.txt"])
bytes_to_files(byte_arr)
