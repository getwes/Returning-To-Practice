notas = []
for x in range(3):
    codigo_aluno = input("rm:")
    nota = float(input("nota:"))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("o rm", codigo_aluno, "tirou a nota:", nota)