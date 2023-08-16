#  import numpy as np
cipher = '''qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs. lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf.'''

cl_cipher = "".join([c for c in cipher if c.isalpha()])
print("The clean cipher is")
print(cl_cipher)

print("Cipher length is "+str(len(cl_cipher)))


key = {
        'a': 't',
        'b': 'v',
        'c': 'i',
        'd': 'u',
        'e': 'c',
        'f': 'h',
        'g': 'g',
        'h': 'p',
        'i': 'q',
        'j': 'b',
        'k': 'l',
        'l': 's',
        'm': 'k',
        'n': 'r',
        'o': ' ',
        'p': 'd',
        'q': 'a',
        'r': 'w',
        's': 'f',
        't': 'l',
        'u': 'm',
        'v': 'e',
        'w': 'o',
        'x': 'y',
        'y': 'n',
        'z': ' '
        }

tmp = ""
for t in cl_cipher.lower():
    tmp += key[t]

print(tmp)

result = ""
for i in range(int(len(tmp)/5)):
    result+=tmp[i*5+3]
    result+=tmp[i*5+2]
    result+=tmp[i*5+4]
    result+=tmp[i*5]
    result+=tmp[i*5+1]

print(result)
