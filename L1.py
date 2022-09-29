def rek(state,kata):
        if len(kata) == 0:
            return "0"
        a=kata[len(kata)-1]
        stslan=rek(state,kata[:len(kata)-1])
        match stslan:
            case "0":
                if a=="0":
                    return "1"
                elif a=="1":
                    return "3"
            case "1":
                if a=="0":
                    return "1"
                elif a=="1":
                    return "2"
            case "2":
                if a=="0":
                    return "1"
                elif a=="1":
                    return "2"
            case "3":
                if a=="0":
                    return "4"
                elif a=="1":
                    return "3"
            case "4":
                if a=="0":
                    return "4"
                elif a=="1":
                    return "3"
        

def mulai(kata):
    F=["1","3","0"]
    hsl=rek(0,kata)
    if hsl in F :
        print("diterima")
    else:
        print("ditolak")
