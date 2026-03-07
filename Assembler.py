import encode_r_type
import encode_i_type
import encode_s_type
import encode_b_type
import encode_u_type
import encode_j_type
import file_parsing
import sys

def main():
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    # first pass of assembler
    insts, labels = file_parsing.parse_file(in_file)
    insts_b = []

    # main program loop
    for inst in insts:

        inst_b = ""
        if inst["format"] == "r":
            inst_b = encode_r_type.encode_r_type(inst)
        elif inst["format"] == "i":
            inst_b = encode_i_type.encode_i_type(inst)
        elif inst["format"] == "s":
            inst_b = encode_s_type.encode_s_type(inst)
        elif inst["format"] == "b":
            inst_b = encode_b_type.encode_b_type(inst, labels)
        elif inst["format"] == "u":
            inst_b = encode_u_type.encode_u_type(inst)
        elif inst["format"] == "j":
            inst_b = encode_j_type.encode_j(inst, labels)
        elif inst["format"] == "error":
            print(f"Invalid instruction on line {inst["line_num"]}")
        
        if inst_b.isdigit():
            insts_b.append(inst_b)
        else:
            insts_b.append("")
            if inst["format"] != "error":
                print(inst_b, f"on line {inst["line_num"]}")
        
    if "00000000000000000000000001100011" not in insts_b:
        print("Virtual Halt Instruction Doesn't Exist")
    
    f = open(out_file, "w")
    for i in range(len(insts_b)):
        f.write(insts_b[i] + ("\n"*(i != len(insts_b) - 1)))
    f.close()

if __name__ == "__main__":
    main()