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


class UpdateChatParticipantDelete(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~gokil.raw.base.Update`.

    Details:
        - Layer: ``158``
        - ID: ``E32F3D77``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        version (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["chat_id", "user_id", "version"]

    ID = 0xe32f3d77
    QUALNAME = "types.UpdateChatParticipantDelete"

    def __init__(self, *, chat_id: int, user_id: int, version: int) -> None:
        self.chat_id = chat_id  # long
        self.user_id = user_id  # long
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChatParticipantDelete":
        # No flags
        
        chat_id = Long.read(b)
        
        user_id = Long.read(b)
        
        version = Int.read(b)
        
        return UpdateChatParticipantDelete(chat_id=chat_id, user_id=user_id, version=version)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.version))
        
        return b.getvalue()
