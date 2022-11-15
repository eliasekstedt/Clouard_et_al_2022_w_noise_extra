from concurrent.futures import process
import matplotlib.pyplot as plt
import numpy as np
import math
import statistics

with open('InfiniumOmni2-5-8_Chr_20.txt') as f:
    no_records = 0
    call_freqs = []
    no_call_freqs_l9725 = 0
    no_call_freqs_l975 = 0
    no_call_freqs_l98 = 0
    no_call_freqs_l99 = 0
    no_minor_freq_l1 = 0
    no_minor_freq_m40 = 0
    location = []
    minor_freqs = []
    lines_minor_freqs_l1 = []
    lines_minor_freqs_m40 = []
    call_freqs_and_location = []
    for line in f:
        processed_line = line.strip().split()
        if processed_line[7] != '1' and processed_line[0] != 'Index':
            call_freqs.append(float(processed_line[7]))
            location.append(int(processed_line[3]))
            minor_freqs.append(float(processed_line[8]))
            if float(processed_line[7]) < 0.9725:
                no_call_freqs_l9725 += 1
            if float(processed_line[7]) < 0.975:
                no_call_freqs_l975 += 1
            if float(processed_line[7]) < 0.98:
                no_call_freqs_l98 += 1
            if float(processed_line[7]) < 0.99:
                no_call_freqs_l99 += 1
            if float(processed_line[8]) < 0.01:
                no_minor_freq_l1 += 1
                lines_minor_freqs_l1.append(processed_line)
            if float(processed_line[8]) > 0.4:
                no_minor_freq_m40 += 1
                lines_minor_freqs_m40.append(processed_line)
            no_records += 1

print('Mean Call Rate:                               ', statistics.mean(call_freqs))
print('Standard Deviation:                           ', statistics.stdev(call_freqs))
print('No of records:                                ', no_records)
# print('No of records with callrate < 97.25%:         ', no_call_freqs_l9725)
# print('No of records with callrate < 97.5%:          ', no_call_freqs_l975)
# print('No of records with callrate < 98%:            ', no_call_freqs_l98)
# print('No of records with callrate < 99%:            ', no_call_freqs_l99)
# print('No of records with minor freq < 1%:            ', no_minor_freq_l1)
# print('No of records with minor freq > 40%:            ', no_minor_freq_m40)


corr_call_minor = np.corrcoef(call_freqs, minor_freqs)
print('Correlation between Call freq and minor freq: ',corr_call_minor[0][1])

# plt.figure(1) 
# plt.plot(location, call_freqs, 'o')
# plt.title('call rates over chromosome 20')
# plt.xlabel('Location (bp)')
# plt.ylabel('Call rate')
# plt.grid()

# plt.figure(2)
# #plt.pcolormesh([call_freqs]*2, cmap='Greys', shading='gouraud')
# plt.imshow(call_freqs_and_location, cmap='hot', interpolation='nearest')
# #plt.set_yticks([])
# #plt.set_xlim(0, max(location))
# plt.title('heat map of call rate over all values')
# plt.xlabel('record number')
# plt.ylabel('Call rate')

# plt.figure(3)
weights = np.ones_like(call_freqs)/float(len(call_freqs))
(n, bins, patches) = plt.hist(call_freqs, bins=[0.97,0.9725,0.975,0.9775,0.98,0.9825,0.985,0.9875,0.99,0.9925,0.995,0.9975,0.9980, 0.9985, 0.9990, 0.9995,1], weights=weights)
plt.title('Call rate distribution chromosome 20')
plt.xlabel('Call rate')
plt.ylabel('count (normalized)')
plt.grid()

plt.show()

print(n)
print(bins)