import pandas as pd 

class Transform: 

    def transform_json_dataFrame(self, data:dict): 
        self.data=pd.json_normalize(data); 
        return pd.json_normalize(self.data.iloc[0,0])
    
    def eliminarPrimerFila(self, data): 
        data.drop([0], axis=0,inplace=True)
        return data
    
    def transformFechas(self,data:pd.DataFrame)->pd.DataFrame: 
        data['FechaInicio']=''
        data['FechaTerminado']=''
        data['Asignacion']=''

        for i in range(1, len(data)): 
            data.loc[i,'FechaInicio']=data.loc[i, 'Inicio'].split("T")[0]
            data.loc[i,'FechaTerminado']=data.loc[i,'Terminado'].split("T")[0]
            data.loc[i,'Asignacion']=data.loc[i,'Fecha Asignación'].split("T")[0]
        return data 
    
    """Elimina las fechas"""
    def eliminarFechas(self,data:pd.DataFrame)->pd.DataFrame: 
        data.drop(['Inicio', 'Terminado','Fecha Asignación'], axis=1, inplace=True) 
        return data 
    
    """
    Cambia el formato de las fechas
    """
    def cambiarFormatoFechas(self,data:pd.DataFrame)->pd.DataFrame: 
        self.columnFecha=['FechaInicio','FechaTerminado', 'Asignacion']
        for j in self.columnFecha:
            
            for i in range(1, len(data)): 
                if (data.loc[i,j]!=''):
                    fecha=pd.to_datetime(data.loc[i,j])
                    data.loc[i,j]=fecha.strftime("%d/%m/%Y") 
                    data.loc[i,j]=pd.to_datetime(data.loc[i,j])
                else: 
                    data.loc[i,j]=''
        return data
    
    def ObtenerEstado(self, data)->pd.DataFrame: 
        return data['Estado'].unique(); 
    