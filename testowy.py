zakupy={
  'piekarnia': ['chleb', 'bułki', 'pączek'],
  'warzywniak': ['marchew', 'seler', 'rukola'],
}

zakupy = {k:[x.capitalize() for x in v] for k,v in zakupy.items()}
for key, value in zakupy.items():
    print('Idę do', key.title(),'i kupuję tam', value,".")

length_piekarnia=len(zakupy['piekarnia'])
length_warzywniak=len(zakupy['warzywniak'])
length_suma=length_piekarnia+length_warzywniak
print("W sumie kupuję", length_suma,"produktów")
print("Zmiana w kodzie do commita")
