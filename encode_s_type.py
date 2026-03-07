def encode_s_type(inst):
    register_mapping = { "x0" : "00000" , "x1" : "00001" , "x2" : "00010" , "x3" : "00011" , "x4" : "00100" , "x5" : "00101" , "x6" : "00110" , 
    "x7" : "00111" , "x8" : "01000" , "x9" : "01001" , "x10" : "01010" , "x11" : "01011" , "x12" : "01100" , "x13" : "01101" , "x14" : "01110" , 
    "x15" : "01111" , "x16" : "10000" , "x17" : "10001" , "x18" : "10010" , "x19" : "10011" , "x20" : "10100" , "x21" : "10101" , "x22" : "10110" , 
    "x23" : "10111" , "x24" : "11000" , "x25" : "11001" , "x26" : "11010" , "x27" : "11011" , "x28" : "11100" , "x29" : "11101" , "x30" : "11110" , 
    "x31" : "11111" }

    s_type_table = { "sb" : { "funct3" : "000" } , "sh" : { "funct3" : "001" } , "sw" : { "funct3" : "010" } }

    opcode = inst["operation"]

    funct3 = s_type_table[opcode]["funct3"]

    rs2 = inst["operands"][0]

    rs1 = inst["operands"][2]

    imm = int(inst["operands"][1])

    if imm > 2047 or imm < -2048:
        return "ERROR: Immediate is incorrect."

    try:
        rs2_binary = register_mapping[rs2]

        rs1_binary = register_mapping[rs1]
    except:

        return "Invalid Operand"

    imm_binary = format(imm % (2^12), "012b")

    imm_high = imm_binary[:7]

    imm_low = imm_binary[7:]

    opcode_bin = "0100011"

    binary = imm_high + rs2_binary + rs1_binary + funct3 + imm_low + opcode_bin

    return binary