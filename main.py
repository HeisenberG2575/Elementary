import mysql.connector
import random
con=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='chem')
cur=con.cursor()
data={
"H":["Hydrogen",1,1.0,1,1,'nm'], #symbol name atno mass period grp type
"He":['Helium', 2, 4.0, 1, 18, 'nm'],
"Li":['Lithium', 3, 7.0, 2, 1,'m'],
"Be":['Beryllium', 4, 9.0, 2, 2,'m'],
"B":['Boron', 5, 10.8, 2, 13, 'me'],
"C":['Carbon', 6, 12.0, 2, 14, 'nm'],
"N":['Nitrogen', 7, 14.0, 2, 15, 'nm'],
"O":['Oxygen', 8, 16.0, 2, 16, 'nm'],
"F":['Fluorine', 9, 19.0, 2, 17, 'nm'],
"Ne":['Neon', 10, 20.2, 2, 18, 'nm'],
"Na":['Sodium', 11, 23.0, 3, 1, 'm'],
"Mg":['Magnesium', 12, 24.3, 3, 2, 'm'],
"Al":['Aluminium', 13, 27.0, 3, 13, 'm'],
"Si":['Silicon', 14, 28.0, 3, 14, 'me'],
"P":['Phosphorus', 15, 31.0, 3, 15, 'nm'],
"S":['Sulphur', 16, 32.0, 3, 16, 'nm'],
"Cl":['Chlorine', 17, 35.5, 3, 17, 'nm'],
"Ar":['Argon', 18, 40.0, 3, 18, 'nm'],
"K":['Potassium', 19, 39.0, 4, 1, 'm'],
"Ca":['Calcium', 20, 40.0, 4, 2, 'm'],
"Sc":['Scandium', 21, 45.0, 4, 3, 'm'],
"Ti":['Titanium', 22, 47.9, 4, 4, 'm'],
"V":['Vanadium', 23, 50.9, 4, 5, 'm'],
"Cr":['Chromium', 24, 51.9, 4, 6, 'm'],
"Mn":['Manganese', 25, 54.9, 4, 7, 'm'],
"Fe":['Iron', 26, 55.8, 4, 8, 'm'],
"Ni":['Nickel', 28, 58.7, 4, 9, 'm'],
"Co":['Cobalt', 27, 58.9, 4, 10, 'm'],
"Cu":['Copper', 29, 63.5, 4, 11, 'm'],
"Zn":['Zinc', 30, 65.3, 4, 12, 'm'],
"Ga":['Gallium', 31, 69.7, 4, 13, 'm'],
"Ge":['Germanium', 32, 72.5, 4, 14, 'me'],
"As":['Arsenic', 33, 74.9, 4, 15, 'me'],
"Se":['Selenium', 34, 79.0, 4, 16, 'nm'],
"Br":['Bromine', 35, 79.9, 4, 17, 'nm'],
"Kr":['Krypton', 36, 83.8, 4, 18, 'nm'],
"Rb":['Rubidium', 37, 85.5, 5, 1, 'm'],
"Sr":['Strontium', 38, 87.6, 5, 2, 'm'],
"Y":['Yttrium', 39, 88.9, 5, 3, 'm'],
"Zr":['Zirconium', 40, 91.2, 5, 4, 'm'],
"Nb":['Niobium', 41, 92.9, 5, 5, 'm'],
"Mo":['Molybdenum', 42, 95.9, 5, 6, 'm'],
"Tc":['Technitium', 43, 98.0, 5, 7, 'm'],
"Ru":['Ruthenium', 44, 101.0, 5, 8, 'm'],
"Rh":['Rhodium', 45, 102.9, 5, 9, 'm'],
"Pd":['Palladium', 46, 106.4, 5, 10, 'm'],
"Ag":['Silver', 47, 107.9, 5, 11, 'm'],
"Cd":['Cadmium', 48, 112.4, 5, 12, 'm'],
"In":['Indium', 49, 114.82, 5, 13, 'm'],
"Sn":['Tin', 50, 118.7, 5, 14, 'm'],
"Sb":['Antimony', 51, 121.8, 5, 15, 'me'],
"I":['Iodine', 53, 126.9, 5, 17, 'nm'],
"Te":['Tellurium', 52, 127.6, 5, 16, 'me'],
"Xe":['Xenon', 54, 131.3, 5, 18, 'nm'],
"Cs":['Cesium', 55, 132.9, 6, 1, 'm'],
"Ba":['Barium', 56, 137.3, 6, 2, 'm'],
"La":['Lanthanum', 57, 138.9, 6, 3, 'm'],
"Ce":['Cerium', 58, 140.1, 'f1', 'f', 'm'],
"Pr":['Praseodymium', 59, 140.9, 'f1', 'f', 'm'],
"Nd":['Neodymium', 60, 144.2, 'f1', 'f', 'm'],
"Pm":['Promethium', 61, 145.0, 'f1', 'f', 'm'],
"Sm":['Samarium', 62, 150.4, 'f1', 'f', 'm'],
"Eu":['Europium', 63, 152.0, 'f1', 'f', 'm'],
"Gd":['Gadolinium', 64, 157.3, 'f1', 'f', 'm'],
"Tb":['Terbium', 65, 158.9, 'f1', 'f', 'm'],
"Dy":['Dysprosium', 66, 162.5, 'f1', 'f', 'm'],
"Ho":['Holmium', 67, 164.9, 'f1', 'f', 'm'],
"Er":['Erbium', 68, 167.3, 'f1', 'f', 'm'],
"Tm":['Thulium', 69, 168.9, 'f1', 'f', 'm'],
"Yb":['Ytterbium', 70, 173.0, 'f1', 'f', 'm'],
"Lu":['Lutetium', 71, 175.0, 'f1', 'f', 'm'],
"Hf":['Hafnium', 72, 178.5, 6, 4, 'm'],
"Ta":['Tantalum', 73, 180.9, 6, 5, 'm'],
"W":['Tungsten', 74, 183.9, 6, 6, 'm'],
"Re":['Rhenium', 75, 186.2, 6, 7, 'm'],
"Os":['Osmium', 76, 190.2, 6, 8, 'm'],
"Ir":['Iridium', 77, 192.2, 6, 9, 'm'],
"Pt":['Platinum', 78, 195.0, 6, 10, 'm'],
"Au":['Gold', 79, 197.0, 6, 11, 'm'],
"Hg":['Mercury', 80, 200.6, 6, 12, 'm'],
"Tl":['Thallium', 81, 204.4, 6, 13, 'm'],
"Pb":['Lead', 82, 207.2, 6, 14, 'm'],
"Bi":['Bismuth', 83, 209.0, 6, 15, 'm'],
"Po":['Polonium', 84, 209.0, 6, 16, 'me'],
"At":['Astatine', 85, 210.0, 6, 17, 'nm'],
"Rn":['Radon', 86, 222.0, 6, 18, 'nm'],
"Fr":['Francium', 87, 223.0, 7, 1, 'm'],
"Ra":['Radium', 88, 226.0, 7, 2, 'm'],
"Ac":['Actinium', 89, 227.0, 7, 3, 'm'],
"Pa":['Protactinium', 91, 231.0, 'f2', 'f', 'm'],
"Th":['Thorium', 90, 232.0, 'f2', 'f', 'm'],
"Np":['Neptunium', 93, 237.0, 'f2', 'f', 'm'],
"U":['Uranium', 92, 238.0, 'f2', 'f', 'm'],
"Pu":['Plutonium', 94, 242.0, 'f2', 'f', 'm'],
"Am":['Americium', 95, 243.0, 'f2', 'f', 'm'],
"Bk":['Berkelium', 97, 247.0, 'f2', 'f', 'm'],
"Cm":['Curium', 96, 247.0, 'f2', 'f', 'm'],
"No":['Nobelium', 102, 250.0, 'f2', 'f', 'm'],
"Cf":['Californium', 98, 251.0, 'f2', 'f', 'm'],
"Es":['Einsteinium', 99, 252.0, 'f2', 'f', 'm'],
"Hs":['Hassium', 108, 255.0, 7, 8, 'm'],
"Mt":['Meitnerium', 109, 256.0, 7, 9, 'm'],
"Fm":['Fermium', 100, 257.0, 'f2', 'f', 'm'],
"Md":['Mendelevium', 101, 258.0, 'f2', 'f', 'm'],
"Lr":['Lawrencium', 103, 260.0, 'f2', 'f', 'm'],
"Rf":['Rutherfordium', 104, 261.0, 7, 4, 'm'],
"Bh":['Bohrium', 107, 262.0, 7, 7, 'm'],
"Db":['Dubnium', 105, 262.0, 7, 5, 'm'],
"Sg":['Seaborgium', 106, 263.0, 7, 6, 'm'],
"Ds":['Dysporium', 110, 269.0, 7, 10, 'm'],
"Rg":['Roentgenium', 111, 272.0, 7, 11, 'm'],
"Cn":['Copernicium', 112, 277.0, 7, 12, 'm'],
"Fl":['Flerovium', 114, 289.0, 7, 14, 'm'],
"Nh":['Nihonium', 113, 286.0, 7, 13, 'm'],
"Mc":['Moscovium', 115, 288.0, 7, 15, 'm'],
"Lv":['Livermorium', 116, 292.0, 7, 16, 'm'],
"Ts":['Tennessine', 117, 294.0, 7, 17, 'nm'],
"Og":['Oganesson', 118, 294.0, 7, 18, 'nm']
}
#misc
###########################################################################################################################################
invalid='Errrr Invalid Input! Try Again \U0001F615'
atnos,names,symbols,periods,groups,pandg,adminpas=None,None,None,None,None,None,None

def variables():
    def sqlvar(fx):
        st='select distinct {} from elements'.format(fx)
        cur.execute(st)
        tempdata=cur.fetchall()
        d=[]
        if fx!='period,grp':
            for x in tempdata:
                d+=[x[0]]
        else:
            for x in tempdata:
                d+=[[x[0],x[1]]]
        return d
    global names,symbols,periods,groups,atnos,pandg,adminpas
    atnos=sqlvar('atno')
    names=sqlvar('name')
    symbols=sqlvar('symbol')
    periods=sqlvar('period')
    groups=sqlvar('grp')
    pandg=sqlvar('period,grp') # p and g
    cur.execute('select * from admin')
    temp=cur.fetchall()
    adminpas=temp[0][0]
def tablecreate(tablename):
    if tablename=='elements':
        st='''create table elements(
atno int,
name varchar(50) unique,
symbol varchar(3) unique,
mass float,
period varchar(2),
grp varchar(2),
type char(2) default 'm')'''
        
    if tablename=='leaderboard':
        st='create table leaderboard (userid varchar(50), score int)'
    if tablename=='compounds':
        st='create table compounds (name varchar(75) primary key,mass float, frequency int)'
    if tablename=='admin':
        st='create table admin (password varchar(100) default "admin")'
    try:
        cur.execute(st)
        con.commit()
    except Exception as e:
        print(e)
def datatransfer():
    for x in range(1,119):
        for y in data.keys():
            if data[y][1]==x:
                print(y)
                temp=(x,data[y][0],y,data[y][2],str(data[y][3]),str(data[y][4]),str(data[y][5]))
                print(temp)
                st='insert into elements values {}'.format(temp)
                try:
                    cur.execute(st)
                    con.commit()
                except Exception as e:
                    print(e)
    return 'Restoration Successful ! \U0001F603'
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def intro():
    print('''
#### ######## # #####     ##### ##    #### ##    ## #### ####### ###### ##### #####  ## ##
 ##     ##    # ##        ##    ##    ##   ###  ### ##   ##   ##   ##   ## ## #  ##  ## ##
 ##     ##      #####     ##### ##    #### ######## #### ##   ##   ##   ##### #####  #####
 ##     ##         ##     ##    ##    ##   ###  ### ##   ##   ##   ##   ## ## ## ##     ##
####    ##      #####     ##### ##### #### ###  ### #### ##   ##   ##   ## ## ##  ## ##### -HeisenberG
''')
comp=''
def menu():
    while True:
        menuvar=int(input('''
        Welcome !! Enter the feature code you wish to use when prompted
        1.Search Element
        2.View Elements 
        3.Calculate Mass of Compound
        4.Be a Scientist! Change the periodic table of elements
        5.Frequently searched compounds
        6.Elementary Quiz
        7.Change Admin Password
        0.Exit
        '''))
        if menuvar==1:
            searchmain()
        elif menuvar==2:
            viewmain()
        elif menuvar==3:
            global comp
            comp=str(input('Enter Compound'))
            massvariables()
            test=mass(0,len(comp))
            evaluate(test)
            print(test)
            print('Mass of',comp,'is',resultmass)
            compound_add(comp,resultmass)
        elif menuvar==4:
            changepttable()
        elif menuvar==5:
            compound_main()
        elif menuvar==6:
            quiz()
        elif menuvar==7:
            adminmenu()
        elif menuvar==0:
            break
        else:
            print(invalid)
            menu()
#******************************************************************************************************************************************            
def searchmain():
    menu1=int(input('''
        Search by
        1.Name 
        2.Atomic Number
        3.Symbol 
        4.Period and Group
        '''))
    if menu1==1:
        search1=str(input("Enter Name "))
        if search1 in names:
            searchcore(search1,'name')
        else:
            print(invalid)
    if menu1==2:
        search1=int(input("Enter Atomic Number "))
        if search1 in atnos:
            searchcore(search1,'atno')
        else:
            print(invalid)
    if menu1==3:
        search1=str(input("Enter Symbol "))
        if search1 in symbols:
            searchcore(search1,'symbol')
        else:
            print(invalid)
    if menu1==4:
        search1_1=str(input("Enter Period "))
        search1_2=str(input("Enter Group "))
        if [search1_1,search1_2] in pandg:
            st='select * from elements where period={} and grp={}'.format(search1_1,search1_2)
            try:
                cur.execute(st)
                pprint()
            except Exception as e:
                print(e)
        else:
            print(invalid)
def searchcore(fx,ffield):
    if ffield=='atno':
        st='select * from elements where {}={}'.format(ffield,fx)
    else:
        st="select * from elements where {}='{}'".format(ffield,fx)
    try:
        cur.execute(st)
        pprint()
    except Exception as e:
        print("Error !! ",e)
def pprint():
    data=cur.fetchone()
    print('\n','Atomic Number ',data[0],'\n', 'Name ',data[1],'\n','Symbol ',data[2],'\n','Mass ',data[3],'\n','Period ',data[4],'\n','Group ',data[5])
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def viewmain():
    menu2=int(input('''
        View by
        1.Period (Symbols only)
        2.Group (Symbols only)
        3.Period (Complete info)
        4.Group (Complete info
        5.Block
        6.Main Menu
        '''))
    if menu2==1:
        view1=str(input("Enter period number "))
        if view1 in periods:
            viewcore(view1,'period',False)
        else:
            print(invalid)
    if menu2==2:
        view1=str(input("Enter group number "))
        if view1 in groups:
            viewcore(view1,'grp',False)
        else:
            print(invalid)
    if menu2==3:
        view1=str(input("Enter period number "))
        if view1 in periods:
            viewcore(view1,'period',True)
        else:
            print(invalid)
    if menu2==4:
        view1=str(input("Enter group number "))
        if view1 in groups:
            viewcore(view1,'grp',True)
        else:
            print(invalid)
    if menu2==6:
        menu()
    if menu2==5:
        view1=str(input("Enter Block "))
        if view1 in ('s','S','p','P','d','D','f','F'):
            viewcoreblock(view1)
        else:
            print("Errr Invalid Input ! Try Again")
            viewmain()
def viewcore(fx,ffield,completeinfo): #completeinfo is true or false
    if ffield!='block':
        if not completeinfo:
            st='select symbol from elements where {}={}'.format(ffield,fx)
        else:
            st='select * from elements where {}={}'.format(ffield,fx)
        try:
            cur.execute(st)
            L=cur.fetchall()
        except Exception as e:
            print("Not Found :/")
            print(e)
        if ffield=='period' and not completeinfo:
            for x in L:
                print(x[0],sep=' ',end=' ')
        elif ffield=='grp' and not completeinfo:
            for x in L:
                print(x[0],end='\n')
        elif completeinfo:
            for x in L:
                print('Atomic Number',x[0], 'Name',x[1],'Symbol',x[2],'Mass',x[3],'Period',x[4],'Group',x[5])
def viewcoreblock(block):
    if block in ('s','S'):
        st1='select symbol,period from elements where grp in ("1","2")'
    if block in ('d','D'):
        st1='select symbol,period from elements where grp in ("3","4","5","6","7","8","9","10","11","12")'
    if block in ('p','P'):
        st1='select symbol,period from elements where grp in ("13","14","15","16","17","18")'
    if block in ('f','F'):
        st1='select symbol,period from elements where grp="f"'
    try:
        cur.execute(st1)
        data1=cur.fetchall()
    except Exception as e:
        print(e)
    if block not in ('f','F'):
        for x in range(1,len(periods)+1): # to also show members of group added by user 
            for y in data1:
                if x==int(y[1]):
                    print(y[0],sep=' ',end=' ')
            print('')
    else:
        for x in ('f1','f2'):
            for y in data1:
                if x==y[1]:
                    print(y[0],sep=' ',end=' ')
#******************************************************************************************************************************************
L,closingbracketindex,bracketelements,resultmass=None,None,None,None  
def massvariables():
    global L,comp,closingbracketindex,bracketelements,resultmass
    L=[]
    closingbracketindex=[]
    bracketelements=[]
    resultmass=0 
def mass(start,end,bracket=False):
    global L,comp,closingbracketindex
    lmass=[]
    bracketmass=0
    braele=bracketelements
    for x in range(start,end):
        if x not in bracketelements:
            if comp[x].isupper():
                if x+1<len(comp)and comp[x+1].islower():
                    tempelement=comp[x]+comp[x+1]
                    if x+2<len(comp) and comp[x+2].isdigit():
                        factor=int(mass_factor(x+2,comp))
                        lmass+=[factor*(mass_sqlgetmass(tempelement))]
                    else:
                        lmass+=[mass_sqlgetmass(tempelement)]
                elif x+1<len(comp) and comp[x+1].isdigit():
                    tempfactor=mass_factor(x+1,comp)
                    factor=int(tempfactor)
                    lmass+=[factor*(mass_sqlgetmass(comp[x]))]
                elif x+1<len(comp) and (comp[x+1].isupper() or comp[x+1]==')' or comp[x+1]==']') :
                    lmass+=[mass_sqlgetmass(comp[x])]
                elif x+1==len(comp):
                    lmass+=[mass_sqlgetmass(comp[x])]
            elif comp[x]=='(' or comp[x]=='[' and x not in bracketelements:
                for y in range(-1,-len(comp),-1):
                    if (y not in closingbracketindex )and (comp[y]==')' or comp[y]==']'):
                        closingbracketindex+=[y]
                        break
                bracketcomp=[x+1,y+len(comp)]
                tempfactor=''
                factor=1 
                if y+len(comp)+1<len(comp) and comp[y+len(comp)+1].isdigit():
                    tempfactor=mass_factor(y+1+len(comp),comp)
                    factor=int(tempfactor)
                bracketlist=mass(bracketcomp[0],bracketcomp[1],True)
                for tempx in range(0,len(bracketlist)):
                    bracketlist[tempx]*=factor
                lmass+=[bracketlist]
                skipindex=[]
                for a in range(x+1,y+len(comp)+len(tempfactor)+1):
                    skipindex.append(a)
                bracketelements.extend(skipindex)
            elif comp[x].isdigit() or comp[x]==')' or comp[x]==']':
                continue
    return lmass
def mass_factor(fx,fcomp):
    factor=fcomp[fx]
    while factor.isdigit() and fx<len(fcomp):
        factor+=(fcomp[fx])
        fx+=1
    if len(factor)>2:
        factor=str(factor)[1:len(factor)-1]
    elif len(factor)==2:
         factor=str(factor)[1:]
    return factor
def mass_sqlgetmass(name):
    st='select mass from elements where symbol="{}"'.format(name)
    try:
        cur.execute(st)
        data=cur.fetchone()
        return data[0]
    except Exception as e:
        print(e)
def evaluate(lst):
    global resultmass
    for x in range(0,len(lst)):
        if type(lst[x]) is list:
            evaluate(lst[x])
        elif type(lst[x]) is float or type(lst[x]) is int :
            resultmass+=lst[x]
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def compound_add(fcomp,mass):
    st='select * from compounds where name="{}"'.format(fcomp)
    try:
        cur.execute(st)
        tempdata=cur.fetchall()
        if len(tempdata)>0:
            st='update compounds set frequency=frequency+1 where name="{}"'.format(fcomp)
            cur.execute(st)
            con.commit()
        else:
            st='insert into compounds values {}'.format((fcomp,mass,1))
            cur.execute(st)
            con.commit()
            print('New compound encountered , added to list')
    except Exception as e:
        print(e)
def compound_main():
    compmain1=int(input('''
Please enter your input
1.View most searched compounds
2.Clear Table
'''))
    if compmain1==1:
        st='select name,mass from compounds order by frequency desc limit 10'
        try:
            cur.execute(st)
            tempdata=cur.fetchall()
            for tempvar in tempdata:
                print(tempvar[0],tempvar[1])
            if len(tempdata)==0:
                print('No data to show \U0001F615')
        except Exception as e:
            print(e)
    elif compmain1==2:
        pas=input('Enter Admin Password')
        if pas==adminpas:
            st='delete from compounds'
            cur.execute(st)
            print('Restoration Successful !')
###########################################################################################################################################    
def quiz():
    print('''
Welcome to the ELEMENTARY QUIZ !
Note - To provide answer with period in F block use f1 or f2 and for group in F block use f
     - Provide names and symbols in their proper form i.e first alphabet as capital  
''')
    quiz1=int(input('''
1. Start Quiz
2. View Leaderboard
3. Clear Leaderboard
'''))
    questionsasked=[]
    score=0
    if quiz1==1:
        while True:
            fieldlist1=['name','symbol','period','grp']
            fieldlist2=['name','symbol','atno']
            at=random.randint(1,119)
            index=[]
            index+=[random.randint(0,3)]
            while len(index)<2:
                temp=random.randint(0,2)
                if fieldlist2[temp]!=fieldlist1[index[0]]:
                    index+=[temp]
                if [fieldlist1[index[0]],fieldlist2[index[1]],at] in questionsasked:
                    at=random.randint(1,119)
                    index=[]
                    index+=[random.randint(0,3)]
            st1='select {} from elements where atno={}'.format(fieldlist1[index[0]],at)
            st2='select {} from elements where atno={}'.format(fieldlist2[index[1]],at)
            try:
                cur.execute(st1)
                answer=cur.fetchone()
                cur.execute(st2)
                question=cur.fetchone()
            except Exception as e:
                print(e)
            inputst="What is {} of the element with {} {} ".format(fieldlist1[index[0]],fieldlist2[index[1]],question[0])
            questionsasked+=[[fieldlist1[index[0]],fieldlist2[index[1]],at]]
            given=input(inputst)
            if given==str(answer[0]):
                print("Correct +1 point")
                score+=1
                print("Score is ",score)
                continue
            else:
                print("Incorrect :( Better luck next time")
                print("Correct answer was ",answer[0],"and you wrote ",given)
                userid=input('Enter ID to enter to Leaderboard')
                temptup=(userid,score)
                st1="insert into leaderboard values {}".format(temptup)
                try:
                    cur.execute(st1)
                    con.commit()
                    print('Score Added!')
                    viewleaderboard()
                except Exception as e:
                    print(e)
                break
    elif quiz1==2:
        viewleaderboard()
    elif quiz1==3:
        pas=input('Enter admin password')
        if pas==adminpas:
            try:
                cur.execute('delete from leaderboard')
                con.commit()
                print('Leaderboard Reset')
            except Exception as e:
                print(e)                        
def viewleaderboard():
    st2='select * from leaderboard order by score desc'
    cur.execute(st2)
    tempdata=cur.fetchall()
    if len(tempdata)==0:
        print('No data to show \U0001F615')
    else:
        for x in tempdata:
            print(x[0],x[1])
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def changepttable():  
    menu4=int(input(''' 
        Be a Scientist! Create your own perioidc table of elements
        1. Add an element
        2. Modify an element
        3. Remove an element
        4. Restore to original state
        '''))
    if menu4==1:
        add()
    if menu4==2:
        print(modify())
    if menu4==3:
        remove()
    if menu4==4:
        st='drop table elements' #drop table initialise new table
        cur.execute(st)
        con.commit()
        tablecreate('elements')
        print('Initialising ... ... ...')
        print(datatransfer())
        variables()
def add():
    at=int(input('Enter atomic number'))
    name=str(input('Enter name of element'))
    symbol=str(input('Enter Symbol of element'))
    mass=float(input('Enter mass'))
    period=str(input('Enter period'))
    grp=str(input('Enter group'))
    temp=(at,name,symbol,mass,period,grp)
    if [period,grp] not in pandg and at not in atnos and name not in names and symbol not in symbols:
        st='insert into elements values {}'.format(temp)
        try:
            cur.execute(st)
            con.commit()
            variables()
            print('Addition Complete ! \U0001F603')
        except Exception as e:
            print(e)
    else:
        print('An element already exists with these parameters in the periodic table!')
    
def modify():
    fieldlist=['atno','name','symbol','mass','period','grp']
    changefield=int(input('''
Enter the field you wish to change
1. Atomic Number
2. Name
3. Symbol
4. Mass
5. Period
6. Group
'''))
    newval=eval(input('''
Enter the new value for the field
In case you at changing name , symbol , period or group please enter value in form of 'xyz' '''))
    corfield=int(input('''
Enter the  corresponding field 
1. Atomic Number
2. Name
3. Symbol
4. Mass
5. Period
6. Group
'''))
    corval=eval(input('''
Enter the corresponding value for the field
In case you are changing name , symbol , period or group please enter value in form of 'xyz'
'''))
    st="update elements set {}='{}' where {}='{}'".format(str(fieldlist[changefield-1]),newval,str(fieldlist[corfield-1]),corval)
    try:
        cur.execute(st)
        con.commit()
        variables()
    except Exception as e:
        print(e)
    return 'Modification Successful \U0001F603	!'
def remove():
    fieldlist=['atno','name','symbol','mass','period','grp']
    field=int(input('''
Enter the field from where you wish to delete
1. Atomic Number
2. Name
3. Symbol
4. Mass
5. Period
6. Group
'''))
    val=eval(input('''
Enter the value you  wish to delete
In case you are changing name , symbol , period or group please enter value in form of 'xyz'
'''))
    st="delete from elements where {}='{}'".format(fieldlist[field-1],val)
    try:
        cur.execute(st)
        con.commit()
        variables()
    except Exception as e:
        print(e)
###########################################################################################################################################
def adminmenu():
    global adminpas
    pas=input('Enter Admin Password')
    if pas==adminpas:
        newpas=input("Enter new password")
        newpas1=input('Confirm your password')
        if newpas==newpas1:
            st='update admin set password="{}"'.format(newpas)
            try:
                cur.execute(st)
                con.commit()
                print('Password changed')
                variables()
            except Exception as e :
                print(e)
        else:
            print('Passwords don\'t match')
    else:
        print('Incorrect password')
        print(adminpas)
        menu()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
#main
cur.execute('show tables')
tables=cur.fetchall()
for tablevar in(('elements',),('leaderboard',),('compounds',),('admin',)):
    if tablevar not in tables:
        tablecreate(tablevar[0])
        if tablevar[0]=='admin':
            cur.execute('insert into admin values ("admin")')
        if tablevar[0]=='elements':
            datatransfer()
        if tablevar[0]=='leaderboard':
            cur.execute('insert into leaderboard values("Aditya",9001)')
intro()
variables()
menu()
