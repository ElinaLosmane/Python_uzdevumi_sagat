"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) kādus ciparus jūs ziniet?
2) kādus romiešu ciparus ziniet? I V C M X L D
3) kas ir klase?
klase ir prigrammēšanas struktūra, kas var definēt datu uzvedību un metodes
4) klase sastāv no konstruktora/destruktora un metodēm (iekšējām funkcijām).
konstruktors - izveido ; destruktors - nojauc nost
5) kādas datu struktūras ziniet?
    -list(saraksts); a="" - tukšs saraksts
    -arry(masīvs)
    -dict(vārdnīca) ; a={} a=dict() ; tabula ar divām kolonnām, viena kolonna ir atslēga, otra ir tā vērtība
"""
class AAA:
    # jāDEFinē konstruktors
    def __init__(self):
        self.roma_sk={ 
            1:'I' ,
            4:'IV',
            5:'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }
    # definē nepieciešamās metodes
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
        return result

#piemērs
skaitlis=21
# definējam objektu
kk=AAA()
#jaunajam objektam jāizsauc klases metode
romieshu=kk.to_roman(skaitlis)

# noformēt izdruku
print(f"{skaitlis} ar romiešu cipariem ir {romieshu}.")