#! /usr/bin/python

import struct
import xml.dom.minidom
from lmcp import LMCPObject

## ===============================================================================
## Authors: AFRL/RQQA
## Organization: Air Force Research Laboratory, Aerospace Systems Directorate, Power and Control Division
## 
## Copyright (c) 2017 Government of the United State of America, as represented by
## the Secretary of the Air Force.  No copyright is claimed in the United States under
## Title 17, U.S. Code.  All Other Rights Reserved.
## ===============================================================================

## This file was auto-created by LmcpGen. Modifications will be overwritten.

from afrl.cmasi import EntityConfiguration
from afrl.cmasi import EntityState
from afrl.cmasi import MissionCommand
from afrl.impact import AreaOfInterest
from afrl.impact import LineOfInterest
from afrl.impact import PointOfInterest


class CreateNewService(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 3
        self.SERIES_NAME = "UXNATIVE"
        self.FULL_LMCP_TYPE_NAME = "uxas.messages.uxnative.CreateNewService"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149751333668345413
        self.SERIES_VERSION = 3

        #Define message fields
        self.ServiceID = 0   #int64
        self.XmlConfiguration = ""   #string
        self.EntityConfigurations = []   #EntityConfiguration
        self.EntityStates = []   #EntityState
        self.MissionCommands = []   #MissionCommand
        self.Areas = []   #AreaOfInterest
        self.Lines = []   #LineOfInterest
        self.Points = []   #PointOfInterest


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = []
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.append(struct.pack(">q", self.ServiceID))
        buffer.append(struct.pack(">H", len(self.XmlConfiguration) ))
        if len(self.XmlConfiguration) > 0:
            buffer.append(struct.pack( `len(self.XmlConfiguration)` + "s", str(self.XmlConfiguration)))
        buffer.append(struct.pack(">H", len(self.EntityConfigurations) ))
        for x in self.EntityConfigurations:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">H", len(self.EntityStates) ))
        for x in self.EntityStates:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">H", len(self.MissionCommands) ))
        for x in self.MissionCommands:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">H", len(self.Areas) ))
        for x in self.Areas:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">H", len(self.Lines) ))
        for x in self.Lines:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())
        buffer.append(struct.pack(">H", len(self.Points) ))
        for x in self.Points:
           buffer.append(struct.pack("B", x != None ))
           if x != None:
               buffer.append(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.append(struct.pack(">I", x.LMCP_TYPE))
               buffer.append(struct.pack(">H", x.SERIES_VERSION))
               buffer.append(x.pack())

        return "".join(buffer)

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a string buffer and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.ServiceID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _strlen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        if _strlen > 0:
            self.XmlConfiguration = struct.unpack_from( `_strlen` + "s", buffer, _pos )[0]
            _pos += _strlen
        else:
             self.XmlConfiguration = ""
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.EntityConfigurations = [None] * _arraylen
        _pos += 2
        for x in range(_arraylen):
            _valid = struct.unpack_from("B", buffer, _pos )[0]
            _pos += 1
            if _valid:
                _series = struct.unpack_from(">q", buffer, _pos)[0]
                _pos += 8
                _type = struct.unpack_from(">I", buffer, _pos)[0]
                _pos += 4
                _version = struct.unpack_from(">H", buffer, _pos)[0]
                _pos += 2
                from lmcp import LMCPFactory
                self.EntityConfigurations[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.EntityConfigurations[x].unpack(buffer, _pos)
            else:
                self.EntityConfigurations[x] = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.EntityStates = [None] * _arraylen
        _pos += 2
        for x in range(_arraylen):
            _valid = struct.unpack_from("B", buffer, _pos )[0]
            _pos += 1
            if _valid:
                _series = struct.unpack_from(">q", buffer, _pos)[0]
                _pos += 8
                _type = struct.unpack_from(">I", buffer, _pos)[0]
                _pos += 4
                _version = struct.unpack_from(">H", buffer, _pos)[0]
                _pos += 2
                from lmcp import LMCPFactory
                self.EntityStates[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.EntityStates[x].unpack(buffer, _pos)
            else:
                self.EntityStates[x] = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.MissionCommands = [None] * _arraylen
        _pos += 2
        for x in range(_arraylen):
            _valid = struct.unpack_from("B", buffer, _pos )[0]
            _pos += 1
            if _valid:
                _series = struct.unpack_from(">q", buffer, _pos)[0]
                _pos += 8
                _type = struct.unpack_from(">I", buffer, _pos)[0]
                _pos += 4
                _version = struct.unpack_from(">H", buffer, _pos)[0]
                _pos += 2
                from lmcp import LMCPFactory
                self.MissionCommands[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.MissionCommands[x].unpack(buffer, _pos)
            else:
                self.MissionCommands[x] = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.Areas = [None] * _arraylen
        _pos += 2
        for x in range(_arraylen):
            _valid = struct.unpack_from("B", buffer, _pos )[0]
            _pos += 1
            if _valid:
                _series = struct.unpack_from(">q", buffer, _pos)[0]
                _pos += 8
                _type = struct.unpack_from(">I", buffer, _pos)[0]
                _pos += 4
                _version = struct.unpack_from(">H", buffer, _pos)[0]
                _pos += 2
                from lmcp import LMCPFactory
                self.Areas[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.Areas[x].unpack(buffer, _pos)
            else:
                self.Areas[x] = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.Lines = [None] * _arraylen
        _pos += 2
        for x in range(_arraylen):
            _valid = struct.unpack_from("B", buffer, _pos )[0]
            _pos += 1
            if _valid:
                _series = struct.unpack_from(">q", buffer, _pos)[0]
                _pos += 8
                _type = struct.unpack_from(">I", buffer, _pos)[0]
                _pos += 4
                _version = struct.unpack_from(">H", buffer, _pos)[0]
                _pos += 2
                from lmcp import LMCPFactory
                self.Lines[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.Lines[x].unpack(buffer, _pos)
            else:
                self.Lines[x] = None
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        self.Points = [None] * _arraylen
        _pos += 2
        for x in range(_arraylen):
            _valid = struct.unpack_from("B", buffer, _pos )[0]
            _pos += 1
            if _valid:
                _series = struct.unpack_from(">q", buffer, _pos)[0]
                _pos += 8
                _type = struct.unpack_from(">I", buffer, _pos)[0]
                _pos += 4
                _version = struct.unpack_from(">H", buffer, _pos)[0]
                _pos += 2
                from lmcp import LMCPFactory
                self.Points[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.Points[x].unpack(buffer, _pos)
            else:
                self.Points[x] = None
        return _pos


    def unpackFromXMLNode(self, el, seriesFactory):
        LMCPObject.LMCPObject.unpackFromXMLNode(self, el, seriesFactory)
        for e in el.childNodes:
            if e.nodeType == xml.dom.Node.ELEMENT_NODE:
                if e.localName == "ServiceID" and len(e.childNodes) > 0 :
                    self.ServiceID = int(e.childNodes[0].nodeValue)
                elif e.localName == "XmlConfiguration" and len(e.childNodes) > 0 :
                    self.XmlConfiguration = str(e.childNodes[0].nodeValue)
                elif e.localName == "EntityConfigurations" and len(e.childNodes) > 0 :
                    self.EntityConfigurations = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            obj = seriesFactory.createObjectByName(c.getAttribute('Series'), c.localName)
                            if obj != None:
                                obj.unpackFromXMLNode(c, seriesFactory)
                                self.EntityConfigurations.append(obj)
                elif e.localName == "EntityStates" and len(e.childNodes) > 0 :
                    self.EntityStates = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            obj = seriesFactory.createObjectByName(c.getAttribute('Series'), c.localName)
                            if obj != None:
                                obj.unpackFromXMLNode(c, seriesFactory)
                                self.EntityStates.append(obj)
                elif e.localName == "MissionCommands" and len(e.childNodes) > 0 :
                    self.MissionCommands = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            obj = seriesFactory.createObjectByName(c.getAttribute('Series'), c.localName)
                            if obj != None:
                                obj.unpackFromXMLNode(c, seriesFactory)
                                self.MissionCommands.append(obj)
                elif e.localName == "Areas" and len(e.childNodes) > 0 :
                    self.Areas = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            obj = seriesFactory.createObjectByName(c.getAttribute('Series'), c.localName)
                            if obj != None:
                                obj.unpackFromXMLNode(c, seriesFactory)
                                self.Areas.append(obj)
                elif e.localName == "Lines" and len(e.childNodes) > 0 :
                    self.Lines = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            obj = seriesFactory.createObjectByName(c.getAttribute('Series'), c.localName)
                            if obj != None:
                                obj.unpackFromXMLNode(c, seriesFactory)
                                self.Lines.append(obj)
                elif e.localName == "Points" and len(e.childNodes) > 0 :
                    self.Points = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            obj = seriesFactory.createObjectByName(c.getAttribute('Series'), c.localName)
                            if obj != None:
                                obj.unpackFromXMLNode(c, seriesFactory)
                                self.Points.append(obj)

        return

    def unpackFromDict(self, d, seriesFactory):
        LMCPObject.LMCPObject.unpackFromDict(self, d, seriesFactory)
        for key in d:
            if key == "ServiceID":
                self.ServiceID = d[key]
            elif key == "XmlConfiguration":
                self.XmlConfiguration = d[key]
            elif key == "EntityConfigurations":
                self.EntityConfigurations = []
                for c in d[key]:
                    obj = seriesFactory.unpackFromDict(c)
                    if obj != None:
                        self.EntityConfigurations.append(obj)
            elif key == "EntityStates":
                self.EntityStates = []
                for c in d[key]:
                    obj = seriesFactory.unpackFromDict(c)
                    if obj != None:
                        self.EntityStates.append(obj)
            elif key == "MissionCommands":
                self.MissionCommands = []
                for c in d[key]:
                    obj = seriesFactory.unpackFromDict(c)
                    if obj != None:
                        self.MissionCommands.append(obj)
            elif key == "Areas":
                self.Areas = []
                for c in d[key]:
                    obj = seriesFactory.unpackFromDict(c)
                    if obj != None:
                        self.Areas.append(obj)
            elif key == "Lines":
                self.Lines = []
                for c in d[key]:
                    obj = seriesFactory.unpackFromDict(c)
                    if obj != None:
                        self.Lines.append(obj)
            elif key == "Points":
                self.Points = []
                for c in d[key]:
                    obj = seriesFactory.unpackFromDict(c)
                    if obj != None:
                        self.Points.append(obj)

        return

    def get_ServiceID(self):
        return self.ServiceID

    def set_ServiceID(self, value):
        self.ServiceID = int( value )

    def get_XmlConfiguration(self):
        return self.XmlConfiguration

    def set_XmlConfiguration(self, value):
        self.XmlConfiguration = str( value )

    def get_EntityConfigurations(self):
        return self.EntityConfigurations

    def get_EntityStates(self):
        return self.EntityStates

    def get_MissionCommands(self):
        return self.MissionCommands

    def get_Areas(self):
        return self.Areas

    def get_Lines(self):
        return self.Lines

    def get_Points(self):
        return self.Points



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From CreateNewService:\n"
        buf +=    "ServiceID = " + str( self.ServiceID ) + "\n" 
        buf +=    "XmlConfiguration = " + str( self.XmlConfiguration ) + "\n" 
        buf +=    "EntityConfigurations = " + str( self.EntityConfigurations ) + "\n" 
        buf +=    "EntityStates = " + str( self.EntityStates ) + "\n" 
        buf +=    "MissionCommands = " + str( self.MissionCommands ) + "\n" 
        buf +=    "Areas = " + str( self.Areas ) + "\n" 
        buf +=    "Lines = " + str( self.Lines ) + "\n" 
        buf +=    "Points = " + str( self.Points ) + "\n" 

        return buf;

    def toDict(self):
        m = {}
        self.toDictMembers(m)
        d = {}
        if ("UXNATIVE" is None) or ("UXNATIVE" is ""): # this should never happen
            # need to fill this with error message
            d["datatype"] = str("DEBUG_PROBLEM_HERE" + "/CreateNewService")
            d["datastring"] = str(m)
        else:
            d['datatype'] = str("UXNATIVE" + "/CreateNewService")
            d['datastring'] = str(m)
        return d

    def toDictMembers(self, d):
        LMCPObject.LMCPObject.toDictMembers(self, d)
        d['ServiceID'] = self.ServiceID
        d['XmlConfiguration'] = self.XmlConfiguration
        d['EntityConfigurations'] = []
        for x in self.EntityConfigurations:
            if x == None:
                d['EntityConfigurations'].append(None)
            else:
                d['EntityConfigurations'].append(x.toDict())
        d['EntityStates'] = []
        for x in self.EntityStates:
            if x == None:
                d['EntityStates'].append(None)
            else:
                d['EntityStates'].append(x.toDict())
        d['MissionCommands'] = []
        for x in self.MissionCommands:
            if x == None:
                d['MissionCommands'].append(None)
            else:
                d['MissionCommands'].append(x.toDict())
        d['Areas'] = []
        for x in self.Areas:
            if x == None:
                d['Areas'].append(None)
            else:
                d['Areas'].append(x.toDict())
        d['Lines'] = []
        for x in self.Lines:
            if x == None:
                d['Lines'].append(None)
            else:
                d['Lines'].append(x.toDict())
        d['Points'] = []
        for x in self.Points:
            if x == None:
                d['Points'].append(None)
            else:
                d['Points'].append(x.toDict())

        return

    def getLMCPType(self):
        return self.LMCP_TYPE

    def getSeriesName(self):
        return self.SERIES_NAME

    def getSeriesNameID(self):
        return self.SERIES_NAME_ID

    def getSeriesVersion(self):
        return self.SERIES_VERSION

    def toXMLStr(self, ws):
        str = ws + '<CreateNewService Series="UXNATIVE" >\n';
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</CreateNewService>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<ServiceID>" + str(self.ServiceID) + "</ServiceID>\n"
        buf += ws + "<XmlConfiguration>" + str(self.XmlConfiguration) + "</XmlConfiguration>\n"
        buf += ws + "<EntityConfigurations>\n"
        for x in self.EntityConfigurations:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</EntityConfigurations>\n"
        buf += ws + "<EntityStates>\n"
        for x in self.EntityStates:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</EntityStates>\n"
        buf += ws + "<MissionCommands>\n"
        for x in self.MissionCommands:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</MissionCommands>\n"
        buf += ws + "<Areas>\n"
        for x in self.Areas:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</Areas>\n"
        buf += ws + "<Lines>\n"
        for x in self.Lines:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</Lines>\n"
        buf += ws + "<Points>\n"
        for x in self.Points:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</Points>\n"

        return buf
        
