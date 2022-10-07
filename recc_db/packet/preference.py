# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import List

from recc_db.packet.plugin import PluginA


@dataclass
class PreferenceA:
    oem: str
    plugins: List[PluginA]
