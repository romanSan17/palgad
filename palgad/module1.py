
def inimeste_ja_palkade_lisamine(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uendatud loendid, kus lusatud inimesi ja palka
    :param list i: inimiste järjend
    :param list p: Palgate järjend
    :param int n: Inimeste arv
    :rtype: list,list
    """
    if n>0:
        for j in range(n):
            nimi=input("Nimi: ").capitalize()
            palk=int(input("Palk: "))
            i.append(nimi)
            p.append(palk)
    return i,p
def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    :param list i:Inimeste järjendid
    :param list p: Palgate järjendid
    """
    for j in range(len(i)):
        print(i[j],"-",p[j])
def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andmeid ja tagastab listid
    :param list i:Inimeste järjendid
    :param list p: Palgate järjendid
    :rtype: list, list
    """
    nimi=input("Keda kustutuda ära(nimi): ")
    for j in range(len(i)):
        if nimi in i:
            i.remove(nimi)
            p.pop(j)
    return i,p
def kellel_on_suurim_palk(i:list,p:list)->any:
    """Funktsioon
    :param list i:Inimeste järjendid
    :param list p: Palgate järjendid
    """
    nimed=[]
    max_palk=max(p)
    ind=-1
    for palk in p:
        if palk==max_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed

def kellel_on_vaiksem_palk(i:list,p:list)->any:
    """Funktsioon
    :param list i:Inimeste järjendid
    :param list p: Palgate järjendid
    """
    nimed=[]
    min_palk=min(p)
    ind=-1
    for palk in p:
        if palk==min_palk:
            ind+=1
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
    return nimed

def sorteerimine(i:list,p:list):
    """Funktsioon palga sorteerimise
    :param list i:Inimeste järjendid
    :param list p: Palgate järjendid
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
return i,p
