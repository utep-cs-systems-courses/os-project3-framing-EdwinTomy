def fixed_string_num(num, num_digits=10):

    num = str(num)
    while len(num) < num_digits:
        num = '0' + num
    return num


def archive(file_name_lst):
    arr = bytearray()
    lengths = []

    for file_name in file_name_lst:
        encoded_file_name = bytearray(file_name.encode())
        arr.extend(encoded_file_name)
        file_name_len = len(encoded_file_name)

        with open(file_name, "rb") as file:
            content = file.read()
            arr.extend(bytes(content))
            file_content_len = len(content)

        lengths.insert(0, fixed_string_num(file_name_len))
        lengths.insert(0, fixed_string_num(file_content_len))

    for length in lengths:
        arr[0:0] = bytes(length, 'utf-8')
    arr[0:0] = bytes(fixed_string_num(len(file_name_lst)), 'utf-8')

    return arr


def unarchive(bytes_arr, file_prefix, num_digits=10):

    num_files = int(bytes_arr[:num_digits].decode('utf-8'))
    lengths = []

    for j in range(num_files):
        lengths.append(int(bytes_arr[((2 * j + 1) * num_digits):((2 * j + 2) * num_digits)].decode('utf-8')))
        lengths.append(int(bytes_arr[((2 * j + 2) * num_digits):((2 * j + 3) * num_digits)].decode('utf-8')))

    bytes_arr = bytes_arr[(num_files*2+1)*num_digits:]
    for j in range(num_files):
        file_name = bytes_arr[:lengths[2*j]].decode()
        bytes_arr = bytes_arr[lengths[2*j]:]

        with open(file_prefix + '_' + file_name, "wb") as f:
            f.write(bytes_arr[:lengths[2*j+1]])
            bytes_arr = bytes_arr[lengths[2*j+1]:]

# byte_arr = archive(["image.png"])
# unarchive(byte_arr)

