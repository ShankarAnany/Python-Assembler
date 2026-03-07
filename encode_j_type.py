reg_set = {
"x0":0, "x1":1, "x2":2, "x3":3, "x4":4, "x5":5, "x6":6, "x7":7,
"x8":8, "x9":9, "x10":10, "x11":11, "x12":12, "x13":13, "x14":14, "x15":15,
"x16":16, "x17":17, "x18":18, "x19":19, "x20":20, "x21":21, "x22":22, "x23":23,
"x24":24, "x25":25, "x26":26, "x27":27, "x28":28, "x29":29, "x30":30, "x31":31
}
insts = [

{'format':'i','operation':'addi','operands':['x1','x0','5'],'pc':4},

{'format':'j','operation':'jal','operands':['x5','loop'],'pc':8},

{'format':'i','operation':'addi','operands':['x2','x0','1'],'pc':12},

{'format':'r','operation':'add','operands':['x3','x1','x2'],'pc':16}

]
labels = {
    "loop": 16
}
def encode_j():
    for inst in insts:
        if inst['format']=='j':
            if inst['operands'][1] in labels:
                ra=reg_set[inst['operands'][0]]
                label=inst['operands'][1]
                imm=labels[label]-inst['pc']

                ra=format(ra,'05b')
                imm=format(imm,'021b')
                encoded_inst=imm[0:1]+imm[10:20]+imm[9:10]+imm[1:9]+ra+'1101111'

                return encoded_inst
            else:
                print("Label not found")
encoded=encode_j()
print (encoded)