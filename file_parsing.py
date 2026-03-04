r_type = ["add", "sub", "slt", "sltu", "xor", "sll", "srl", "or", "and"]
i_type = ["lw", "addi", "sltiu", "jalr"]
s_type = ["sw"]
b_type = ["beq", "bne", "bge", "bgeu", "blt", "bltu"]
u_type = ["auipc", "lui"]
j_type = ["jal"]

file_name = "test_case_1_in.txt"
file = open(file_name, "r")

insts = []
labels = {}

lines  = file.readlines()
pc = 0

for line in lines:

    if line == "":
        continue

    pc += 4

    line = line.replace(",", " ")
    line = line.replace("(", " ")
    line = line.replace(")", " ")
    line = line.split()

    # label handling
    if line[0][-1] == ":":
        labels[line[0][:-1]] = pc
        line.pop(0)

    instr = {}

    # handle instruction format
    if line[0] in r_type:
        instr["format"] = "r"
    elif line[0] in i_type:
        instr["format"] = "i"
    elif line[0] in s_type:
        instr["format"] = "s"
    elif line[0] in b_type:
        instr["format"] = "b"
    elif line[0] in u_type:
        instr["format"] = "u"
    elif line[0] in j_type:
        instr["format"] = "j"

    instr["operation"] = line[0]
    instr["operands"] = line[1:]

    insts.append(instr)


print(labels)
print(insts)