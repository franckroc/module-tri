def tri(name,tab,direction):

    # name : "fusion" or "buble"
    # tab : list of data
    # direction : "increase" or "decrease"

    name = name.lower()
    direction = direction.lower()
    
    if name == "fusion" or name == "buble":
        if direction == "increase" or direction == "decrease":
            if type(tab) == list:

                match name:  #tri adapté au big data

                    case "fusion":

                        if len(tab) > 1:
                            mid = len(tab)//2
                            A = tab[:mid]
                            B = tab[mid:]
                            tri(name,A,direction)
                            tri(name,B,direction)

                            i = j = k = 0

                            while i < len(A) and j < len(B):
                                if direction == "increase":

                                    if A[i] < B[j]:
                                        tab[k] = A[i]
                                        i += 1
                                    else:
                                        tab[k] = B[j]
                                        j += 1

                                elif direction == "decrease":

                                    if A[i] > B[j]:
                                        tab[k] = A[i]
                                        i += 1
                                    else:
                                        tab[k] = B[j]
                                        j += 1
                                k += 1

                            while i < len(A):
                                tab[k] = A[i]
                                i += 1
                                k += 1

                            while j < len(B):
                                tab[k] = B[j]
                                j += 1
                                k += 1
                        return tab

                    case "buble":  #tri adapté aux petites listes

                        a = 0
                        while a < len(tab):
                            for i in range(len(tab)-1):

                                if direction == "increase":
                    
                                    if tab[i] > tab[i+1]:
                                        temp = tab[i+1]
                                        tab.pop(i+1)
                                        tab.insert(i,temp)

                                elif direction == "decrease":

                                    if tab[i] < tab[i+1]:
                                        temp = tab[i+1]
                                        tab.pop(i+1)
                                        tab.insert(i,temp)
                            a+=1
                        return tab
            else:
                return "Erreur data: data's type not list"
        else:
            return 'Erreur direction : must be "increase" or "decrease" '
    else:
        return 'Erreur name : must be "fusion" or "buble" '
          