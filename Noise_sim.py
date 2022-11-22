def _add_noise(self,enc_mat):
    import random as rand
    data_illumina = pd.read_csv("InfiniumOmni2-5-8_Chr_20.txt", sep='\t')
    pos_illumina = data_illumina['Position'].tolist()
    pos = self.var.pos
    t = rand.uniform(0,1)
    if pos in pos_illumina:
        for i in enc_mat:
            for j in i:
                if t >= data_illumina.loc[data_illumina['Position'] == pos, 'Call Freq']:
                    print('Add Noise')
                    if j[0] == 0 and j[1] == 0:
                        print('before',j)
                        j[0] = 1
                        print('after',j)
                    elif j[0] == 1 and j[1] == 0:
                        print('before',j)
                        j[0] = 0
                        print('after:',j)
                    elif j[0] == 1 and j[1] == 1:
                        print('before',j)
                        j[1] = 0
                        print('after:',j)


