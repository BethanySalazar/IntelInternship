"""
...And Make it Double

Create two functions ---
Encrypt and Decrypt, that use the ciphering method
that Lurk used to encipher these logs. He's put the logs into a
encrypted_logs.txt file.
--Use the double transposition cipher with the key words FIRE and ROME--

Riddle 1:
You can see that your logs might look a little... vague. That
might be an understatement.
The point is, you cracked my first cipher, but that was easy.
Now, prepare for trouble. And make it **DOUBLE**.

- Double Transposition Cipher -

Riddle 2: (THIS ONE FIRST!)
Multiplies; but never breeds, Uses air; but never breathes.
Consumes much; will never eat, Often measured by its heat.
- FIRE -

Riddle 3:
My name is short, yet my history long.
Once I was the greatest one, but now, all but my core is gone.
Known for might and buildings and art,
At last I fell, now stories they tell.
Who am I?
- ROME -
"""
# Open the file with read only permit
f = open('encrypted_logs.txt', '+r')
# Read the first line
line = f.readline()
# If the file is not empty keep reading line one at a time
# till the file is empty
while line:
    print(line)
    line = f.readline()
f.close()

# used to make extract the data
def encryptedLogs(info):
    name, hours, qpoints = info.split("\t")
    return Student(name, hours, qpoints)

def decipher():
    encryptedCode = open("encrypted_logs.txt", "r+")

    pList = []
    for line in encryptedCode:
        pList.append(makeStudent(line))
    encryptedCode.close()
    return pList



print(decipher())
