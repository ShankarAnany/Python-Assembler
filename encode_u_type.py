def encode_u_type(inst):
    register_mapping = { "x0" : "00000" , "x1" : "00001" , "x2" : "00010" , "x3" : "00011" , "x4" : "00100" , "x5" : "00101" , "x6" : "00110" , 
    "x7" : "00111" , "x8" : "01000" , "x9" : "01001" , "x10" : "01010" , "x11" : "01011" , "x12" : "01100" , "x13" : "01101" , "x14" : "01110" , 
    "x15" : "01111" , "x16" : "10000" , "x17" : "10001" , "x18" : "10010" , "x19" : "10011" , "x20" : "10100" , "x21" : "10101" , "x22" : "10110" , 
    "x23" : "10111" , "x24" : "11000" , "x25" : "11001" , "x26" : "11010" , "x27" : "11011" , "x28" : "11100" , "x29" : "11101" , "x30" : "11110" , 
    "x31" : "11111" }

    u_type_table = { "lui" : { "opcode" : "0110111" } , "auipc" : { "opcode" : "0010111" } }

    opcode = inst["operation"]
    
    rd = inst["operands"][0]
    
    imm = int(inst["operands"][1])

    if imm > 524287 or imm < -534288:
        return "ERROR: Immediate is incorrect."

    try:
        rd_binary = register_mapping[rd]
    
    except:
        return "Invalid Operand"

    imm_binary = format(imm % (2^20), "020b")

    opcode_binary = u_type_table[opcode]["opcode"]

    binary = imm_binary + rd_binary + opcode_binary

    return binary