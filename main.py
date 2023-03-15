import decode

text = '''
vzcbeg gvzr
vzcbeg bf
vzcbeg fhocebprff

# Qb abg gel gb rqvg guvf pbqr, qbvat fb jvyy erfhyg va n onq reebe naq punatrf jvyy abg or fnirq
qrs trg_qve():
    cngu = bf.trgpjq()
    svyrf = bf.yvfgqve(cngu)

    sbe svyr va svyrf:
        shyy_cngu = bf.cngu.wbva(cngu, svyr)
        cevag(shyy_cngu)


qrs glcr(grkg):
    sbe pune va grkg:
        cevag(pune, raq="", syhfu=Gehr)
        gvzr.fyrrc(0.05)
    cevag()


eha_ntnva = Gehr
juvyr eha_ntnva:
    pq = trg_qve()
    cevag(
        "[34z"
        + e"""
  ____       _   _              _____       _           _        _ _  __      ____ 
 |  _ \     | | | |            |  __ \     (_)         | |      | | | \ \    / /_ |
 | |_) | ___| |_| |_ ___ _ __  | |__) |   _ _ _ __  ___| |_ __ _| | |  \ \  / / | |
 |  _ < / _ \ __| __/ _ \ '__| |  ___/ | | | | '_ \/ __| __/ _` | | |   \ \/ /  | |
 | |_) |  __/ |_| ||  __/ |    | |   | |_| | | | | \__ \ || (_| | | |    \  /   | |
 |____/ \___|\__|\__\___|_|    |_|    \__, |_|_| |_|___/\__\__,_|_|_|     \/    |_|
                                       __/ |                                       
                                      |___/                                        
    """
        + "[0z"
    )
    glcr("vf gur svyr lbh jnag va gur pheerag qverpgbel? [l]/[a]:  ")
    n = vachg().ybjre()
    k = 0
    juvyr k == 0:
        vs n == "l":
            cevag(pq)
            oernx
        ryvs n == "a":
            gel:
                bf.puqve(vachg("Jung vf gur arj qverpgbel: "))
                oernx
            rkprcg:
                cevag("Abg n inyvq qverpgbel. Cyrnfr gel ntnva.")
                k = 0
        ryfr:
            cevag("Abg na nafjre")
            oernx
    glcr("Fgrc bar abj npgvingvat")
    gvzr.fyrrc(0.5)
    glcr("Fgrc bar abj npgvir")

    sa = vachg("Jung vf gur svyr anzr: ")
    k = 0
    juvyr k == 0:
        vs abg bf.cngu.rkvfgf(sa) be abg sa.raqfjvgu(".cl"):
            glcr("Gung vf abg n inyvq svyr be vg qbrf abg rkvfg")
            glcr("ABGR: Guvf bayl fhccbegf .cl svyrf")
            k = 0
        ryfr:
            glcr("Svyr unf orra irevsvrq, gvzr sbe fgrc 2")
            gvzr.fyrrc(0.5)
            glcr("Pbairegvat svyr gb rkrphgnoyr...")
            k = 1

    gel:
        ortvavat_gvzr = gvzr.gvzr()
        fhocebprff.eha(["clvafgnyyre", "--barsvyr", sa], purpx=Gehr)
        glcr("Svyr unf orra fhpprffshyyl pbairegrq gb rkrphgnoyr!")
        raq_gvzr = gvzr.gvzr()
    rkprcg fhocebprff.PnyyrqCebprffReebe:
        glcr("Reebe: Snvyrq gb pbaireg svyr gb rkrphgnoyr")

    qg = gvzr.gvzr()
    gbgny_gvzr = ortvavat_gvzr.__sybbe__() - raq_gvzr.__sybbe__()
    gbgny_gvzr = s"{gbgny_gvzr}"
    gbgny_gvzr = gbgny_gvzr.erzbircersvk("-")
    glcr(s"Guvf gbbx {gbgny_gvzr} frpbaqf gb qbjaybnq {sa}")
    glcr("Gunax lbh sbe hfvat Orggre Vafgnyyre")
    glcr("Perqvgf gb Qerkkl sbe cebtenzzvat naq Yrapnab sbe gur vqrn :)")
    glcr("jbhyq lbh yvxr gb qb nabgure svyr? [l]/[a]: ")
    ehantnva = vachg().ybjre()
    q = Snyfr

    juvyr abg q:
        
        vs ehantnva == "l":
            eha_ntnva = Gehr
            q = Gehr
        ryvs ehantnva == "a":
            eha_ntnva = Snyfr
            q = Gehr
        ryfr:
            cevag("Abg n inyvq njafre gel ntnva")
            q = Snyfr




'''

exec(decode.decode(text=text))
