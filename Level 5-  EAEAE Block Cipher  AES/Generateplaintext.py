r = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
plain = []
k=0
i=0
while k<8:
    temp = []
    i=0
    while i<8:
        for j in range(16):
            st = 'ff'*k + r[i]+r[j] + 'ff'*(8-1-k)
            temp.append(st)
        i=i+1    
    plain.append(temp)
    k=k+1

file = open('plaintexts1.txt','w')
for i in plain:
    st = ' '.join(i) + '\n'
    file.write(st)
file.close()