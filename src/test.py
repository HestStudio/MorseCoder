from morsecoder import Morsecoder

morse1 = Morsecoder(text='Hello World', sep='/')
print(f'The text of morse1: {morse1.text}')
for i in morse1.morse_en():
    print(i, end='')
print()

Morsecoder.modify('×', '.----...-.')

morse2 = Morsecoder(text='.----...-.', sep=' ')
print(f'The text of morse2: {morse2.text}')
for i in morse2.morse_de():
    print(i, end='')
print()
