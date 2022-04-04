""" VERSÃO 2 - CALCULADOR DE MÉDIA COM TRÊS CHANCES
Desenvolva um algoritmo que receba 2 notas (reais) referentes a P1 e P2 
para um determinado aluno em uma disciplina. Caso a média MFP simples (entre 
P1 e P2) seja pelo menos 6.0, o aluno é APROVADO ;
Para os alunos não aprovados o sistema permite uma terceira entrada de nota
(real), a SUBSTITUTIVA. Neste caso esta nova média (MFS) é a média simples
entre a nota SUBSTITUTIVA e a maior nota entre P1 e P2 (a menor entre elas é
desconsiderada). Caso a MFS seja pelo menos 6.0 o aluno é APROVADO.
Para alunos não aprovados, o sistema' ainda permite uma quarta entrada de
nota (real), o EXAME. Neste caso a média final com exame (MFE) é a média
simples entre MFS e a nota de EXAME do aluno. Caso MFE seja pelo menos 6.0
o aluno é APROVADO; caso contrário ele é NÃO APROVADO. """

p1 = float(input("(10/0) Informe a 1º nota do aluno(P1): "))
p2 = float(input("(10/0) Informe a 2º nota do aluno(P2): "))

while p1 < 0 or p1 > 10 or p2 < 0 or p2 > 10:
    print("\nNota Ínvalida!\n")
    p1 = float(input("(10/0) Informe a 1º nota do aluno(P1) novamente: "))
    p2 = float(input("(10/0) Informe a 2º nota do aluno(P2) novamente: "))

mfp = (p1 + p2) / 2
mfs = 0

print("Nota final:", mfp)


if mfp >= 6.0:
    print("Aluno foi Aprovado!")
    print("=" * 30)
else:
    print("Aluno Reprovado!\nAluno terá que fazer a 'SUBSTITUTIVA!'")
    print("=" * 30)

    sub = float(input("(10/0) Informe a nota do aluno(P3/sub): "))

    if sub > p1:
        mfs = (sub + p2) / 2
        print("Desconsidera a nota(P1): {:.1f}!\nNova nota(P1): {}".format(p1, sub))
        print("Nota final:", mfs)
        print("=" * 30)

    elif sub > p2:
        mfs = (sub + p1) / 2
        print("Desconsidera a nota(P2): {:.1f}!\nNova nota(P2): {}".format(p2, sub))
        print("Nota final:", mfs)
        print("="*30)
    else:
        print("Aluno não atingiu a meta necessaria.\n")

    if mfs >= 6.0:
        print("Aluno foi Aprovado!")
        print("=" * 30)
    else:
        print("Aluno Reprovado!\nAluno terá que fazer o 'EXAME!'")
        print("=" * 30)

        exame = float(input("Informe a nota(P4/exame) do aluno: "))
        mfe = (mfs + exame) / 2

        print("Nota final:", mfe)

        if mfe >= 6.0:
            print("Aluno foi Aprovado!")
            print("=" * 30)
        else:
            print("Aluno Reprovado!'")
            print("=" * 30)