f = open("program.txt", "r")

int_dict = {
    "add": "000000",
    "sub": "000001",
    "addi": "000010",
    "mult": "000011",
    "div": "000100",
    "mfhi": "000101",
    "mflo": "000110",
    "and": "000111",
    "or": "001000",
    "sll": "001001",
    "srl": "001010",
    "j": "001011",
    "jal": "001100",
    "jr": "001101",
    "beq": "001110",
    "bne": "001111",
    "bgt": "010000",
    "blt": "010001",
    "move": "010010",
    "li": "010011",
    "la": "010100",
    "lw": "010101",
    "sw": "010110",
    "$0": "00000",
    "$at": "00001",
    "$v0": "00010",
    "$v1": "00011",
    "$a0": "00100",
    "$a1": "00101",
    "$a2": "00110",
    "$a3": "00111",
    "$t0": "01000",
    "$t1": "01001",
    "$t2": "01010",
    "$t3": "01011",
    "$t4": "01100",
    "$t5": "01101",
    "$t6": "01110",
    "$t7": "01111",
    "$t8": "10000",
    "$t9": "10001",
    "$s0": "10010",
    "$s1": "10011",
    "$s2": "10100",
    "$s3": "10101",
    "$s4": "10110",
    "$s5": "10111",
    "$s6": "11000",
    "$s7": "11001",
    "$k0": "11010",
    "$k1": "11011",
    "$gp": "11100",
    "$sp": "11101",
    "$fp": "11110",
    "$ra": "11111"
}


#print(type(list(f.read())))
ints_list = list(f.read().split("\n"))

bin_insts = []
for i in ints_list:
    #print(list(i.split(" ")))
    bin_inst = ""
    for j in list(i.split(" ")):
        #print(j)
        #print(int_dict[j])
        value = int_dict.get(j, 0)
        if value != 0: 
            bin_inst+=int_dict[j]
        else:
            print(str(bin(int(j)))[2:])
            binn = str(str(bin(int(j)))[2:])
            print(str((binn[::-1])))
            bin_inst+=str((binn[::-1]))
            #print("h")
    bin_insts.append(bin_inst)
    
bin32_inst = []
for i in bin_insts:
    z = ""
    for j in range(32-len(i)):
        z+="0"
    #print(len(z))
    #print(len(i))
    bin32 = i+z
    bin32_inst.append(bin32)

bintxt = open("binario.txt", "w")

for i in bin32_inst:
    bintxt.write(i)
    bintxt.write("\n")

bintxt.close

hextxt = open("hex.txt", "w")

for i in bin32_inst:
    binary_string = i
    decimal_representation = int(binary_string, 2)
    hexadecimal_string = hex(decimal_representation)
    hextxt.write(hexadecimal_string)
    hextxt.write("\n")

hextxt.close