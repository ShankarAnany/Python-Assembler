def encode_r_type(inst):
    register_map = {"zero":"00000","ra":"00001","sp":"00010","gp":"00011","tp":"00100","t0":"00101","t1":"00110","t2":"00111",
    "s0":"01000","s1":"01001","a0":"01010","a1":"01011","a2":"01100","a3":"01101","a4":"01110","a5":"01111",
    "a6":"10000","a7":"10001","s2":"10010","s3":"10011","s4":"10100","s5":"10101","s6":"10110","s7":"10111","s8":"11000","s9":"11001",
    "s10":"11010","s11":"11011","t3":"11100","t4":"11101","t5":"11110","t6":"11111"
        }
    r_type_table = {
    "add":{"funct3": "000", "funct7": "0000000"},"sub":{"funct3": "000", "funct7": "0100000"},"sll":{"funct3": "001", "funct7": "0000000"},
    "slt":{"funct3": "010", "funct7": "0000000"},"sltu":{"funct3": "011", "funct7": "0000000"},"xor":{"funct3": "100", "funct7": "0000000"},
    "srl":{"funct3": "101", "funct7": "0000000"},"or":{"funct3": "110", "funct7": "0000000"},"and":{"funct3": "111", "funct7": "0000000"}
    }

    opcode=inst["opcode"]
    func3=r_type_table[opcode]["func3"]
    func7=r_type_table[opcode]["func7"]
    rd=inst["operands"]["rd"]
    rs1=inst["operands"]["rs1"]
    rs2=inst["operands"]["rs2"]
    rd_b=register_map[rd]
    rs1_b=register_map[rs1]
    rs2_b=register_map[rs2]
    opcode_bin = "0110011"
    binary = func7+rs2_b+rs1_b+func3+rd_b+opcode_bin
    return binary