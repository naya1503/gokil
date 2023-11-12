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


class AcceptTermsOfService(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``EE72F79A``

    Parameters:
        id (:obj:`DataJSON <gokil.raw.base.DataJSON>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["id"]

    ID = 0xee72f79a
    QUALNAME = "functions.help.AcceptTermsOfService"

    def __init__(self, *, id: "raw.base.DataJSON") -> None:
        self.id = id  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AcceptTermsOfService":
        # No flags
        
        id = TLObject.read(b)
        
        return AcceptTermsOfService(id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        return b.getvalue()