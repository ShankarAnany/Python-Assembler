
reg_set = {
"x0":0, "x1":1, "x2":2, "x3":3, "x4":4, "x5":5, "x6":6, "x7":7,
"x8":8, "x9":9, "x10":10, "x11":11, "x12":12, "x13":13, "x14":14, "x15":15,
"x16":16, "x17":17, "x18":18, "x19":19, "x20":20, "x21":21, "x22":22, "x23":23,
"x24":24, "x25":25, "x26":26, "x27":27, "x28":28, "x29":29, "x30":30, "x31":31
}
insts =[
{'format':'i','operation':'addi','operands':['x1','x0','5'],'pc':4},

{'format':'i','operation':'addi','operands':['x2','x0','10'],'pc':8},

{'format':'b','operation':'beq','operands':['x1','x2','loop'],'pc':12},

{'format':'i','operation':'addi','operands':['x3','x0','1'],'pc':16},

{'format':'i','operation':'addi','operands':['x4','x0','2'],'pc':20},

{'format':'r','operation':'add','operands':['x5','x1','x2'],'pc':24}
]
labels = {
    "loop": 24
}
def encode_b(instruction,rs1,rs2,imm):
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


def convert_to_binary():
    for inst in insts:
        if inst['format']== 'b':
            if inst['operands'][2] in labels:
                label=inst['operands'][2]
                imm=labels[label]-inst['pc']

                if -2048<=imm<=2047:
                    rs1=reg_set[inst['operands'][0]]
                    rs2=reg_set[inst['operands'][1]]
                    rs1=format(rs1,'05b')
                    rs2=format(rs2,'05b')
                    imm=format(imm,'013b')
                    encoded=encode_b(inst['operation'],rs1,rs2,imm)
                    print(encoded)
                else:
                    print("Immediate out of range")
            else:
                print("Label not found")
                
            

convert_to_binary()