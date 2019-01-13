#!/usr/bin/python
#!/usr/bin/python
import string

def deleteSigns(word):  #replace polish signs
    
    bb= word.replace("{\\'", " ")
    cc=bb.replace("}", " ")     
    dd=cc.split(' ')
    k=0
    out=[" "]
    while k<len(dd):
        out[0]=out[0]+dd[k]
        k=k+1
    without_special_sign = out[0].split(" ",1)[1] 
    return without_special_sign

def GiveAuthors(my_string):
#several authors example
#my_string="@article{kornuta2015robot,\n  title={Robot control system design exemplified by multi-camera visual servoing},\n  author={Kornuta, Tomasz and Zieli{\\'n}ski, Cezary and Roman, Dmowski and Michail, Gorbaczow and Hahimoto, Hygens},\n  journal={Journal of Intelligent \\& Robotic Systems},\n  volume={77},\n  number={3-4},\n  pages={499--523},\n  year={2015},\n  publisher={Springer}\n}\n"
#only one author example
#my_string2="@article{kornuta2015robot,\n  title={Robot control system design exemplified by multi-camera visual servoing},\n  author={Roman, Dmowski},\n  journal={Journal of Intelligent \\& Robotic Systems},\n  volume={77},\n  number={3-4},\n  pages={499--523},\n  year={2015},\n  publisher={Springer}\n}\n"

    a= (my_string.split("author={",1)[1] )  #begin - first author
    b= (a.split("},\n  journal",1)[0] )     #end - last author

    list=[b]

    authors = []
    i=-1
    if " and "  in (list [0]) :  #  if there is several authors
  
        while " and "  in (list [i+1]) : #add them to the list of authors
    
            list.append(list [i+1].split(" and ",1) [1] ) #add the rest authors to the list
            c = (list [i+1].split(" and ",1) [0] )          #first author from the list
            authors.append(c)                                #add first author from the list to the list of the authors
            i=i+1
    
        authors.append(list[i].split(" and ",1)[1] )     #if there is only one author on the list, add him to the list of the authors
    else :          #if there is only one author
        authors.append(b)


    j=0
    while j<len(authors) :    #replace polish signs
        if "{\\"  in authors[j]:
            authors[j] = deleteSigns(authors[j])
        j=j+1
    
    return authors
        


