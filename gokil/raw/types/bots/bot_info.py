#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from gokil.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from gokil.raw.core import TLObject
from gokil import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class BotInfo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~gokil.raw.base.bots.BotInfo`.

    Details:
        - Layer: ``158``
        - ID: ``E8A775B0``

    Parameters:
        name (``str``):
            N/A

        about (``str``):
            N/A

        description (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: gokil.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetBotInfo
    """

    __slots__: List[str] = ["name", "about", "description"]

    ID = 0xe8a775b0
    QUALNAME = "types.bots.BotInfo"

    def __init__(self, *, name: str, about: str, description: str) -> None:
        self.name = name  # string
        self.about = about  # string
        self.description = description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInfo":
        # No flags
        
        name = String.read(b)
        
        about = String.read(b)
        
        description = String.read(b)
        
        return BotInfo(name=name, about=about, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.name))
        
        b.write(String(self.about))
        
        b.write(String(self.description))
        
        return b.getvalue()
