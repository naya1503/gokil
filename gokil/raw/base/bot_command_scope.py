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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from gokil import raw
from gokil.raw.core import TLObject

BotCommandScope = Union[raw.types.BotCommandScopeChatAdmins, raw.types.BotCommandScopeChats, raw.types.BotCommandScopeDefault, raw.types.BotCommandScopePeer, raw.types.BotCommandScopePeerAdmins, raw.types.BotCommandScopePeerUser, raw.types.BotCommandScopeUsers]


# noinspection PyRedeclaration
class BotCommandScope:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: gokil.raw.types

        .. autosummary::
            :nosignatures:

            BotCommandScopeChatAdmins
            BotCommandScopeChats
            BotCommandScopeDefault
            BotCommandScopePeer
            BotCommandScopePeerAdmins
            BotCommandScopePeerUser
            BotCommandScopeUsers
    """

    QUALNAME = "gokil.raw.base.BotCommandScope"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.gokil.org/telegram/base/bot-command-scope")
