#!/usr/bin/python
#!/usr/bin/python
import string

#kilku autorow
my_string="@article{kornuta2015robot,\n  title={Robot control system design exemplified by multi-camera visual servoing},\n  author={Kornuta, Tomasz and Zieli{\\'n}ski, Cezary and Roman, Dmowski and Michail, Gorbaczow and Hahimoto, Hygens},\n  journal={Journal of Intelligent \\& Robotic Systems},\n  volume={77},\n  number={3-4},\n  pages={499--523},\n  year={2015},\n  publisher={Springer}\n}\n"
#jeden autor
my_string2="@article{kornuta2015robot,\n  title={Robot control system design exemplified by multi-camera visual servoing},\n  author={Roman, Dmowski},\n  journal={Journal of Intelligent \\& Robotic Systems},\n  volume={77},\n  number={3-4},\n  pages={499--523},\n  year={2015},\n  publisher={Springer}\n}\n"

a= (my_string.split("author={",1)[1] )  #początek od autorow
b= (a.split("},\n  journal",1)[0] )     #koniec zaostatnim autorem

list=[b]

autors = []
i=-1
if " and "  in (list [0]) :  #  sprawdza czy wielu autorów
  
    while " and "  in (list [i+1]) : #jesli wielu to dodawaj kolejno do listy autorów
    
        list.append(list [i+1].split(" and ",1) [1] ) #dodaj reszte autorów do listy
        c = (list [i+1].split(" and ",1) [0] )          #pierwszy autor  z listy list
        autors.append(c)                                #dodaj pierwszego autora z listy list do listy autorów
        i=i+1
    
    autors.append(list[i].split(" and ",1)[1] )     #jesli na liscie jest juz tylko jeden autor to dodaj go do list autorow
else :          #jesli tylko jeden autor
    autors.append(b)

print (autors)
print (len(autors))
