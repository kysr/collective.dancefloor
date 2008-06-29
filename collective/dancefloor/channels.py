# -*- coding: utf-8 -*-
#
# File: .py
#
# Copyright (c) InQuant GmbH
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

__author__    = """Stefan Eletzhofer <stefan.eletzhofer@inquant.de>"""
__docformat__ = 'plaintext'
__revision__  = "$Revision$"
__version__   = '$Revision$'[11:-2]

import logging

from zope import component
from zope import interface

from collective.singing.interfaces import IChannelLookup

from collective.dancefloor.interfaces import IDanceFloor
from collective.dancefloor.interfaces import IDanceFloorParty

from Acquisition import aq_inner, aq_parent, aq_chain, Explicit
from persistent import Persistent

from OFS.SimpleItem import SimpleItem

info = logging.getLogger("collective.dancefloor.channels").info

class ILocalNewsletterLookup(interface.Interface):
    pass

class LocalNewsletterLookup(Explicit, SimpleItem):
    interface.implements(ILocalNewsletterLookup, IChannelLookup)

    def local_channels(self):
        parent = aq_parent(aq_inner(self))
        channels = parent.get("channels")
        if channels is not None:
            info("Returning local channels of ctx %s: %s" % (repr(parent), channels.keys()))
            return channels.values()
        return []

    def __call__(self):
        return self.local_channels()

    def __repr__(self):
        return "<LocalNewsletterLookup at %s>" % id(self)

# vim: set ft=python ts=4 sw=4 expandtab :