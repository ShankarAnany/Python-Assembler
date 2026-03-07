def encode_i_type(inst):
    i_type_table = {"addi":{"opcode":"0010011","func3":"000"},"sltiu":{"opcode":"0010011","func3":"011"},
                    "lw":{"opcode":"0000011","func3":"010"},"jalr":{"opcode":"1100111","func3":"000"}
                   }
    register_map = {"x0":"00000","x1":"00001","x2":"00010","x3":"00011","x4":"00100","x5":"00101","x6":"00110","x7":"00111",
    "x8":"01000","x9":"01001","x10":"01010","x11":"01011","x12":"01100","x13":"01101","x14":"01110","x15":"01111",
    "x16":"10000","x17":"10001","x18":"10010","x19":"10011","x20":"10100","x21":"10101","x22":"10110","x23":"10111","x24":"11000","x25":"11001",
    "x26":"11010","x27":"11011","x28":"11100","x29":"11101","x30":"11110","x31":"11111"
    }
    rd=inst["operands"][0]

    if inst["operation"] == "lw":
        rs1=inst["operands"][2]
        imm=int(inst["operands"][1])
    else:
        rs1=inst["operands"][1]
        imm=int(inst["operands"][2])
    try:
        rd_b=register_map[rd]
        rs1_b=register_map[rs1]
    except:
        return "Invalid Operand"
    s=inst["operation"]
    func3=i_type_table[s]["func3"]
    opcode=i_type_table[s]["opcode"]
    if imm<-2048:
        return "Imm value not valid"
    if imm>2047:
        return "Imm value not valid"
    if imm>=0:
        imm_b=format(imm,"012b") 
    else:
        imm_b=format((1<<12)+imm,'012b')
    binary=imm_b+rs1_b+func3+rd_b+opcode 
    return binary      
        
