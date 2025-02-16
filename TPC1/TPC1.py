s = "Estou a fazer um trabalho"

#1 - given a string "s", reverse it

def reverse(string):
    rev = string[::-1]
    return rev

palavra = reverse(s)
print(palavra)

#2 - given a string "s", returns how many "a" and "A" characters are present in it

def contagem_aA(string):
    count = 0
    for letra in string:
        if letra=='a' or letra=='A':
            count+=1
    return count

print(contagem_aA(s))

#3 -  given a string "s", returns the number of vowels there are present in it

def contagemVogais(string):
    contador =0
    s = string.upper()
    for caracter in s:
        if caracter == "A" or caracter == "E" or  caracter == "I" or caracter == "O" or caracter == "U":
            contador +=1
    return contador

print(contagemVogais(s))

#4 - given a string "s", convert it into lowercase

def lowerCase(s):
    return s.lower()

print(lowerCase(s))

#5 - given a string "s", convert it into uppercase

def upperCase(s):
    return s.upper()

print(upperCase(s))

#6 - Verifica se uma string é capicua

def capicua(string):
    palavra = reverse(string)
    return  palavra.lower() == string.lower()

print(capicua("Ana"))
print(capicua("palavra"))

#7 - Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão balanceadas se todos os caracteres de s1 estão presentes em s2)

def balanceado(s1,s2):
    
    lista1 = []
    lista2 = []
    
    for caracter in s1:
        if caracter not in lista1:
            lista1.append(caracter)
    for caracter in s2:
        if caracter not in lista2:
            lista2.append(caracter)
    
    lista1 = sorted(lista1)
    lista2 = sorted(lista2)
    
    return lista1==lista2

print(balanceado("estou","bala"))
print(balanceado("rab","bara"))

#8 - Calcula o número de ocorrências de s1 em s2

def ocorrencias(s1,s2):
    contador = 0 #Vai contar o número de ocorrências
        
    for i in range(len(s2) - len(s1) + 1): #garante que é possível encontrar as ocorrências em s2
        if s2[i:i + len(s1)] == s1: 
            contador = contador + 1
    return contador

ocorrencias("ola", "olaolaola") 

#9 - Verifica se s1 é anagrama de s2

def anagrama3(s1,s2):
    return sorted(s1) == sorted(s2)

print(anagrama3("listen","silent"))
print(anagrama3("hello","world"))


#10 - Dado um dicionário, calcular a tabela das classes de anagramas

def anagrama(s1,s2):
    dic1={}
    dic2={}
    
    for caracter in s1:
        if caracter not in dic1.values():
            dic1[caracter]=1
        else:
            dic1[caracter]+=1
    for caracter in s2:
        if caracter not in dic2.values():
            dic2[caracter]=1
        else:
            dic2[caracter]+=1
    
    dic1 = sorted(dic1.items())
    dic2 = sorted(dic2.items())
    
    return dic1==dic2

print(anagrama("listen","silent"))
print(anagrama("hello","world"))