from fastapi import FastAPI,Response,Request
from fastapi.middleware.cors import CORSMiddleware
import json
from schema.sort_schema import Sort
from utils.validations import validate_arr_numbers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
# app.config["PREFERRED_URL_SCHEME"] = "https"



@app.post("/acomodar_numeros", tags = ["We Claims"])
def sort_numbers(sort:Sort,response:Response):
    sorted_array = sort.array
    sorted_array = sorted_array.split(",")

    name = sort.nombre

    print(sorted_array)

    valid_arr, new_sorted_array = validate_arr_numbers(sorted_array)

    if not valid_arr:
        response.status_code = 401
        data = {
            'message' : 'El arreglo de datos ingresado no es valido'
        }
        return data

    #validar_int = all([isinstance(item, int) for item in sorted_array])

    new_sorted_array.sort()
    item = {
        "Name": name,
        "sorted_array" : new_sorted_array,
        "min": new_sorted_array[0],
        "max": new_sorted_array[len(new_sorted_array)-1]
    }
    return item


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")
# def https_url_for(request: Request, name: str, **path_params: any) -> str:

#     http_url = request.url_for(name, **path_params)

#     # Replace 'http' with 'https'
#     return http_url.replace("http", "https", 1)

# templates.env.globals["https_url_for"] = https_url_for


@app.get("/we_company", response_class=HTMLResponse , tags = ["We Claims"])
async def read_item(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})