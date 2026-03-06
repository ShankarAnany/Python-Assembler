def encode_r_type(inst):
    register_map = {"x0":"00000","x1":"00001","x2":"00010","x3":"00011","x4":"00100","x5":"00101","x6":"00110","x7":"00111",
    "x8":"01000","x9":"01001","x10":"01010","x11":"01011","x12":"01100","x13":"01101","x14":"01110","x15":"01111",
    "x16":"10000","x17":"10001","x18":"10010","x19":"10011","x20":"10100","x21":"10101","x22":"10110","x23":"10111","x24":"11000","x25":"11001",
    "x26":"11010","x27":"11011","x28":"11100","x29":"11101","x30":"11110","x31":"11111"
    }
    r_type_table = {
    "add":{"funct3": "000", "funct7": "0000000"},"sub":{"funct3": "000", "funct7": "0100000"},"sll":{"funct3": "001", "funct7": "0000000"},
    "slt":{"funct3": "010", "funct7": "0000000"},"sltu":{"funct3": "011", "funct7": "0000000"},"xor":{"funct3": "100", "funct7": "0000000"},
    "srl":{"funct3": "101", "funct7": "0000000"},"or":{"funct3": "110", "funct7": "0000000"},"and":{"funct3": "111", "funct7": "0000000"}
    }

    opcode=inst["opcode"]
    func3=r_type_table[opcode]["func3"]
    func7=r_type_table[opcode]["func7"]
    rd=inst["operands"][0]
    rs1=inst["operands"][1]
    rs2=inst["operands"][2]
    rd_b=register_map[rd]
    rs1_b=register_map[rs1]
    rs2_b=register_map[rs2]
    opcode_bin = "0110011"
    binary = func7+rs2_b+rs1_b+func3+rd_b+opcode_bin
    return binary