#Importing functions

from IPython.display import clear_output
import random


uncommon_letters="zZqQxXyYgGwWjJvVfFdD"
number=0


#Dictionaries for single player

hindi=["dangal","bahubali","krish","sholay","zanjeer","badlekiaag","naagin","shershah","amar","amrit","angoor","holiday","raone","ravan","tehelka","tehekhana","barsaat","shahid","uri","udaan","lagaan","mehbooba","lakshya","baby","haider","pyaasa","bluffmaster","players","queen","guru","sarkaar","bombay","pk","piku","kahaani","raazi","devdas","awednesday","airlift","andhaadhun","swades","moti","barfi","omkara","sonchiriya","deewar","maqbool","ardhsatya","pushpak","herapheri","welcome","parmanu","ahsaan","padman","don","insaan","jeewan","sanju","nadiyakepaar","halfticket"]
english=["transformers","avengers","ironman","captainamerica","nowyouseeme","lightsout","conjuring","anabelle","hulk","thenun","thor","avatar","titanic","themummy","themummyreturns","missionimpossible","insurgent","divergent","thehobbit","matrix","kungfupanda","joker","batman","superman","flash","wonderwoman","bourneidentitiy","startrek","starwars","interstellar","wolverine","xmen","up","jumanji","johnwick","venom","deadpool","coco","brave","harrypotter","mugentrain","thecore","bohemianrhapsody","inception","martian","kungfuhustle","hungergames","logan"]


#While loop for playing again

p=1
while p==1:
 gamemode=int(input("Select gamemode (Single{1},Double{2}): "))

 if gamemode==2 :
  m=input("Enter movie name: ")
  m=m.lower()
  while m.isalpha()==False:
    print("Only letters allowed")
    m=input("Enter movie name: ")


#Entering Language

 lang=input("Enter language of the movie(H/E)")

 if lang in "hH":
   B="BOLLYWOOD"

   if gamemode==1:
     m=random.choice(hindi)
   clear_output()

 elif lang in "eE":
   B="HOLLYWOOD"

   if gamemode==1:
     m=random.choice(english)
   clear_output()


#Setting difficulty

 D=input("Choose difficulty level(e/m/h): ")
 if D in "Ee":
   l=0

   for op in m:
    if op in uncommon_letters:
      number+=1

 elif D in "Mm":
  l=3
 elif D in "hH":
  l=5
 else:
   l=3

#Printing number of uncommon letters for easy difficulty

 if D in "eE":
   print("Uncommon letters: ",number)

 S=[]


#Changing the movie name into "_"

 for j in range(len(m)):
   S.append("_ ")


#Replacing _s with vowels

 for i in range(len(m)):

   if m[i] in "aeiou":
     S[i]=m[i]

 print(B)

 for k in S:
   print(k,end=" ")


#Loop which takes guesses till lives are over

 while l<10:
   print()
   g=input("Guessed letter: ")

   if g in ("a","e","i","o","u"):
     l+=1
     print("Punishment for using vowels, -1 life. Lives left: ",10-l)
     print(B[l:])

   elif g not in m:
     l+=1
     print(B[l:])
     print("You lost a life")
     print("Lives left: ",10-l)


   for h in range(len(m)):

     if m[h]==g:
       S[h]=g

   for k in S:
    print(k,end=" ")

   if "_ " not in S:

     print()
     print("You win, pog")
     Q=input("Play again(Y/N): ")
     clear_output()

     if Q in"nN":
       p=0
       break

   elif l==10:

     print()
     print("You lose, rip. The movie was: ",m)
     Q=input("Play again(Y/N): ")
     clear_output()
     if Q in "nN":
       p=0
     break

   if len(g)>1 and g==m:

     print()
     print("You win, pog")
     Q=input("Play again(Y/N): ")
     clear_output()
     if Q in "nN":
       p=0
     break

   elif len(g)>1 and g!=m:

     print()
     print("You lose, rip. The movie was: ",m)
     Q=input("Play again(Y/N): ")
     clear_output()
     if Q in "nN":
       p=0
     break

#Over and out

