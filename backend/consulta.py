import pandas as pd 

class Consulta: 

    def FiltroPorEstado(self, data:pd.DataFrame, option:str)->pd.DataFrame: 
        if option not in ["Terminado","En Proceso","Sin asignar","No Iniciado"]: 
            return data 
        
        return data[data['Estado']==option]
    
    def CantidadTareasCompletadas(self,data:pd.DataFrame)->int:
        self.Terminado=data[data['Estado']=='Terminado']
        return len(self.Terminado)