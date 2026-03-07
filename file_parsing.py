## Constants
reg_set = {"zero": 0, "ra": 1, "sp": 2, "gp": 3, "tp": 4, "t0": 5, "t1": 6, "t2": 7, "s0": 8, "fp": 8, "s1": 9, "a0": 10,
    "a1": 11, "a2": 12, "a3": 13, "a4": 14, "a5": 15, "a6": 16, "a7": 17, "s2": 18, "s3": 19, "s4": 20, "s5": 21, "s6": 22,
    "s7": 23, "s8": 24, "s9": 25, "s10": 26, "s11": 27, "t3": 28, "t4": 29, "t5": 30, "t6": 31,}
r_type = ["add", "sub", "slt", "sltu", "xor", "sll", "srl", "or", "and"]
i_type = ["lw", "addi", "sltiu", "jalr"]
s_type = ["sw"]
b_type = ["beq", "bne", "bge", "bgeu", "blt", "bltu"]
u_type = ["auipc", "lui"]
j_type = ["jal"]

def parse_file(file_name):
    insts = []
    labels = {}

    file = open(file_name, "r")
    lines  = file.readlines()

    if "beq zero,zero,0x00000000" not in lines:
        print("Virtual Halt Does'nt Exist")
    elif lines[-1] != "beq zero,zero,0x00000000":
        print("Virtual Halt is not last instruction")
    
    pc = 0
    line_num = 0
    for line in lines:
        line_num += 1
        # ignore empty lines
        if line == "\n":
            print("e")
            continue

        # update program counter
        pc += 4

        # remove , ( ) for easier splitting
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
        else:
            instr["format"] = "error"

        if instr["format"] != "error":
            instr["operation"] = line[0]
            instr["operands"] = line[1:]

            for i in range(len(instr["operands"])):
                if instr["operands"][i] in reg_set.keys():
                    instr["operands"][i] = "x" + str(reg_set[instr["operands"][i]])

        instr["pc"] = pc
        instr["line_num"] = line_num
        insts.append(instr)

    file.close()
    return insts, labels
