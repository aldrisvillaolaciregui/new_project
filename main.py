from fastapi import FastAPI,Request, Form, File,UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

import pandas as pd 

import math #para validar si los campos de las columnas son nan


from database import database as conexion
from database import Usuario

from schemas import UserBasemodel


app =  FastAPI()


templates=Jinja2Templates(directory="templates")

app.mount("/static",StaticFiles(directory="static"),name="static")

@app.on_event("startup")
def startup():
    if conexion.is_closed():
        conexion.connect()
    print("conectado a la base de datos ") 
  
#login
@app.get("/")
async def login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})

    
@app.post("/")
async def login(request:Request, username:str=Form(...), password:str=Form(...)):
    users=UserBasemodel(username=username, password=password)
    
    print(users.username)
    cursor=conexion.cursor()
    query="SELECT password FROM usuario WHERE username=%s"
    values=(users.username,)
    cursor.execute(query,values)
    response=cursor.fetchone()  
    if ( response is None or users.password != response[0]):
        return templates.TemplateResponse("login.html", {"request":request, "message":"Error de credenciales"})
    respuesta=RedirectResponse(url="/dashboard")
    respuesta.set_cookie(key="user",value=username)
    return respuesta
    #fin login
    
    
    
    #dashboard

        
    
@app.get("/dashboard")
async def dashboard(request:Request):
    username=request.cookies.get("user")
    if not username:
        return RedirectResponse(url="/")
    cursor=conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM productos;")
    canti_product=cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM usuario")
    user=cursor.fetchone()
    print(user)
    return templates.TemplateResponse("dashboard.html",{"request":request , "cantidad":canti_product[0],"cantidad_user":user[0]})

@app.post("/dashboard")
async def dashboard(request:Request):
    username=request.cookies.get("user")
    if not username:
        return RedirectResponse(url="/")
    cursor=conexion.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM productos;")
    canti_product=cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM usuario")
    user=cursor.fetchone()
    print(user)
    return templates.TemplateResponse("dashboard.html",{"request":request, "cantidad":canti_product[0],"cantidad_user":user[0]})
        
    
    
    
@app.get("/productos")
async def productos(request:Request):
    return templates.TemplateResponse("products.html", {"request":request})

@app.post("/productos")
async def productos(request:Request,excel_file:UploadFile=File(...)):
    contents = await excel_file.read()
    df = pd.read_excel(contents)
    con=0
    for index,row in df.iterrows():
            columna1=row["Articulo"]
            columna2=row["Modelo"]
            columna3=row["Compañía"]
            columna4=row["Recibo"]
            columna5=row["Cliente"]
            columna6=row["Fecha"]
            columna7=row["Teléfono"]
            columna8=row["Desperfecto"]
            columna9=row["Entregado_con"]
            columna10=row["Reparación"]
            columna11=row["Comentarios"]
            columna12=row["Coste_total"]
            columna13=row["Cobrar_cliente"]
            columna14=row["Balance"]
            columna15=row["Trabajado"]
            columna16=row["Notificado"]
            columna17=row["Entregado"]
            columna18=row["Fecha_entrega"]
            if pd.isna(columna1) or columna1=="":
                columna1=None
            else:
                columna1=str(columna1)
            if pd.isna(columna2) or columna2=="":
                columna2=None
            else:
                columna2=str(columna2)
                
            if pd.isna(columna3) or columna3=="":
                columna3=None
            else:
                columna3=str(columna3)
                
            if pd.isna(columna4) or columna4=="":
                columna4=None
            else:
                columna4=str(columna4)
                
            if pd.isna(columna5) or columna5=="":
                columna5=None
            else:
                columna5=str(columna5)
                
            if pd.isna(columna6) or columna6=="":
                columna6=None
            else:
                columna6=str(columna6)
                
            if pd.isna(columna7) or columna7=="":
                columna7=None
            else:
                columna7=str(columna7)
                
            if pd.isna(columna8) or columna8=="":
                columna8=None
            else:
                columna8=str(columna8)
                
            if pd.isna(columna9) or columna9=="":
                columna9=None
            else:
                columna9=str(columna9)
                
            if pd.isna(columna10) or columna10=="":
                columna10=None
            else:
                columna10=str(columna10)
                
            if pd.isna(columna11) or columna11=="":
                columna11=None
            else:
                columna11=str(columna11)
                
            if pd.isna(columna12) or columna12=="":
                columna12=0
            else:
                columna12=int(columna12) 
                
            if pd.isna(columna13) or columna13=="":
                columna13=0
            else:
                columna13=int(columna13)
                
            if pd.isna(columna14) or columna14=="":
                columna14=0
            else:
                columna14=columna14
                
            if pd.isna(columna15) or columna15=="":
                columna15=None
            else:
                columna15=int(columna15)
                
            if pd.isna(columna16) or columna16=="":
                columna16=None
            else:
                columna16=str(columna16)
                
            if pd.isna(columna17) or columna17=="":
                columna17=None
            else:
                columna17=str(columna17)
                
            if pd.isna(columna18) or columna18=="":
                columna18=None
            else:
                columna18=str(columna18)
                
            
               
            
            
            cursor=conexion.cursor()
            query="INSERT INTO `articulos_empresa`(`articulos`, `modelo`, `compañia`, `recibo`, `cliente`, `fecha`, `telefono`, `desperfecto`, `entregaod_con`, `reparacion`, `comentarios`, `conste_total`, `cobro_cliente`, `balance`, `trabajado`, `notificado`, `entregado`, `fecha_entrega`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values=(columna1,columna2,columna3,columna4,columna5,columna6,columna7,columna8,columna9,columna10,columna11,columna12,columna13,columna14,columna15,columna16,columna17,columna18,)
            cursor.execute(query,values)
            conexion.commit()
            
            
   
          
      
    
          
    
    return templates.TemplateResponse("products.html", {"request":request})


@app.get("/users")
async def enviarusario(request:Request):
    username=request.cookies.get("user")
    return username

