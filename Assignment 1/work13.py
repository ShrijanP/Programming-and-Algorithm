'''Write a Python script to concatenate following nepctionaries to create a new one.
'''

nep1={1:10, 2:20}
nep2={3:30, 4:40}
nep3={5:50,6:60}
nep4 = {}
for i in (nep1, nep2, nep3): nep4.update(i)
print(nep4)