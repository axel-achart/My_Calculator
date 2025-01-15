

while True:# boucle infinie qui continue le programme tant que la reponse est invalide(pas un nombre)
    
    try:#essaie de faire ce qu'i y a dans le block qui suit et qui comporte un risque d erreur

        number1 = int(input('enter first number : '))#permet a l utilisateur d entrer une valeur souhaitée
        number2 = int(input('enter second number : '))
        print(number1)#print la valeur entré
        break#stop la boucle while si bonne entrée
    
    except ValueError:#si on rencontre une erreur "fais plutot..." en gros il gere l erreur
        print('invalid entry')#message qui s affiche en cas d erreur

while True:

    operator = input("Choose an operator (+,-,*,/) : " )#demande a l utilisateur d'entrer un operateur
    if operator in ['+', '-', '*', '/']:#verification de l'entrée si valide ou non
     
     print(operator)#print la valeur entré
     break#stop la boucle while si bonne entrée
      
    else:#si on rencontre une erreur "fais plutot..." en gros il gere l erreur
        print('invalid entry')#message qui s affiche en cas d erreur


if operator == '+':
    result = number1 + number2

elif operator == '-':
    result = number1 - number2

elif operator == '*':
    result = number1 * number2

elif operator == '/':
    result = number1 / number2

print(f"Result is : {result}")

#while True:# boucle infinie qui continue le programme tant que la reponse est invalide(pas un nombre)
    
   # try:#essaie de faire ce qu'i y a dans le block qui suit et qui comporte un risque d erreur

        #number2 = int(input('enter second number : '))#permet a l utilisateur d entrer une valeur souhaitée
        #print(number1)#print la valeur entré
        #break#stop la boucle while si bonne entrée
      
    #except ValueError:#si on rencontre une erreur "fais plutot..." en gros il gere l erreur
        #print('invalid entry')#message qui s affiche en cas d erreur


#while True:# boucle infinie qui continue le programme tant que la reponse est invalide(pas bon opérateur)
 #   operator = input("Choose an operator (+,-,*,/) : " )#demande a l utilisateur d'entrer un operateur
  #  if operator in ['+', '-', '*', '/']:#verification de l'entrée si valide ou non
     
   #  print(operator)#print la valeur entré
    # break#stop la boucle while si bonne entrée
      
    #else:#si on rencontre une erreur "fais plutot..." en gros il gere l erreur
     #   print('invalid entry')#message qui s affiche en cas d erreur

    
    


        

       






#main()