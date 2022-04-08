import random

lvl =90
atk=205
pwr=110
defe=188

brn=1
typ=0.5
stb=1.5
rndm=round(random.uniform(0.85,1.0),2)
crt=1
bdg=1
wthr=1
trgt=1
mdf=brn*typ*stb*rndm*crt*bdg*wthr*trgt*1

dmg=((2*lvl)/5)+2
dmg=(dmg*pwr)*(atk/defe)
dmg=((dmg/50)+2)*mdf

print(round(dmg))
print("random number=" +str(rndm))