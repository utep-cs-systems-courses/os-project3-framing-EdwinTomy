def text_to_bytes(file_name):
    
    # stores byte representation of file name and its length
    bytes_arr = [0]
    file_name_len = 0
    for i in file_name.encode():
        file_name_len += 1
        bytes_arr.append(bin(i))
    bytes_arr[0] = bin(file_name_len)

    # stores byte representation of file content and its length
    bytes_arr.append(0)
    file_content_len = 0
    for i in open(file_name, "rb").read():
        file_content_len += 1
        bytes_arr.append(bin(i))
    bytes_arr[file_name_len+1] = bin(file_content_len)

    return bytes_arr


def bytes_to_text(bytes_arr):

    # read file name
    filename = "new_"
    for i in bytes_arr[1:int(bytes_arr[0], 2) + 1]:
        filename += chr(int(i, 2))

    # read file content
    f = open(filename, "w")
    for i in bytes_arr[int(bytes_arr[0], 2) + 2:]:
        f.write(chr(int(i, 2)))


byte_arr = text_to_bytes("fiesta_lyrics.txt")
print(byte_arr)
bytes_to_text(byte_arr)
