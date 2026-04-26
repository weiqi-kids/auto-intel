"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .3m import 3mFetcher
from .aptiv import AptivFetcher
from .arcelormittal import ArcelormittalFetcher
from .bridgestone import BridgestoneFetcher
from .byd import BydFetcher
from .cheng_shin import ChengShinFetcher
from .continental import ContinentalFetcher
from .denso import DensoFetcher
from .ford import FordFetcher
from .fuyao import FuyaoFetcher
from .gm import GmFetcher
from .honda import HondaFetcher
from .hota import HotaFetcher
from .hotai import HotaiFetcher
from .hyundai import HyundaiFetcher
from .hyundai_mobis import HyundaiMobisFetcher
from .kenda import KendaFetcher
from .magna import MagnaFetcher
from .nippon_steel import NipponSteelFetcher
from .posco import PoscoFetcher
from .saint_gobain import SaintGobainFetcher
from .stellantis import StellantisFetcher
from .tesla import TeslaFetcher
from .toyota import ToyotaFetcher
from .tyc import TycFetcher
from .valeo import ValeoFetcher
from .volkswagen import VolkswagenFetcher
from .yulon import YulonFetcher

FETCHERS = {
    "3m": 3mFetcher,
    "aptiv": AptivFetcher,
    "arcelormittal": ArcelormittalFetcher,
    "bridgestone": BridgestoneFetcher,
    "byd": BydFetcher,
    "cheng_shin": ChengShinFetcher,
    "continental": ContinentalFetcher,
    "denso": DensoFetcher,
    "ford": FordFetcher,
    "fuyao": FuyaoFetcher,
    "gm": GmFetcher,
    "honda": HondaFetcher,
    "hota": HotaFetcher,
    "hotai": HotaiFetcher,
    "hyundai": HyundaiFetcher,
    "hyundai_mobis": HyundaiMobisFetcher,
    "kenda": KendaFetcher,
    "magna": MagnaFetcher,
    "nippon_steel": NipponSteelFetcher,
    "posco": PoscoFetcher,
    "saint_gobain": SaintGobainFetcher,
    "stellantis": StellantisFetcher,
    "tesla": TeslaFetcher,
    "toyota": ToyotaFetcher,
    "tyc": TycFetcher,
    "valeo": ValeoFetcher,
    "volkswagen": VolkswagenFetcher,
    "yulon": YulonFetcher,
}
