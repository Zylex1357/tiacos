import os
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')

if (len(sys.argv) != 4):
    print("Error in th enumber of parameters. We need 3 file names.")
    sys.exit(0)
else:
    print("Matrix 1 in file: ", sys.argv[1])
    print("Matrix 1 in file: ", sys.argv[2])
    print("Matrix result in file: ", sys.argv[3])

try:
    fd_source1 = os.open(sys.argv[1].rstrip(), os.O_RDONLY)
except:
    print("File",sys.argv[1], "not found")
    sys.exit(0)

try:
    fd_source2 = os.open(sys.argv[2].rstrip(), os.O_RDONLY)
except:
    print("File",sys.argv[2], "not found")
    sys.exit(0)

try:
    fd_sum = os.open(sys.argv[3].rstrip(), os.O_CREAT|os.O_WRONLY )
except:
    print("File",sys.argv[3], "cannot be created")
    sys.exit(0)



# Reading the rows and columns
# chunk is a bytestring, and to get the byte into it we need to get its first position
chunk = os.read(fd_source1,1)
rows = chunk[0]
chunk = os.read(fd_source1,1)
cols = chunk[0]

chunk = os.read(fd_source2,1)
if chunk[0] != rows:
    print("Number of rows does not match")
    sys.exit(0)

chunk = os.read(fd_source2,1)
if chunk[0] != cols:
    print("Number of columns does not match")
    sys.exit(0)

os.write (fd_sum, bytes([rows]))
os.write (fd_sum, bytes([cols]))
print (rows,",",cols);

# Reading the matrix
i = 0
while i < rows:
    j = 0
    while j < cols:
       chunk1 = os.read(fd_source1,1)
       chunk2 = os.read(fd_source2,1)
       val = chunk1[0] + chunk2[0]
       os.write (fd_sum, bytes([val]))
       print("(",i,",",j,")=",val)
       j = j + 1
    i = i + 1
		
os.close(fd_source1)
os.close(fd_source2)
os.close(fd_sum)

