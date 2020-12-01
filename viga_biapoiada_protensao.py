#Calculo da protensao para vigas biapoiadas
#Novembro de 2020

import math #biblioteca para operações matemáticas

class color: #classe com efeitos visuais para o output
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#00 - Título

print (color.BOLD + color.YELLOW + "\nCÁLCULO DA PROTENSÃO PARA VIGAS BIAPOIADAS\n" + color.END)
print ("Insira os dados solicitados abaixo, seguindo exatamente a formatação solicitada. Não utilize vírgulas ou acentos. \n")

#01 - Quantidade de vigas

qtde_vigas = float (input ("Quantidade de vigas no vão (limite de 10 vigas): \n"))

#02 - Dados de entrada executados uma única vez

nivel_protensao = (input ("Nível de protensão (1/2/3): \n"))
if nivel_protensao != '2':
    print ("Atualmente somente a opção '2' está habilitada\n")
area_secao = float (input ("Área da seção (A) [m²]: \n"))
momento_inercia = float (input ("Momento de inércia (I) [m⁴]: \n"))
cg_y = float (input ("Coordenada y do centro de gravidade (CG) [m]: \n"))
altura_secao = float (input ("Altura total da seção (h) [m]: \n"))
comprimento_total = float (input ("Comprimento total (C) [m]: \n"))
peso_proprio_material = float (input ("Peso próprio do material (PP) [kN/m³]: \n"))
fck_concreto = float (input ("Fck do concreto [MPa]: \n"))
fcj = float (input ("Fcj [Mpa]: \n"))
perdas_diferidas = float (input ("Perdas diferidas [%]: \n"))
perdas_imediatas = float (input ("Perdas imediatas [%]: \n"))
aco = (input ("Tipo de aço ('CP190RB' ou 'outro'): \n"))
tipo_secao = (input ("Tipo de seção ('R' para retangular, 'I' para T invertido ou 'T'): \n"))

#06 - Valores atribuídos conforme escolha do usuário:

if aco == 'CP190RB':
    fptk= float (1900)
    fpyk= float (1710)
else:
    fptk = float(input("Fptk do aço [MPa]: \n"))
    fpyk = float(input("Fpyk do aço [MPa]: \n"))

if tipo_secao == 'R':
    alfa= float(1.5)
elif tipo_secao == 'I':
    alfa= float(1.3)
elif tipo_secao == 'T':
    alfa= float(1.2)
else:
    print ("Seção incorreta\n")

# 03 - Dados de entrada variáveis conforme o número de vigas:

qtde_calculos = math.ceil(qtde_vigas / 2) #arredonda para cima
print (color.BOLD + color.BLUE+ "\nQuantidade de cálculos iterativos: {} \n".format(qtde_calculos))
if qtde_calculos > 5:
    print ("O limite previsto são 05 cálculos iterativos.\n")
if qtde_calculos < 1:
    print ("O mínimo previsto é 01 cálculo iterativo.\n")

# Viga 01
if qtde_calculos >= 1:
    print (color.BOLD + color.YELLOW + "\nVIGA 1\n" + color.END)
    momento_quase_permanente_viga1 = float (input ("Momento para situação quase permanente [kN.m]: \n"))
    momento_situacao_frequente_viga1 = float (input ("Momento para situação frequente [kN.m]: \n"))
    area_secao_aba_colaborante_viga1 = float (input ("Área da Seção com aba colaborante (Ac) [m²]: \n"))
    momento_inercia_aba_colaborante_viga1 = float (input ("Momento de Inércia com aba colaborante (Ic) [m4]: \n"))
    coordenada_y_cg_aba_colaborante_viga1 = float (input ("Coordenada y do centro de gravidade com aba colaborante (CGc) [m]: \n"))
    altura_total_secao_aba_colaborante_viga1 = float (input ("Altura total da seção com aba colaborante (hc) [m]: \n"))

# Viga 02
if qtde_calculos >= 2:
    print (color.BOLD + color.YELLOW + "\nVIGA 2\n" + color.END)
    momento_quase_permanente_viga2 = float (input ("Momento para situação quase permanente [kN.m]: \n"))
    momento_situacao_frequente_viga2 = float (input ("Momento para situação frequente [kN.m]: \n"))
    area_secao_aba_colaborante_viga2 = float (input ("Área da Seção com aba colaborante (Ac) [m²]: \n"))
    momento_inercia_aba_colaborante_viga2 = float (input ("Momento de Inércia com aba colaborante (Ic) [m4]: \n"))
    coordenada_y_cg_aba_colaborante_viga2 = float (input ("Coordenada y do centro de gravidade com aba colaborante (CGc) [m]: \n"))
    altura_total_secao_aba_colaborante_viga2 = float (input ("Altura total da seção com aba colaborante (hc) [m]: \n"))

# Viga 03
if qtde_calculos >= 3:
    print (color.BOLD + color.YELLOW + "\nVIGA 3\n" + color.END)
    momento_quase_permanente_viga3 = float (input ("Momento para situação quase permanente [kN.m]: \n"))
    momento_situacao_frequente_viga3 = float (input ("Momento para situação frequente [kN.m]: \n"))
    area_secao_aba_colaborante_viga3 = float (input ("Área da Seção com aba colaborante (Ac) [m²]: \n"))
    momento_inercia_aba_colaborante_viga3 = float (input ("Momento de Inércia com aba colaborante (Ic) [m4]: \n"))
    coordenada_y_cg_aba_colaborante_viga3 = float (input ("Coordenada y do centro de gravidade com aba colaborante (CGc) [m]: \n"))
    altura_total_secao_aba_colaborante_viga3 = float (input ("Altura total da seção com aba colaborante (hc) [m]: \n"))

# Viga 04
if qtde_calculos >= 4:
    print (color.BOLD + color.YELLOW + "\nVIGA 4\n" + color.END)
    momento_quase_permanente_viga4 = float (input ("Momento para situação quase permanente [kN.m]: \n"))
    momento_situacao_frequente_viga4 = float (input ("Momento para situação frequente [kN.m]: \n"))
    area_secao_aba_colaborante_viga4 = float (input ("Área da Seção com aba colaborante (Ac) [m²]: \n"))
    momento_inercia_aba_colaborante_viga4 = float (input ("Momento de Inércia com aba colaborante (Ic) [m4]: \n"))
    coordenada_y_cg_aba_colaborante_viga4 = float (input ("Coordenada y do centro de gravidade com aba colaborante (CGc) [m]: \n"))
    altura_total_secao_aba_colaborante_viga4 = float (input ("Altura total da seção com aba colaborante (hc) [m]: \n"))

# Viga 05
if qtde_calculos == 5:
    print (color.BOLD + color.YELLOW + "\nVIGA 5\n" + color.END)
    momento_quase_permanente_viga5 = float (input ("Momento para situação quase permanente [kN.m]: \n"))
    momento_situacao_frequente_viga5 = float (input ("Momento para situação frequente [kN.m]: \n"))
    area_secao_aba_colaborante_viga5 = float (input ("Área da Seção com aba colaborante (Ac) [m²]: \n"))
    momento_inercia_aba_colaborante_viga5 = float (input ("Momento de Inércia com aba colaborante (Ic) [m4]: \n"))
    coordenada_y_cg_aba_colaborante_viga5 = float (input ("Coordenada y do centro de gravidade com aba colaborante (CGc) [m]: \n"))
    altura_total_secao_aba_colaborante_viga5 = float (input ("Altura total da seção com aba colaborante (hc) [m]: \n"))

#04 - Cálculos iniciais executados uma única vez

y_inf= round (cg_y, 4)
y_sup= round ((cg_y - altura_secao), 4)
w_inf= round ((momento_inercia / y_inf), 4)
w_sup= round ((momento_inercia / y_sup), 4)
ep= round ((y_inf - 0.10), 4)
print (color.BOLD + color.YELLOW + "\nResultados:\n" + color.END)
print ("Coordenada y inferior: {} [m] \n".format(y_inf))
print ("Coordenada y superior: {} [m] \n".format(y_sup))
print ("Módulo de resistência w inferior: {} [m] \n".format(w_inf))
print ("Módulo de resistência w superior: {} [m] \n".format(w_sup))
print ("Excentricidade da forma de protensão (ep): {} [m] \n".format(ep))

#05 - Cálculos iniciais variáveis conforme o número de vigas

# Viga 01
if qtde_calculos >= 1:
    print (color.BOLD + color.YELLOW + "\nVIGA 1\n" + color.END)
    y_inf_viga1 = round (coordenada_y_cg_aba_colaborante_viga1, 4)
    y_sup_viga1 = round ((coordenada_y_cg_aba_colaborante_viga1 - altura_total_secao_aba_colaborante_viga1), 4)
    w_inf_viga1 = round ((momento_inercia_aba_colaborante_viga1 / y_inf_viga1), 4)
    w_sup_viga1 = round ((momento_inercia_aba_colaborante_viga1 / y_sup_viga1), 4)
    ep_viga1 = round ((y_inf_viga1 - 0.10), 4)
    print ("Coordenada y inferior colaborante: {} [m] \n".format(y_inf_viga1))
    print ("Coordenada y superior colaborante: {} [m] \n".format(y_sup_viga1))
    print ("Módulo de resistência w inferior colaborante: {} [m] \n".format(w_inf_viga1))
    print ("Módulo de resistência w superior colaborante: {} [m] \n".format(w_sup_viga1))
    print ("Excentricidade da forma de protensão colaborante (ep): {} [m] \n".format(ep_viga1))

# Viga 02
if qtde_calculos >= 2:
    print (color.BOLD + color.YELLOW + "\nVIGA 2\n" + color.END)
    y_inf_viga2 = round (coordenada_y_cg_aba_colaborante_viga2, 4)
    y_sup_viga2 = round ((coordenada_y_cg_aba_colaborante_viga2 - altura_total_secao_aba_colaborante_viga2), 4)
    w_inf_viga2 = round ((momento_inercia_aba_colaborante_viga2 / y_inf_viga2), 4)
    w_sup_viga2 = round ((momento_inercia_aba_colaborante_viga2 / y_sup_viga2), 4)
    ep_viga2 = round ((y_inf_viga2 - 0.10), 4)
    print ("Coordenada y inferior colaborante: {} [m] \n".format(y_inf_viga2))
    print ("Coordenada y superior colaborante: {} [m] \n".format(y_sup_viga2))
    print ("Módulo de resistência w inferior colaborante: {} [m] \n".format(w_inf_viga2))
    print ("Módulo de resistência w superior colaborante: {} [m] \n".format(w_sup_viga2))
    print ("Excentricidade da forma de protensão colaborante (ep): {} [m] \n".format(ep_viga2))

# Viga 03
if qtde_calculos >= 3:
    print (color.BOLD + color.YELLOW + "\nVIGA 3\n" + color.END)
    y_inf_viga3 = round (coordenada_y_cg_aba_colaborante_viga3, 4)
    y_sup_viga3 = round ((coordenada_y_cg_aba_colaborante_viga3 - altura_total_secao_aba_colaborante_viga3), 4)
    w_inf_viga3 = round ((momento_inercia_aba_colaborante_viga3 / y_inf_viga3), 4)
    w_sup_viga3 = round ((momento_inercia_aba_colaborante_viga3 / y_sup_viga3), 4)
    ep_viga3 = round ((y_inf_viga3 - 0.10), 4)
    print ("Coordenada y inferior colaborante: {} [m] \n".format(y_inf_viga3))
    print ("Coordenada y superior colaborante: {} [m] \n".format(y_sup_viga3))
    print ("Módulo de resistência w inferior colaborante: {} [m] \n".format(w_inf_viga3))
    print ("Módulo de resistência w superior colaborante: {} [m] \n".format(w_sup_viga3))
    print ("Excentricidade da forma de protensão colaborante (ep): {} [m] \n".format(ep_viga3))

# Viga 04
if qtde_calculos >= 4:
    print (color.BOLD + color.YELLOW + "\nVIGA 4\n" + color.END)
    y_inf_viga4 = round (coordenada_y_cg_aba_colaborante_viga4, 4)
    y_sup_viga4 = round ((coordenada_y_cg_aba_colaborante_viga4 - altura_total_secao_aba_colaborante_viga4), 4)
    w_inf_viga4 = round ((momento_inercia_aba_colaborante_viga4 / y_inf_viga4), 4)
    w_sup_viga4 = round ((momento_inercia_aba_colaborante_viga4 / y_sup_viga4), 4)
    ep_viga4 = round ((y_inf_viga4 - 0.10), 4)
    print ("Coordenada y inferior colaborante: {} [m] \n".format(y_inf_viga4))
    print ("Coordenada y superior colaborante: {} [m] \n".format(y_sup_viga4))
    print ("Módulo de resistência w inferior colaborante: {} [m] \n".format(w_inf_viga4))
    print ("Módulo de resistência w superior colaborante: {} [m] \n".format(w_sup_viga4))
    print ("Excentricidade da forma de protensão colaborante (ep): {} [m] \n".format(ep_viga4))

# Viga 05
if qtde_calculos == 5:
    print (color.BOLD + color.YELLOW + "\nVIGA 5\n" + color.END)
    y_inf_viga5 = round (coordenada_y_cg_aba_colaborante_viga5, 4)
    y_sup_viga5 = round ((coordenada_y_cg_aba_colaborante_viga5 - altura_total_secao_aba_colaborante_viga5), 4)
    w_inf_viga5 = round ((momento_inercia_aba_colaborante_viga5 / y_inf_viga5), 4)
    w_sup_viga5 = round ((momento_inercia_aba_colaborante_viga5 / y_sup_viga5), 4)
    ep_viga5 = round ((y_inf_viga5 - 0.10), 4)
    print ("Coordenada y inferior colaborante: {} [m] \n".format(y_inf_viga5))
    print ("Coordenada y superior colaborante: {} [m] \n".format(y_sup_viga5))
    print ("Módulo de resistência w inferior colaborante: {} [m] \n".format(w_inf_viga5))
    print ("Módulo de resistência w superior colaborante: {} [m] \n".format(w_sup_viga5))
    print ("Excentricidade da forma de protensão colaborante (ep): {} [m] \n".format(ep_viga5))

#07 - Cálculos secundários

print (color.BOLD + color.YELLOW + "\nCálculos Secundários\n" + color.END)
fctk_inf= round ((0.21 * (math.pow(fck_concreto, (2/3)))), 4)
v1= round ((alfa * fctk_inf * 1000), 4)
v2= round ((0.74 * fptk / 10), 4)
v3= round ((0.82 * fpyk / 10), 4)
fctm= round ((0.3 * (math.pow(fcj, (2/3)))), 4)
v4= round ((1.2 * fctm * 1000), 4)
v5= round ((-1 * 0.7 * fcj * 1000), 4)
print ("Fctk inferior: {} [MPa] \n".format(fctk_inf))
print ("V1 (α x fctk,inf): {} [kN/m²] \n".format(v1))
print ("V2 (0.74 x fptk): {} [kN/cm²] \n".format(v2))
print ("V3 (0.84 x fpyk): {} [kN/cm²] \n".format(v3))
print ("Fctm: {} [MPa] \n".format(fctm))
print ("V4 (1.2 x fctm): {} [kN/m²] \n".format(v4))
print ("V5 (-0.7 x fcj): {} [kN/m²] \n".format(v5))

#08 - Cálculo da Protensão variáveis conforme o número de vigas

print (color.BOLD + color.YELLOW + "\nProtensão:\n" + color.END)

# Viga 01
if qtde_calculos >= 1:
    print (color.BOLD + color.YELLOW + "\nVIGA 1\n" + color.END)
    p_permanente_viga1 = round ((( 0 - (momento_quase_permanente_viga1 / w_inf_viga1)) / ((1 / area_secao_aba_colaborante_viga1) + (ep_viga1 / w_inf_viga1))), 4)
    p_frequente_viga1 = round ((( (v1) - (momento_situacao_frequente_viga1 / w_inf_viga1)) / ((1 / area_secao_aba_colaborante_viga1) + (ep_viga1 / w_inf_viga1))), 4)
    if p_permanente_viga1 <= p_frequente_viga1:
        p_viga1= p_permanente_viga1
    else:
        p_viga1= p_frequente_viga1

    p0_viga1= round (( p_viga1 / ((100 - perdas_imediatas - perdas_diferidas) / 100)), 4)
    p1_viga1= round ((p0_viga1 * ((100 - perdas_imediatas) / 100)), 4)

    print ("\tP (mínimo): {} [kN] \n".format(p_viga1))
    print ("\tP0: {} [kN] \n".format(p0_viga1))
    print ("\tP1: {} [kN] \n".format(p1_viga1))

# Viga 02
if qtde_calculos >= 2:
    print (color.BOLD + color.YELLOW + "\nVIGA 2\n" + color.END)
    p_permanente_viga2 = round ((( 0 - (momento_quase_permanente_viga2 / w_inf_viga2)) / ((1 / area_secao_aba_colaborante_viga2) + (ep_viga2 / w_inf_viga2))), 4)
    p_frequente_viga2 = round ((( (v1) - (momento_situacao_frequente_viga2 / w_inf_viga2)) / ((1 / area_secao_aba_colaborante_viga2) + (ep_viga2 / w_inf_viga2))), 4)
    if p_permanente_viga2 <= p_frequente_viga2:
        p_viga2= p_permanente_viga2
    else:
        p_viga2= p_frequente_viga2

    p0_viga2= round (( p_viga2 / ((100 - perdas_imediatas - perdas_diferidas) / 100)), 4)
    p1_viga2= round ((p0_viga2 * ((100 - perdas_imediatas) / 100)), 4)

    print ("\tP: {} [kN] \n".format(p_viga2))
    print ("\tP0: {} [kN] \n".format(p0_viga2))
    print ("\tP1: {} [kN] \n".format(p1_viga2))

# Viga 03
if qtde_calculos >= 3:
    print (color.BOLD + color.YELLOW + "\nVIGA 3\n" + color.END)
    p_permanente_viga3 = round ((( 0 - (momento_quase_permanente_viga3 / w_inf_viga3)) / ((1 / area_secao_aba_colaborante_viga3) + (ep_viga3 / w_inf_viga3))), 4)
    p_frequente_viga3 = round ((( (v1) - (momento_situacao_frequente_viga3 / w_inf_viga3)) / ((1 / area_secao_aba_colaborante_viga3) + (ep_viga3 / w_inf_viga3))), 4)
    if p_permanente_viga3 <= p_frequente_viga3:
        p_viga3= p_permanente_viga3
    else:
        p_viga3= p_frequente_viga3

    p0_viga3= round (( p_viga3 / ((100 - perdas_imediatas - perdas_diferidas) / 100)), 4)
    p1_viga3= round ((p0_viga3 * ((100 - perdas_imediatas) / 100)), 4)

    print ("\tP: {} [kN] \n".format(p_viga3))
    print ("\tP0: {} [kN] \n".format(p0_viga3))
    print ("\tP1: {} [kN] \n".format(p1_viga3))

# Viga 04
if qtde_calculos >= 4:
    print (color.BOLD + color.YELLOW + "\nVIGA 4\n" + color.END)
    p_permanente_viga4 = round ((( 0 - (momento_quase_permanente_viga4 / w_inf_viga4)) / ((1 / area_secao_aba_colaborante_viga4) + (ep_viga4 / w_inf_viga4))), 4)
    p_frequente_viga4 = round ((( (v1) - (momento_situacao_frequente_viga4 / w_inf_viga4)) / ((1 / area_secao_aba_colaborante_viga4) + (ep_viga4 / w_inf_viga4))), 4)
    if p_permanente_viga4 <= p_frequente_viga4:
        p_viga4= p_permanente_viga4
    else:
        p_viga4= p_frequente_viga4

    p0_viga4= round (( p_viga4 / ((100 - perdas_imediatas - perdas_diferidas) / 100)), 4)
    p1_viga4= round ((p0_viga4 * ((100 - perdas_imediatas) / 100)), 4)

    print ("\tP: {} [kN] \n".format(p_viga4))
    print ("\tP0: {} [kN] \n".format(p0_viga4))
    print ("\tP1: {} [kN] \n".format(p1_viga4))

# Viga 05
if qtde_calculos == 5:
    print (color.BOLD + color.YELLOW + "\nVIGA 5\n" + color.END)
    p_permanente_viga5 = round ((( 0 - (momento_quase_permanente_viga5 / w_inf_viga5)) / ((1 / area_secao_aba_colaborante_viga5) + (ep_viga5 / w_inf_viga5))), 4)
    p_frequente_viga5 = round ((( (v1) - (momento_situacao_frequente_viga5 / w_inf_viga5)) / ((1 / area_secao_aba_colaborante_viga5) + (ep_viga5 / w_inf_viga5))), 4)
    if p_permanente_viga5 <= p_frequente_viga5:
        p_viga5= p_permanente_viga5
    else:
        p_viga5= p_frequente_viga5

    p0_viga5= round (( p_viga5 / ((100 - perdas_imediatas - perdas_diferidas) / 100)), 4)
    p1_viga5= round ((p0_viga5 * ((100 - perdas_imediatas) / 100)), 4)

    print ("\tP: {} [kN] \n".format(p_viga5))
    print ("\tP0: {} [kN] \n".format(p0_viga5))
    print ("\tP1: {} [kN] \n".format(p1_viga5))

#09A - Cálculo da quantidade de aço variável segundo o número de vigas

if v2 <= v3:
    v_menor = v2
else:
    v_menor = v3

print (color.BOLD + color.YELLOW + "Cálculo da quantidade de aço:\n" + color.END)
diametro_aco = float (input ("Insira o diâmetro do aço (12.7 ou 15.2) [cm²]: \n"))
if diametro_aco == 12.7:
    area_cordoalha= 0.99
elif diametro_aco == 15.2:
    area_cordoalha= 1.40
else:
    print ("Diâmetro do aço incorreto\n")

# Viga 01
if qtde_calculos >= 1:
    print (color.BOLD + color.YELLOW + "\nVIGA 1\n" + color.END)
    area_aco_viga1= round ((-p0_viga1 / v_menor), 4)
    qtde_cordoalhas_viga1= math.ceil(area_aco_viga1 / area_cordoalha)
    print ("Serao necessarias {} cordoalhas, com diametro de {} e 07 fios\n".format(qtde_cordoalhas_viga1, diametro_aco))

# Viga 02
if qtde_calculos >= 2:
    print (color.BOLD + color.YELLOW + "\nVIGA 2\n" + color.END)
    area_aco_viga2= round ((-p0_viga2 / v_menor), 4)
    qtde_cordoalhas_viga2= math.ceil(area_aco_viga2 / area_cordoalha)
    print ("Serao necessarias {} cordoalhas, com diametro de {} e 07 fios\n".format(qtde_cordoalhas_viga2, diametro_aco))

# Viga 03
if qtde_calculos >= 3:
    print (color.BOLD + color.YELLOW + "\nVIGA 3\n" + color.END)
    area_aco_viga3= round ((-p0_viga3 / v_menor), 4)
    qtde_cordoalhas_viga3= math.ceil(area_aco_viga3 / area_cordoalha)
    print ("Serao necessarias {} cordoalhas, com diametro de {} e 07 fios\n".format(qtde_cordoalhas_viga3, diametro_aco))

# Viga 04
if qtde_calculos >= 4:
    print (color.BOLD + color.YELLOW + "\nVIGA 4\n" + color.END)
    area_aco_viga4= round ((-p0_viga4 / v_menor), 4)
    qtde_cordoalhas_viga4= math.ceil(area_aco_viga4 / area_cordoalha)
    print ("Serao necessarias {} cordoalhas, com diametro de {} e 07 fios\n".format(qtde_cordoalhas_viga4, diametro_aco))

# Viga 05
if qtde_calculos == 5:
    print (color.BOLD + color.YELLOW + "\nVIGA 5\n" + color.END)
    area_aco_viga5= round ((-p0_viga5 / v_menor), 4)
    qtde_cordoalhas_viga5= math.ceil(area_aco_viga5 / area_cordoalha)
    print ("Serao necessarias {} cordoalhas, com diametro de {} e 07 fios\n".format(qtde_cordoalhas_viga5, diametro_aco))

# 09B - Cálculo da nova área de aço independente do número de vigas

print (color.BOLD + color.YELLOW + "\nCálculo da nova área de aço:\n" + color.END)
nova_qtde_cabos = float (input ("Insira a quantidade de cabos:\n"))
nova_qtde_cordoalhas = float (input ("Insira a quantidade de cordoalhas:\n"))
print ("\nCálculos considerando {} cabos de {} cordoalhas.\n".format(nova_qtde_cabos, nova_qtde_cordoalhas))
nova_area_aco= round ((nova_qtde_cabos * nova_qtde_cordoalhas * area_cordoalha), 4)
print ("Nova área do aço: {} [cm²]\n".format(nova_area_aco))

#10 - Cálculo da nova força de protensão independente do número de vigas

novo_p0= round ((v_menor * nova_area_aco), 4)
novo_p1 = round (( novo_p0 * ((100 - perdas_imediatas) /100 )), 4)
novo_p = round (( novo_p0 * ((100 - perdas_imediatas - perdas_diferidas) /100 )), 4)
print (color.BOLD + color.YELLOW + "Resultados das novas forças de protensão:\n" + color.END)
print ("Novo P: {} [kN] \n".format(novo_p))
print ("Novo P0: {} [kN] \n".format(novo_p0))
print ("Novo P1: {} [kN] \n".format(novo_p1))

#11 - Momentos variando conforme número de vigas

print (color.BOLD + color.YELLOW + "\nResultados dos Momentos: \n" + color.END)

# Viga 01
if qtde_calculos >= 1:
    print (color.BOLD + color.YELLOW + "\nVIGA 1\n" + color.END)
    print ("Momento ½ do vão quase permanente: {} [kN/m] \n".format(momento_quase_permanente_viga1))
    print ("Momento ½  do vão frequente: {} [kN/m] \n".format(momento_situacao_frequente_viga1))
    mqp_viga1= round ((0.75 * momento_quase_permanente_viga1), 4)
    print ("Momento ¼ do vão quase permanente: {} [kN/m] \n".format(mqp_viga1))
    mf_viga1= round ((0.75 * momento_situacao_frequente_viga1), 4)
    print ("Momento ¼ do vão frequente: {} [kN/m] \n".format(mf_viga1))

# Viga 02
if qtde_calculos >= 2:
    print (color.BOLD + color.YELLOW + "\nVIGA 2\n" + color.END)
    print ("Momento ½ do vão quase permanente: {} [kN/m] \n".format(momento_quase_permanente_viga2))
    print ("Momento ½ do vão frequente: {} [kN/m] \n".format(momento_situacao_frequente_viga2))
    mqp_viga2= round ((0.75 * momento_quase_permanente_viga2), 4)
    print ("Momento ¼ do vão quase permanente: {} [kN/m] \n".format(mqp_viga2))
    mf_viga2= round ((0.75 * momento_situacao_frequente_viga2), 4)
    print ("Momento ¼ do vão frequente: {} [kN/m] \n".format(mf_viga2))

# Viga 03
if qtde_calculos >= 3:
    print (color.BOLD + color.YELLOW + "\nVIGA 3\n" + color.END)
    print ("Momento ½ do vão quase permanente: {} [kN/m] \n".format(momento_quase_permanente_viga3))
    print ("Momento ½ do vão frequente: {} [kN/m] \n".format(momento_situacao_frequente_viga3))
    mqp_viga3= round ((0.75 * momento_quase_permanente_viga3), 4)
    print ("Momento ¼ do vão quase permanente: {} [kN/m] \n".format(mqp_viga3))
    mf_viga3= round ((0.75 * momento_situacao_frequente_viga3), 4)
    print ("Momento ¼ do vão frequente: {} [kN/m] \n".format(mf_viga3))

# Viga 04
if qtde_calculos >= 4:
    print (color.BOLD + color.YELLOW + "\nVIGA 4\n" + color.END)
    print ("Momento ½ do vão quase permanente: {} [kN/m] \n".format(momento_quase_permanente_viga4))
    print ("Momento ½ do vão frequente: {} [kN/m] \n".format(momento_situacao_frequente_viga4))
    mqp_viga4= round ((0.75 * momento_quase_permanente_viga4), 4)
    print ("Momento ¼ do vão quase permanente: {} [kN/m] \n".format(mqp_viga4))
    mf_viga4= round ((0.75 * momento_situacao_frequente_viga4), 4)
    print ("Momento ¼ do vão frequente: {} [kN/m] \n".format(mf_viga4))

# Viga 05
if qtde_calculos == 5:
    print (color.BOLD + color.YELLOW + "\nVIGA 5\n" + color.END)
    print ("Momento ½ do vão quase permanente: {} [kN/m] \n".format(momento_quase_permanente_viga5))
    print ("Momento ½ do vão frequente: {} [kN/m] \n".format(momento_situacao_frequente_viga5))
    mqp_viga5= round ((0.75 * momento_quase_permanente_viga5), 4)
    print ("Momento ¼ do vão quase permanente: {} [kN/m] \n".format(mqp_viga5))
    mf_viga5= round ((0.75 * momento_situacao_frequente_viga5), 4)
    print ("Momento ¼ do vão frequente: {} [kN/m] \n".format(mf_viga5))

#Não varia conforme número de vigas
print (color.BOLD + color.YELLOW + "\nVALORES INDEPENDENTES DA QUANTIDADE DE VIGAS:\n" + color.END)
mg_meio= round ((((area_secao * peso_proprio_material) * (math.pow(comprimento_total , 2))) / 8 ), 4)
print ("Momento ½ do vão - peso próprio: {} [kN/m] \n".format(mg_meio))
mg_um_quarto= round ((0.75 * mg_meio), 4)
print ("Momento ¼ do vão - peso próprio: {} [kN/m] \n".format(mg_um_quarto))

#Não varia conforme número de vigas
apoio_permanente= float(0)
apoio_frequente= float(0)
mg_apoio= float(0)
print ("Momento no apoio quase permanente: {} [kN/m] \n".format(apoio_permanente))
print ("Momento no apoio frequente: {} [kN/m] \n".format(apoio_frequente))
print ("Momento no apoio peso próprio: {} [kN/m] \n".format(mg_apoio))

#Tabela de momentos variável conforme quantidade de vigas

def tabela_momentos_viga1():
    print ("\n----------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "Viga 1" + color.END)
    if (qtde_calculos == 1) or (qtde_calculos == 2) or (qtde_calculos == 3):
        print(color.BOLD + color.YELLOW + "(Válido também para a Viga 5)\n" + color.END)
    print ("Tipo\t\t\t\tQuase Permanente\tFrequente\t\tPeso Próprio")
    print ("----------------------------------------------------------------------------")
    print ("%s:\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f" % ('1/2 vão', momento_quase_permanente_viga1, momento_situacao_frequente_viga1, mg_meio))
    print ("%s:\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f" % ('1/4 vão', mqp_viga1, mf_viga1, mg_um_quarto))
    print ("%s:\t\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f\n" % ('Apoio', apoio_permanente, apoio_frequente, mg_apoio))
    print ("[Todos os resultados em kN/m]")
    print ("----------------------------------------------------------------------------")

def tabela_momentos_viga2():
    print ("\n----------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "Viga 2" + color.END)
    if (qtde_calculos == 1) or (qtde_calculos == 2) or (qtde_calculos == 3):
        print(color.BOLD + color.YELLOW + "(Válido também para a Viga 4)\n" + color.END)
    print ("Tipo\t\t\t\tQuase Permanente\tFrequente\t\tPeso Próprio")
    print ("----------------------------------------------------------------------------")
    print ("%s:\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f" % ('1/2 vão', momento_quase_permanente_viga2, momento_situacao_frequente_viga2, mg_meio))
    print ("%s:\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f" % ('1/4 vão', mqp_viga2, mf_viga2, mg_um_quarto))
    print ("%s:\t\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f\n" % ('Apoio', apoio_permanente, apoio_frequente, mg_apoio))
    print ("[Todos os resultados em kN/m]")
    print ("----------------------------------------------------------------------------")

def tabela_momentos_viga3():
    print ("\n----------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "Viga 3" + color.END)
    print ("Tipo\t\t\t\tQuase Permanente\tFrequente\t\tPeso Próprio")
    print ("----------------------------------------------------------------------------")
    print ("%s:\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f" % ('1/2 vão', momento_quase_permanente_viga3, momento_situacao_frequente_viga3, mg_meio))
    print ("%s:\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f" % ('1/4 vão', mqp_viga3, mf_viga3, mg_um_quarto))
    print ("%s:\t\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f\n" % ('Apoio', apoio_permanente, apoio_frequente, mg_apoio))
    print ("[Todos os resultados em kN/m]")
    print ("----------------------------------------------------------------------------")

def tabela_momentos_viga4():
    print ("\n----------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "Viga 4" + color.END)
    print ("Tipo\t\t\t\tQuase Permanente\t\tFrequente\t\t\tPeso Próprio")
    print ("----------------------------------------------------------------------------")
    print ("%s:\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f" % ('1/2 vão', momento_quase_permanente_viga4, momento_situacao_frequente_viga4, mg_meio))
    print ("%s:\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f" % ('1/4 vão', mqp_viga4, mf_viga4, mg_um_quarto))
    print ("%s:\t\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f\n" % ('Apoio', apoio_permanente, apoio_frequente, mg_apoio))
    print ("[Todos os resultados em kN/m]")
    print ("----------------------------------------------------------------------------")

def tabela_momentos_viga5():
    print ("\n----------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "Viga 5" + color.END)
    print ("Tipo\t\t\t\tQuase Permanente\tFrequente\t\tPeso Próprio")
    print ("----------------------------------------------------------------------------")
    print ("%s:\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f" % ('1/2 vão', momento_quase_permanente_viga5, momento_situacao_frequente_viga5, mg_meio))
    print ("%s:\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f" % ('1/4 vão', mqp_viga5, mf_viga5, mg_um_quarto))
    print ("%s:\t\t\t\t%.2f\t\t\t\t%.2f\t\t\t%.2f\n" % ('Apoio', apoio_permanente, apoio_frequente, mg_apoio))
    print ("[Todos os resultados em kN/m]")
    print ("----------------------------------------------------------------------------")

print (color.BOLD + color.YELLOW + "\nTabela de Momentos" + color.END)

#Viga 1
if qtde_calculos >= 1:
    tabela_momentos_viga1()

#Viga 2
if qtde_calculos >= 2:
    tabela_momentos_viga2()

#Viga 3
if qtde_calculos >= 3:
    tabela_momentos_viga3()

#Viga 4
if qtde_calculos >= 4:
    tabela_momentos_viga4()

#Viga 5
if qtde_calculos == 5:
    tabela_momentos_viga5()

#12 - Verificações

#Para 1/2 do vão

#EP1 Variável conforme quantidade de vigas - ELS-F

#Viga 01
if qtde_calculos >= 1:
    ep1_viga1=  round (((((v1 - (momento_situacao_frequente_viga1 / w_inf_viga1)) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga1)) * w_inf_viga1), 2)
else:
    ep1_viga1= 0

#Viga 02
if qtde_calculos >= 2:
    ep1_viga2=  round (((((v1 - (momento_situacao_frequente_viga2 / w_inf_viga2)) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga2)) * w_inf_viga2), 2)
else:
    ep1_viga2= 0

#Viga 03
if qtde_calculos >= 3:
    ep1_viga3=  round (((((v1 - (momento_situacao_frequente_viga3 / w_inf_viga3)) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga3)) * w_inf_viga3), 2)
else:
    ep1_viga3= 0

#Viga 04
if qtde_calculos >= 4:
    ep1_viga4=  round (((((v1 - (momento_situacao_frequente_viga4 / w_inf_viga4)) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga4)) * w_inf_viga4), 2)
else:
    ep1_viga4= ep1_viga2

#Viga 05
if qtde_calculos == 5:
    ep1_viga5=  round (((((v1 - (momento_situacao_frequente_viga5 / w_inf_viga5)) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga5)) * w_inf_viga5), 2)
else:
    ep1_viga5= ep1_viga1

#EP2 Variável conforme quantidade de vigas - ELS-D

#Viga 01
if qtde_calculos >= 1:
    ep2_viga1= round (((((-momento_quase_permanente_viga1 / w_inf_viga1) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga1)) * w_inf_viga1), 2)
else:
    ep2_viga1= 0

#Viga 02
if qtde_calculos >= 2:
    ep2_viga2= round (((((-momento_quase_permanente_viga2 / w_inf_viga2) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga2)) * w_inf_viga2), 2)
else:
    ep2_viga2= 0

#Viga 03
if qtde_calculos >= 3:
    ep2_viga3= round (((((-momento_quase_permanente_viga3 / w_inf_viga3) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga3)) * w_inf_viga3), 2)
else:
    ep2_viga3= 0

#Viga 04
if qtde_calculos >= 4:
    ep2_viga4= round (((((-momento_quase_permanente_viga4 / w_inf_viga4) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga4)) * w_inf_viga4), 2)
else:
    ep2_viga4= ep2_viga2

#Viga 05
if qtde_calculos == 5:
    ep2_viga5= round (((((-momento_quase_permanente_viga5 / w_inf_viga5) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga5)) * w_inf_viga5), 2)
else:
    ep2_viga5= ep2_viga1

ep3= round (((((v5 - (mg_meio / w_inf)) / (-1.1 * novo_p1)) - (1 / area_secao)) * w_inf), 2)

ep4= round (((((v4 - (mg_meio / w_sup)) / (-1.1 * novo_p1)) - (1 / area_secao)) * w_sup), 2)

#Para 1/4 do vão

#EP5 Variável conforme quantidade de vigas - ELS-F

#Viga 01
if qtde_calculos >= 1:
    ep5_viga1= round (((((v1 - (mf_viga1 / w_inf_viga1)) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga1)) * w_inf_viga1), 2)
else:
    ep5_viga1= 0

#Viga 02
if qtde_calculos >= 2:
    ep5_viga2= round (((((v1 - (mf_viga2 / w_inf_viga2)) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga2)) * w_inf_viga2), 2)
else:
    ep5_viga2= 0

#Viga 03
if qtde_calculos >= 3:
    ep5_viga3= round (((((v1 - (mf_viga3 / w_inf_viga3)) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga3)) * w_inf_viga3), 2)
else:
    ep5_viga3= 0

#Viga 04
if qtde_calculos >= 4:
    ep5_viga4= round (((((v1 - (mf_viga4 / w_inf_viga4)) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga4)) * w_inf_viga4), 2)
else:
    ep5_viga4= ep5_viga2

#Viga 05
if qtde_calculos == 5:
    ep5_viga5= round (((((v1 - (mf_viga5 / w_inf_viga5)) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga5)) * w_inf_viga5), 2)
else:
    ep5_viga5= ep5_viga1

#EP6 Variável conforme quantidade de vigas - ELS-D

#Viga 01
if qtde_calculos >= 1:
    ep6_viga1=  round (((((-mqp_viga1 / w_inf_viga1) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga1)) * w_inf_viga1), 2)
else:
    ep6_viga1= 0

#Viga 02
if qtde_calculos >= 2:
    ep6_viga2=  round (((((-mqp_viga2 / w_inf_viga2) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga2)) * w_inf_viga2), 2)
else:
    ep6_viga2= 0

#Viga 03
if qtde_calculos >= 3:
    ep6_viga3=  round (((((-mqp_viga3 / w_inf_viga3) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga3)) * w_inf_viga3), 2)
else:
    ep6_viga3= 0

#Viga 04
if qtde_calculos >= 4:
    ep6_viga4=  round (((((-mqp_viga4 / w_inf_viga4) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga4)) * w_inf_viga4), 2)
else:
    ep6_viga4= ep6_viga2

#Viga 05
if qtde_calculos == 5:
    ep6_viga5=  round (((((-mqp_viga5 / w_inf_viga5) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga5)) * w_inf_viga5), 2)
else:
    ep6_viga5= ep6_viga1

ep7= round (((((v5 - (mg_um_quarto / w_inf)) / (-1.1 * novo_p1)) - (1 / area_secao)) * w_inf), 2)

ep8= round (((((v4 - (mg_um_quarto / w_sup)) / (-1.1 * novo_p1)) - (1 / area_secao)) * w_sup), 2)

#Para o apoio do vão

#EP9 Variável conforme quantidade de vigas - ELS-D

#Viga 01
if qtde_calculos >= 1:
    ep9_viga1=  round (((((-apoio_permanente / w_inf_viga1) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga1)) * w_inf_viga1), 2)
else:
    ep9_viga1= 0

#Viga 02
if qtde_calculos >= 2:
    ep9_viga2=  round (((((-apoio_permanente / w_inf_viga2) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga2)) * w_inf_viga2), 2)
else:
    ep9_viga2= 0

#Viga 03
if qtde_calculos >= 3:
    ep9_viga3=  round (((((-apoio_permanente / w_inf_viga3) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga3)) * w_inf_viga3), 2)
else:
    ep9_viga3= 0

#Viga 04
if qtde_calculos >= 4:
    ep9_viga4=  round (((((-apoio_permanente / w_inf_viga4) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga4)) * w_inf_viga4), 2)
else:
    ep9_viga4= ep9_viga2

#Viga 05
if qtde_calculos == 5:
    ep9_viga5=  round (((((-apoio_permanente / w_inf_viga5) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga5)) * w_inf_viga5), 2)
else:
    ep9_viga5= ep9_viga1

#EP10 Variável conforme quantidade de vigas - ELS-D

#Viga 01
if qtde_calculos >= 1:
    ep10_viga1=  round (((((-apoio_permanente / w_sup_viga1) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga1)) * w_sup_viga1), 2)
else:
    ep10_viga1= 0

#Viga 02
if qtde_calculos >= 2:
    ep10_viga2=  round (((((-apoio_permanente / w_sup_viga2) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga2)) * w_sup_viga2), 2)
else:
    ep10_viga2= 0

#Viga 03
if qtde_calculos >= 3:
    ep10_viga3=  round (((((-apoio_permanente / w_sup_viga3) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga3)) * w_sup_viga3), 2)
else:
    ep10_viga3= 0

#Viga 04
if qtde_calculos >= 4:
    ep10_viga4=  round (((((-apoio_permanente / w_sup_viga4) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga4)) * w_sup_viga4), 2)
else:
    ep10_viga4= ep10_viga2

#Viga 05
if qtde_calculos == 5:
    ep10_viga5=  round (((((-apoio_permanente / w_sup_viga5) / (-novo_p)) - (1 / area_secao_aba_colaborante_viga5)) * w_sup_viga5), 2)
else:
    ep10_viga5= ep10_viga1

ep11= round (((((v5 - (mg_apoio / w_inf)) / (-1.1 * novo_p1)) - (1 / area_secao)) * w_inf), 2)

ep12= round (((((v5 - (mg_apoio / w_sup)) / (-1.1 * novo_p1)) - (1 / area_secao)) * w_sup), 2)

def tabela_meiovao():
    print ("\n------------------------------------------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "1/2 Vão" + color.END)
    print ("Verificações - EP [m]\t\t\tSinal\t\t\tV1\t\tV2\t\tV3\t\tV4\t\tV5")
    print ("------------------------------------------------------------------------------------------------------------")
    print ("%s\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-F (Frequente) - tinf', '=>', ep1_viga1, ep1_viga2, ep1_viga3, ep1_viga4, ep1_viga5))
    print ("%s\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-D (Quase Permanente) - tinf', '=>', ep2_viga1, ep2_viga2, ep2_viga3, ep2_viga4, ep2_viga5))
    print ("%s\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-Cex - t0', '<=', ep3, ep3, ep3, ep3, ep3))
    print ("%s\t\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-F - t0', '<=', ep4, ep4, ep4, ep4, ep4))
    print ("------------------------------------------------------------------------------------------------------------")

def tabela_quartovao():
    print ("\n------------------------------------------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "1/4 Vão" + color.END)
    print ("Verificações - EP [m]\t\t\tSinal\t\t\tV1\t\tV2\t\tV3\t\tV4\t\tV5")
    print ("------------------------------------------------------------------------------------------------------------")
    print ("%s\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-F (Frequente) - tinf', '=>', ep5_viga1, ep5_viga2, ep5_viga3, ep5_viga4, ep5_viga5))
    print ("%s\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-D (Quase Permanente) - tinf', '=>', ep6_viga1, ep6_viga2, ep6_viga3, ep6_viga4, ep6_viga5))
    print ("%s\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-Cex - t0', '<=', ep7, ep7, ep7, ep7, ep7))
    print ("%s\t\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-F - t0', '<=', ep8, ep8, ep8, ep8, ep8))
    print ("------------------------------------------------------------------------------------------------------------")

def tabela_apoio():
    print ("\n------------------------------------------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "Apoio" + color.END)
    print ("Verificações - EP [m]\t\t\tSinal\t\t\tV1\t\tV2\t\tV3\t\tV4\t\tV5")
    print ("------------------------------------------------------------------------------------------------------------")
    print ("%s\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-D (QP) - Inferior - tinf', '=>', ep9_viga1, ep9_viga2, ep9_viga3, ep9_viga4, ep9_viga5))
    print ("%s\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-D (QP) - Superior - tinf', '<=', ep10_viga1, ep10_viga2, ep10_viga3, ep10_viga4, ep10_viga5))
    print ("%s\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-Cex - Inferior - t0', '<=', ep11, ep11, ep11, ep11, ep11))
    print ("%s\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-Cex - Superior - t0', '=>', ep12, ep12, ep12, ep12, ep12))
    print ("------------------------------------------------------------------------------------------------------------")

print (color.BOLD + color.YELLOW + "\n\nTabela de Verificações - EP" + color.END)
tabela_meiovao()
tabela_quartovao()
tabela_apoio()

#13 - Resultados Parciais
if qtde_calculos == 1:
    y_inf_viga2 = 0
    y_inf_viga3 = 0
    y_inf_viga4 = y_inf_viga2
    y_inf_viga5 = y_inf_viga1

elif qtde_calculos == 2:
    y_inf_viga3 = 0
    y_inf_viga4 = y_inf_viga2
    y_inf_viga5 = y_inf_viga1

elif qtde_calculos == 3:
    y_inf_viga4 = y_inf_viga2
    y_inf_viga5 = y_inf_viga1

elif qtde_calculos == 4:
    y_inf_viga5 = y_inf_viga1

novo_ep1_viga1 = round (-(ep1_viga1 - y_inf_viga1), 2)
novo_ep1_viga2 = round (-(ep1_viga2 - y_inf_viga2), 2)
novo_ep1_viga3 = round (-(ep1_viga3 - y_inf_viga3), 2)
novo_ep1_viga4 = round (-(ep1_viga4 - y_inf_viga4), 2)
novo_ep1_viga5 = round (-(ep1_viga5 - y_inf_viga5), 2)
novo_ep2_viga1 = round (-(ep2_viga1 - y_inf_viga1), 2)
novo_ep2_viga2 = round (-(ep2_viga2 - y_inf_viga2), 2)
novo_ep2_viga3 = round (-(ep2_viga3 - y_inf_viga3), 2)
novo_ep2_viga4 = round (-(ep2_viga4 - y_inf_viga4), 2)
novo_ep2_viga5 = round (-(ep2_viga5 - y_inf_viga5), 2)
novo_ep3 = round (-(ep3 - y_inf), 2)
novo_ep4 = round (-(ep4 - y_inf), 2)
novo_ep5_viga1 = round (-(ep5_viga1 - y_inf_viga1), 2)
novo_ep5_viga2 = round (-(ep5_viga2 - y_inf_viga2), 2)
novo_ep5_viga3 = round (-(ep5_viga3 - y_inf_viga3), 2)
novo_ep5_viga4 = round (-(ep5_viga4 - y_inf_viga4), 2)
novo_ep5_viga5 = round (-(ep5_viga5 - y_inf_viga5), 2)
novo_ep6_viga1 = round (-(ep6_viga1 - y_inf_viga1), 2)
novo_ep6_viga2 = round (-(ep6_viga2 - y_inf_viga2), 2)
novo_ep6_viga3 = round (-(ep6_viga3 - y_inf_viga3), 2)
novo_ep6_viga4 = round (-(ep6_viga4 - y_inf_viga4), 2)
novo_ep6_viga5 = round (-(ep6_viga5 - y_inf_viga5), 2)
novo_ep7 = round (-(ep7 - y_inf), 2)
novo_ep8 = round (-(ep8 - y_inf), 2)
novo_ep9_viga1 = round (-(ep9_viga1 - y_inf_viga1), 2)
novo_ep9_viga2 = round (-(ep9_viga2 - y_inf_viga2), 2)
novo_ep9_viga3 = round (-(ep9_viga3 - y_inf_viga3), 2)
novo_ep9_viga4 = round (-(ep9_viga4 - y_inf_viga4), 2)
novo_ep9_viga5 = round (-(ep9_viga5 - y_inf_viga5), 2)
novo_ep10_viga1 = round (-(ep10_viga1 - y_inf_viga1), 2)
novo_ep10_viga2 = round (-(ep10_viga2 - y_inf_viga2), 2)
novo_ep10_viga3 = round (-(ep10_viga3 - y_inf_viga3), 2)
novo_ep10_viga4 = round (-(ep10_viga4 - y_inf_viga4), 2)
novo_ep10_viga5 = round (-(ep10_viga5 - y_inf_viga5), 2)
novo_ep11 = round (-(ep11 - y_inf), 2)
novo_ep12 = round (-(ep12 - y_inf), 2)

def tabela_nova_meiovao():
    print ("\n------------------------------------------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "1/2 Vão" + color.END)
    print ("Verificações - H [m]\t\t\tSinal\t\t\tV1\t\tV2\t\tV3\t\tV4\t\tV5")
    print ("------------------------------------------------------------------------------------------------------------")
    print ("%s\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-F (Frequente) - tinf', '<=', novo_ep1_viga1, novo_ep1_viga2, novo_ep1_viga3, novo_ep1_viga4, novo_ep1_viga5))
    print ("%s\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-D (Quase Permanente) - tinf', '<=', novo_ep2_viga1, novo_ep2_viga2, novo_ep2_viga3, novo_ep2_viga4, novo_ep2_viga5))
    print ("%s\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-Cex - t0', '=>', novo_ep3, novo_ep3, novo_ep3, novo_ep3, novo_ep3))
    print ("%s\t\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-F - t0', '=>', novo_ep4, novo_ep4, novo_ep4, novo_ep4, novo_ep4))
    print ("------------------------------------------------------------------------------------------------------------")

def tabela_nova_quartovao():
    print ("\n------------------------------------------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "1/4 Vão" + color.END)
    print ("Verificações - H [m]\t\t\tSinal\t\t\tV1\t\tV2\t\tV3\t\tV4\t\tV5")
    print ("------------------------------------------------------------------------------------------------------------")
    print ("%s\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-F (Frequente) - tinf', '<=', novo_ep5_viga1, novo_ep5_viga2, novo_ep5_viga3, novo_ep5_viga4, novo_ep5_viga5))
    print ("%s\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-D (Quase Permanente) - tinf', '<=', novo_ep6_viga1, novo_ep6_viga2, novo_ep6_viga3, novo_ep6_viga4, novo_ep6_viga5))
    print ("%s\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-Cex - t0', '=>', novo_ep7, novo_ep7, novo_ep7, novo_ep7, novo_ep7))
    print ("%s\t\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-F - t0', '=>', novo_ep8, novo_ep8, novo_ep8, novo_ep8, novo_ep8))
    print ("------------------------------------------------------------------------------------------------------------")

def tabela_nova_apoio():
    print ("\n------------------------------------------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "Apoio" + color.END)
    print ("Verificações - H [m]\t\t\tSinal\t\t\tV1\t\tV2\t\tV3\t\tV4\t\tV5")
    print ("------------------------------------------------------------------------------------------------------------")
    print ("%s\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-D (QP) - Inferior - tinf', '<=', novo_ep9_viga1, novo_ep9_viga2, novo_ep9_viga3, novo_ep9_viga4, novo_ep9_viga5))
    print ("%s\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-D (QP) - Superior - tinf', '=>', novo_ep10_viga1, novo_ep10_viga2, novo_ep10_viga3, novo_ep10_viga4, novo_ep10_viga5))
    print ("%s\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-Cex - Inferior - t0', '=>', novo_ep11, novo_ep11, novo_ep11, novo_ep11, novo_ep11))
    print ("%s\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('ELS-Cex - Superior - t0', '<=', novo_ep12, novo_ep12, novo_ep12, novo_ep12, novo_ep12))
    print ("------------------------------------------------------------------------------------------------------------")

print (color.BOLD + color.YELLOW + "\n\nTabela de Verificações - H" + color.END)
tabela_nova_meiovao()
tabela_nova_quartovao()
tabela_nova_apoio()

#14 - Resultado Final

#1/2 vão
tinf_meio_viga1 = min(novo_ep1_viga1 , novo_ep2_viga1)
tinf_meio_viga2 = min(novo_ep1_viga2 , novo_ep2_viga2)
tinf_meio_viga3 = min(novo_ep1_viga3 , novo_ep2_viga3)
tinf_meio_viga4 = min(novo_ep1_viga4 , novo_ep2_viga4)
tinf_meio_viga5 = min(novo_ep1_viga5 , novo_ep2_viga5)
t0_meio_viga = max(novo_ep3 , novo_ep4)

#1/4 vão
tinf_quarto_viga1 = min(novo_ep5_viga1 , novo_ep6_viga1)
tinf_quarto_viga2 = min(novo_ep5_viga2 , novo_ep6_viga2)
tinf_quarto_viga3 = min(novo_ep5_viga3 , novo_ep6_viga3)
tinf_quarto_viga4 = min(novo_ep5_viga4 , novo_ep6_viga4)
tinf_quarto_viga5 = min(novo_ep5_viga5 , novo_ep6_viga5)
t0_quarto_viga = max(novo_ep7 , novo_ep8)

#Apoio
apoio1_viga1 = min(novo_ep9_viga1 , novo_ep12)
if apoio1_viga1 == novo_ep9_viga1:
    apoio1_aux = 'ELS-D(QP)-Inf-tinf'
else:
    apoio1_aux = 'ELS-Cex-Sup-t0'
apoio1_viga2 = min(novo_ep9_viga2 , novo_ep12)
apoio1_viga3 = min(novo_ep9_viga3 , novo_ep12)
apoio1_viga4 = min(novo_ep9_viga4 , novo_ep12)
apoio1_viga5 = min(novo_ep9_viga5 , novo_ep12)
apoio2_viga1 = max (novo_ep10_viga1 , novo_ep11)
if apoio2_viga1 == novo_ep10_viga1:
    apoio2_aux = 'ELS-D(QP)-Sup-tinf'
else:
    apoio2_aux = 'ELS-Cex-Inf-t0'
apoio2_viga2 = max (novo_ep10_viga2 , novo_ep11)
apoio2_viga3 = max (novo_ep10_viga3 , novo_ep11)
apoio2_viga4 = max (novo_ep10_viga4 , novo_ep11)
apoio2_viga5 = max (novo_ep10_viga5 , novo_ep11)

if qtde_calculos == 1:
    tinf_meio_viga2 = 0
    tinf_quarto_viga2 = 0
    apoio1_viga2 = 0
    apoio2_viga2 = 0
    tinf_meio_viga3 = 0
    tinf_quarto_viga3 = 0
    apoio1_viga3 = 0
    apoio2_viga3 = 0
    tinf_meio_viga4 = 0
    tinf_quarto_viga4 = 0
    apoio1_viga4 = 0
    apoio2_viga4 = 0
    tinf_meio_viga5 = 0
    tinf_quarto_viga5 = 0
    apoio1_viga5 = 0
    apoio2_viga5 = 0

elif qtde_calculos == 2:
    tinf_meio_viga3 = 0
    tinf_quarto_viga3 = 0
    apoio1_viga3 = 0
    apoio2_viga3 = 0
    tinf_meio_viga4 = 0
    tinf_quarto_viga4 = 0
    apoio1_viga4 = 0
    apoio2_viga4 = 0
    tinf_meio_viga5 = 0
    tinf_quarto_viga5 = 0
    apoio1_viga5 = 0
    apoio2_viga5 = 0

elif qtde_calculos == 3:
    tinf_meio_viga4 = tinf_meio_viga2
    tinf_quarto_viga4 = tinf_quarto_viga2
    apoio1_viga4 = apoio1_viga2
    apoio2_viga4 = apoio2_viga2
    tinf_meio_viga5 = tinf_meio_viga1
    tinf_quarto_viga5 = tinf_quarto_viga1
    apoio1_viga5 = apoio1_viga1
    apoio2_viga5 = apoio2_viga1

elif qtde_calculos == 4:
    tinf_meio_viga5 = tinf_meio_viga1
    tinf_quarto_viga5 = tinf_quarto_viga1
    apoio1_viga5 = apoio1_viga1
    apoio2_viga5 = apoio2_viga1

def tabela_resultado_meio():
    print ("\n------------------------------------------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "1/2 Vão" + color.END)
    print ("Verificações - H [m]\t\tSinal\t\t\tV1\t\tV2\t\tV3\t\tV4\t\tV5")
    print ("------------------------------------------------------------------------------------------------------------")
    print ("%s\t\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('tinf', '<=', tinf_meio_viga1, tinf_meio_viga2, tinf_meio_viga3, tinf_meio_viga4, tinf_meio_viga5))
    print ("%s\t\t\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('t0', '=>', t0_meio_viga, t0_meio_viga, t0_meio_viga, t0_meio_viga, t0_meio_viga))
    print ("------------------------------------------------------------------------------------------------------------")

def tabela_resultado_quarto():
    print ("\n------------------------------------------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "1/4 Vão" + color.END)
    print ("Verificações - H [m]\t\tSinal\t\t\tV1\t\tV2\t\tV3\t\tV4\t\tV5")
    print ("------------------------------------------------------------------------------------------------------------")
    print ("%s\t\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('tinf', '<=', tinf_quarto_viga1, tinf_quarto_viga2, tinf_quarto_viga3, tinf_quarto_viga4, tinf_quarto_viga5))
    print ("%s\t\t\t\t\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % ('t0', '=>', t0_quarto_viga, t0_quarto_viga, t0_quarto_viga, t0_quarto_viga, t0_quarto_viga))
    print ("------------------------------------------------------------------------------------------------------------")

def tabela_resultado_apoio():
    print ("\n------------------------------------------------------------------------------------------------------------")
    print (color.BOLD + color.YELLOW + "Apoio" + color.END)
    print ("Verificações - H [m]\t\tSinal\t\t\tV1\t\tV2\t\tV3\t\tV4\t\tV5")
    print ("------------------------------------------------------------------------------------------------------------")
    print ("%s\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % (apoio1_aux, '<=', apoio1_viga1, apoio1_viga2, apoio1_viga3, apoio1_viga4, apoio1_viga5))
    print ("%s\t\t\t%s\t\t\t\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" % (apoio2_aux, '=>', apoio2_viga1, apoio2_viga2, apoio2_viga3, apoio2_viga4, apoio2_viga5))
    print ("------------------------------------------------------------------------------------------------------------")

print(color.BOLD + color.YELLOW + "\n\nTabela de Resultados Finais - H" + color.END)
tabela_resultado_meio()
tabela_resultado_quarto()
tabela_resultado_apoio()
