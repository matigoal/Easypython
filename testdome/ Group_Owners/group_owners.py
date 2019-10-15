def group_by_owners(files):#création de la fonction en paramètre files
    done= {} # futur contenant du tableau
    for file, owner in files.items():  # boucle sur la séquence 
        done[owner] = done.get(owner, []) + [file]   
    return done

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}#Ensemble de  fichiers
