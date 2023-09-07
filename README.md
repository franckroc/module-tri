# module-tri

Module de tri d'une liste.
tri "fusion" ou tri "bubble"
ordre croissant ou décroissant

Utilisation python:

import module-tri #  ou from module-tri import tri
result = tri(name,tab,direction)

    # where name must be: "fusion" or "buble"
    #       tab : your list
    #       direction must be: "increase" or "decrease"
    
 Exemple:
 
 from module-tri import tri
 
 tab = [100,1,-8,2500,-10,56,-100,3,8,725,-65]
 result = tri("buble",tab,"decrease")
 print(result)
