

# with open('InfiniumOmniExpress24_LocusReport.txt') as f:
#     with open('Pos.txt') as x:
#         chr20_lines = []
#         for line_f in f:
#             processed_line_f = line_f.strip().split()
#             if processed_line_f[2] == '20':
#                 if float(processed_line_f[7]) != 1:
#                     for line_x in x:
#                         processed_line_x = line_x[1:].split()
#                         if int(processed_line_f[3]) == int(processed_line_x[0]):
#                             chr20_lines.append(processed_line_f)

# f = open("InfiniumOmniExpress24_Chr_20.txt", "x")
# f.write('Index	Name	Chr	Position	AA Freq	AB Freq	BB Freq	Call Freq	Minor Freq')
# f.write('\n')
# for i in chr20_lines:
#     for j in i:
#         f.write(j)
#         f.write('\t')
#     f.write('\n')

with open('InfiniumOmni2-5-8_LocusReport.txt') as f:
    with open('Pos.txt') as x:
        x_lines = x.readlines()
        chr20_2_5_8 = []
        for line_f in f:
            processed_line_f = line_f.strip().split()
            if processed_line_f[2] == '20':
                if float(processed_line_f[7]) != 1:
                    next((x for x in x_lines if x.value == value), None)
                    chr20_2_5_8.append(processed_line_f)

print(chr20_2_5_8)

f = open("InfiniumOmni2-5-8_Chr_20.txt", "x")
f.write('Index	Name	Chr	Position	AA Freq	AB Freq	BB Freq	Call Freq	Minor Freq')
f.write('\n')
for i in chr20_2_5_8:
    for j in i:
        f.write(j)
        f.write('\t')
    f.write('\n')
