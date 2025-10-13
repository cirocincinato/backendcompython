#dada uma string s constituida apenas dos caracteres 'a' e 'b',
# retorne vardadeiro se cada 'a' aparecer antes de cada 'b' na string
#caso contrario, retorne falso.

minha_string="aaaaaaaabbbbbbbbbbbbbbb"
if 'ba' not in minha_string:
    print("ta certo")
else:
    print("errado")