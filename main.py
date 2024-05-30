# A empresa do nosso melhor cliente vai nos visitar hoje
# e ele adora melancias!
import climage
import time

# HOF lambda(anônimas(parametros))

frutas = ["melancia", "banana", "maça"]

distancia_ate_feira = 4
def ir_a_feira(coisas_a_fazer):
    x = 0
    while(x < distancia_ate_feira):
        time.sleep(1)
        print(f'Percorrendo Km {x}')
        x += 1

    for algo_a_fazer in coisas_a_fazer:
        print(algo_a_fazer())


def verificar_se_tem(fruta):
    return "Sim temos" if fruta in frutas else "Não temos"

def check_preco():
    return "Custa R$ 10,00 cada"

def check_promocao():
    return "20% desconto para 5 unidades"

def mostrar_melancia_para_chefia():
    return climage.convert('melancia.png')

if __name__ == "__main__":
    acoes = [lambda: verificar_se_tem("melancia"), check_preco, check_promocao, mostrar_melancia_para_chefia]
    ir_a_feira(acoes)



    