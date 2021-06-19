
#3.8.5
#Writing
file_handle =open("my_bin_file.bin", "wb")
msg = "Hi there"
arr = bytearray(msg.encode())
file_handle.write(arr)
file_handle.close()

#Reading
file_handle = open("my_bin_file.bin","rb")
msg = file_handle.read()
print(msg)
print(msg.decode())

################################
#3.8.7
file_handle = open("first_file.txt","w+")
print('Closed or Not - ',file_handle.closed)
print('Mode : ',file_handle.mode)
print('Name : ',file_handle.name)
