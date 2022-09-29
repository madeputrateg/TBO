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
                    return "0"
            case "1":
                if a=="0":
                    return "2"
                elif a=="1":
                    return "0"
            case "2":
                if a=="0":
                    return "3"
                elif a=="1":
                    return "0"
            case "3":
                if a=="0":
                    return "3"
                elif a=="1":
                    return "3"



        

def mulai(kata):
    F=["3"]
    hsl=rek(0,kata)
    if hsl in F :
        print("diterima")
    else:
        print("ditolak")


