
articol = """România a înregistrat o creștere semnificativă a turismului intern în acest an. 
Potrivit datelor furnizate de Institutul Național de Statistică, numărul turiștilor români care au ales 
să își petreacă vacanțele în țară a crescut cu peste 15% față de anul precedent!"""


lungime = len(articol)
mijloc = lungime // 2

prima_parte = articol[:mijloc]
a_doua_parte = articol[mijloc:]


prima_parte_proc = prima_parte.upper().strip()


a_doua_parte_inversa = a_doua_parte[::-1]
a_doua_parte_fara_punct = ""
for ch in a_doua_parte_inversa:
    if ch not in ".,!?":
        a_doua_parte_fara_punct += ch


a_doua_parte_proc = a_doua_parte_fara_punct.capitalize()


rezultat = prima_parte_proc + " " + a_doua_parte_proc


print("Rezultatul final:\n")
print(rezultat)
