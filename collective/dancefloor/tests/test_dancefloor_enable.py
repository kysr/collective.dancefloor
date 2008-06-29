import unittest

from zope import interface

from zope.app.component.interfaces import ISite

from collective.dancefloor.tests.base import DanceFloorTestCase
from collective.dancefloor.interfaces import *

from collective.dancefloor.handlers import dancefloor_changed

from Products.ATContentTypes.content.folder import ATFolder

class TestDancefloorEnabled(DanceFloorTestCase):
    """ Test enable/disable dancefloor
    """

    def afterSetUp(self):
        _ = self.folder.invokeFactory("Folder", "dancefloor")
        self.dancefloor = self.folder.get(_)

    def test_interface_default_disabled(self):
        self.assertEqual(IDanceFloorParty.providedBy(self.dancefloor), False, "default interface is enabled!")

    def test_stuff_not_there_if_new(self):
        df = ATFolder("dancefloor")
        self.failUnless("channels" not in df.keys())
        self.failUnless("collectors" not in df.keys())

    def test_event_adds_channels(self):
        dancefloor_changed(self.dancefloor, None)
        self.failUnless("channels" not in self.dancefloor.keys(), "channels not created even inf no local party")

        interface.alsoProvides(self.dancefloor, IDanceFloorParty)
        dancefloor_changed(self.dancefloor, None)
        self.failUnless("channels" in self.dancefloor.keys(), "channels not created")

    def test_local_utility(self):
        dancefloor = self.dancefloor
        interface.alsoProvides(dancefloor, IDanceFloorParty)
        dancefloor_changed(self.dancefloor, None)
        self.failUnless(ISite.providedBy(dancefloor))




def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDancefloorEnabled))
    return suite

# vim: set ft=python ts=4 sw=4 expandtab :