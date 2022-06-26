#coding:utf-8
#RSA差异计算解码计算器，已知c1e1和c2e2,使用相同n加密
# Modified By MAX230 20210912


import binascii
from Crypto.Util.number import *

'''
c1 = 14086932244393217502907224674408736488830849146214227184918262698062675736724337554446711585503734671616977407523947180439538475650652413419679106435434870038055027980301567294772290568083578726775663339768961737480740922223388718943787094330870471886171540256870630059797491648906275021947443613254535459415614412289718705188895798826235866579862681303315446414825328707142227744471707921742768342732559562524019443552187374960675403256064296192626351031408014769594350992074453942709110651276633951009115468620886310509692671361261934324842739148921650085982490562922669906835464674323688759465709626540284576889210
c2 = 9788755099571270122752620318833990768386552453915390611782202313009843880011885989102462216813557305415919308702993594866012255516635580308442538867800280824955615413443022611149710694144180395588528536827198061901961298781041399064307258829088210698947995786806886824892341393690873854230422832064661235313593912677068722144241580197984421905987499008664508485233509643273752098892825326153287135195132848517181638343515469682704077797334084053581822968060796475866168907228760199308163970477417979781603099935953389513751241815586854968725454388470460653618696872424888914546835979441528674579794525553550639554293
n = 14571489544273684681632745165173941757355029852967262639728000988042839386897493030097099884895386115482493694058873038502860513888769546717076461092157274631880422404640774568976816310850151976919429837061384758878560393916832880369835035094654445542998583110983141044252629041042005200028747437532412882541760701913277010315019696176276304794162940731256361777150089869864848752521412637555443729084762017260965056626550279092491606837302796652497491465469860146607791410672793656097187677222298486237121302232907875363012059539134811841994652897489100941594071086553725267695160318463265760189436211892048571831049
e1 = 18181
e2 = 19937
'''

'''
c1 = 78552378607874335972488545767374401332953345586323262531477516680347117293352843468592985447836452620945707838830990843415342047337735534418287912723395148814463617627398248738969202758950481027762126608368555442533803610260859075919831387641824493902538796161102236794716963153162784732179636344267189394853
c2 = 98790462909782651815146615208104450165337326951856608832305081731255876886710141821823912122797166057063387122774480296375186739026132806230834774921466445172852604926204802577270611302881214045975455878277660638731607530487289267225666045742782663867519468766276566912954519691795540730313772338991769270201
n = 116547141139745534253172934123407786743246513874292261984447028928003798881819567221547298751255790928878194794155722543477883428672342894945552668904410126460402501558930911637857436926624838677630868157884406020858164140754510239986466552869866296144106255873879659676368694043769795604582888907403261286211
e1 = 1804229351
e2 = 17249876309
'''

c1 = 14086932244393217502907224674408736488830849146214227184918262698062675736724337554446711585503734671616977407523947180439538475650652413419679106435434870038055027980301567294772290568083578726775663339768961737480740922223388718943787094330870471886171540256870630059797491648906275021947443613254535459415614412289718705188895798826235866579862681303315446414825328707142227744471707921742768342732559562524019443552187374960675403256064296192626351031408014769594350992074453942709110651276633951009115468620886310509692671361261934324842739148921650085982490562922669906835464674323688759465709626540284576889210
c2 = 9788755099571270122752620318833990768386552453915390611782202313009843880011885989102462216813557305415919308702993594866012255516635580308442538867800280824955615413443022611149710694144180395588528536827198061901961298781041399064307258829088210698947995786806886824892341393690873854230422832064661235313593912677068722144241580197984421905987499008664508485233509643273752098892825326153287135195132848517181638343515469682704077797334084053581822968060796475866168907228760199308163970477417979781603099935953389513751241815586854968725454388470460653618696872424888914546835979441528674579794525553550639554293
n = 14571489544273684681632745165173941757355029852967262639728000988042839386897493030097099884895386115482493694058873038502860513888769546717076461092157274631880422404640774568976816310850151976919429837061384758878560393916832880369835035094654445542998583110983141044252629041042005200028747437532412882541760701913277010315019696176276304794162940731256361777150089869864848752521412637555443729084762017260965056626550279092491606837302796652497491465469860146607791410672793656097187677222298486237121302232907875363012059539134811841994652897489100941594071086553725267695160318463265760189436211892048571831049
e1 = 18181
e2 = 19937

def egcd(a, b):
    if a == 0:
      return (b, 0, 1)
    else:
      g, y, x = egcd(b % a, a)
      return (g, x - (b // a) * y, y)

g, r, s = egcd(e1, e2)

if r < 0:
    r = -r
    c1 = inverse(c1, n)
else:
    s = -s
    c2 = inverse(c2, n)
    
m = (pow(c1, r,  n) * pow(c2, s, n)) % n

print("DEC:")
print(m)
mi = long_to_bytes(m)
print("STRIING:",mi.decode())
message = binascii.hexlify(mi).decode()
print("HEX:",message)
