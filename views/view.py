from pickle import LIST
from models.LinkedList import LinkedList

def main():
    
    lista_ligada = LinkedList()
    try:
        while True:
            userinput = input().split(" ")
            if userinput[0] == "RPI":
                lista_ligada.insert_at_start(userinput[1])
                lista_ligada.traverse_list()
            
            elif userinput[0] == "RPF":
                lista_ligada.insert_at_end(userinput[1])
                lista_ligada.traverse_list()
            
            elif userinput[0] == "RPDE":
                lista_ligada.insert_after_item(userinput[1], userinput[2])
                lista_ligada.traverse_list()
                
            elif userinput[0] == "RPAE":
                lista_ligada.insert_before_item(userinput[1], userinput[2])
                lista_ligada.traverse_list()
            
            elif userinput[0] == "RPII":
                lista_ligada.insert_at_index(int(userinput[1]), userinput[2])
                lista_ligada.traverse_list()
                
            elif userinput[0] == "VNE":
                print(f"O número de elementos são {lista_ligada.get_count()}.")
                
            elif userinput[0] == "VP":
                if (lista_ligada.search_item(userinput[1])):
                    print(f"O país {userinput[1]} encontra-se na lista.")
                else:
                    print(f"O país {userinput[1]} não se encontra na lista.")
            
            elif userinput[0] == "EPE":
                print(f"O país {lista_ligada.start_node.get_item()} foi eliminado da lista.")
                lista_ligada.delete_at_start()
                
            elif userinput[0] == "EUE":
                print(f"O país {lista_ligada.get_last_node()} foi eliminado da lista.")
                lista_ligada.delete_at_end()
             
            elif userinput[0] == "EP":
                if(lista_ligada.delete_element_by_value(userinput[1])):
                    print(f"O país {userinput[1]} foi eliminado da lista.")
                else:
                    print(f"O país {userinput[1]}  não se encontra na lista.")


                 
            
                    
            
                
    except EOFError:
        return  
    