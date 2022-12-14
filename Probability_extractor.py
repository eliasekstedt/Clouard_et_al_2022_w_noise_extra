import vcf
import xlsxwriter

probs = {}

vcf_reader = vcf.Reader(open('data/Result_files/Clouard_2022_noise/IMP.chr20.pooled.imputed.vcf', 'r'))

workbook = xlsxwriter.Workbook('imputation_probabilities.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 1
samples = vcf_reader.samples
for i in samples:
    worksheet.write(row,column,i)
    column += 1

roww = 1
for record in vcf_reader:
    columnn = 1
    record_str = str(record)
    record_str = record_str[6:]
    worksheet.write(roww,0,record_str)
    for sample in samples:
        call_data = record.genotype(sample)
        call_str = str(call_data.data)
        pos = 0
        for s in call_str:
            if s == '[':
                startpos = pos
            elif s == ']':
                endpos = pos
            pos += 1
        call_str_fnsh = call_str[startpos+1:endpos]
        worksheet.write(roww, columnn, call_str_fnsh)
        columnn += 1

    roww += 1
        
        
workbook.close()