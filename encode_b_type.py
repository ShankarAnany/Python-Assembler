reg_set = {"zero": 0, "ra": 1, "sp": 2, "gp": 3, "tp": 4, "t0": 5, "t1": 6, "t2": 7, "s0": 8, "fp": 8, "s1": 9, "a0": 10,
    "a1": 11, "a2": 12, "a3": 13, "a4": 14, "a5": 15, "a6": 16, "a7": 17, "s2": 18, "s3": 19, "s4": 20, "s5": 21, "s6": 22,
    "s7": 23, "s8": 24, "s9": 25, "s10": 26, "s11": 27, "t3": 28, "t4": 29, "t5": 30, "t6": 31,}

def encode_b_type(instruction,rs1,rs2,imm):
    b_type_funct3 = {
    "beq":  "000", 
    "bne":  "001",   
    "blt":  "100",
    "bge":  "101",   
    "bltu": "110",
    "bgeu": "111",   
}
    match instruction:
        case "beq":
            encoded_inst=imm[0:1]+imm[2:8]+rs2+rs1+b_type_funct3["beq"]+imm[8:12]+imm[1:2]+"1100011"
        case "bne":
            encoded_inst=imm[0:1]+imm[2:8]+rs2+rs1+b_type_funct3["bne"]+imm[8:12]+imm[1:2]+"1100011"
        case "blt":
            encoded_inst=imm[0:1]+imm[2:8]+rs2+rs1+b_type_funct3["blt"]+imm[8:12]+imm[1:2]+"1100011"
        case "bge":
            encoded_inst=imm[0:1]+imm[2:8]+rs2+rs1+b_type_funct3["bge"]+imm[8:12]+imm[1:2]+"1100011"
        case "bltu":
            encoded_inst=imm[0:1]+imm[2:8]+rs2+rs1+b_type_funct3["bltu"]+imm[8:12]+imm[1:2]+"1100011"
        case "bgeu":
            encoded_inst=imm[0:1]+imm[2:8]+rs2+rs1+b_type_funct3["bgeu"]+imm[8:12]+imm[1:2]+"1100011"
    
    return encoded_inst


def convert_to_binary(rs1,rs2,imm):
    rs1=format(rs1,'05b')
    rs2=format(rs2,'05b')
    imm=format(imm,'012b')
    return rs1,rs2,imm
    



def entry():
    ent_inst=input("Enter instruction : ")
    part_inst=ent_inst.split(",")
    instruction=part_inst[0]
    rs1=int(reg_set[part_inst[1]])
    rs2=int(reg_set[part_inst[2]])
    imm=int(part_inst[3])
    rs1,rs2,imm=convert_to_binary(rs1,rs2,imm)
    print(rs1," ",rs2," ",imm," ")
    print(encode_b_type(instruction,rs1,rs2,imm))

entry()