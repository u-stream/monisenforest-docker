from typing import Optional

from pydantic import BaseModel


class LitterEachBase(BaseModel):
    year: float
    t1: str
    t2: str
    inst_period: float
    wdry_leaf: Optional[float]
    wdry_branch: Optional[float]
    wdry_rep: Optional[float]
    wdry_all: Optional[float]
    datafile_id: int


class LitterEachCreate(LitterEachBase):
    pass


class LitterEach(LitterEachBase):
    id: int

    class Config:
        orm_mode = True
