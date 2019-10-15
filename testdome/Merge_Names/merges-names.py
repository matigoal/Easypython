def unique_names(list1, list2): #création de la fonction en paramètre list1 et list2
    return list(set().union(list1, list2))#set pour créer des ensembles.

list1 = ["Ava", "Emma", "Olivia"]#Créez un tableau contenant des noms
list2 = ["Olivia", "Sophia", "Emma"]#Créez d'un deuxième  tableau contenant des noms
print(unique_names(list1, list2)) # si les test fonctionne à la fin imprimer Ava, Emma, Olivia, Sophia
