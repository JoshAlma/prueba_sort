from typing import Optional

from pydantic import BaseModel, Field

class Sort(BaseModel):
    nombre: Optional[str] = Field(
        title="Nombre"
    )
    array: Optional[str] = Field(
        title="Array"
    )
