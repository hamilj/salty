#! /usr/bin/python

import sys, struct
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

from afrl.cmasi import Waypoint
from afrl.cmasi import WaypointTransferMode


class WaypointTransfer(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 59
        self.SERIES_NAME = "CMASI"
        self.FULL_LMCP_TYPE_NAME = "afrl.cmasi.WaypointTransfer"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 3

        #Define message fields
        self.EntityID = 0   #int64
        self.Waypoints = []   #Waypoint
        self.TransferMode = WaypointTransferMode.WaypointTransferMode.AddWaypoints   #WaypointTransferMode


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = bytearray()
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.extend(struct.pack(">q", self.EntityID))
        buffer.extend(struct.pack(">H", len(self.Waypoints) ))
        for x in self.Waypoints:
           buffer.extend(struct.pack("B", x != None ))
           if x != None:
               buffer.extend(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.extend(struct.pack(">I", x.LMCP_TYPE))
               buffer.extend(struct.pack(">H", x.SERIES_VERSION))
               buffer.extend(x.pack())
        buffer.extend(struct.pack(">i", self.TransferMode))

        return buffer

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a bytearray and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.EntityID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        self.Waypoints = [None] * _arraylen
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
                self.Waypoints[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.Waypoints[x].unpack(buffer, _pos)
            else:
                self.Waypoints[x] = None
        self.TransferMode = struct.unpack_from(">i", buffer, _pos)[0]
        _pos += 4
        return _pos


    def unpackFromXMLNode(self, el, seriesFactory):
        LMCPObject.LMCPObject.unpackFromXMLNode(self, el, seriesFactory)
        for e in el.childNodes:
            if e.nodeType == xml.dom.Node.ELEMENT_NODE:
                if e.localName == "EntityID" and len(e.childNodes) > 0 :
                    self.EntityID = int(e.childNodes[0].nodeValue)
                elif e.localName == "Waypoints" and len(e.childNodes) > 0 :
                    self.Waypoints = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            obj = seriesFactory.createObjectByName(c.getAttribute('Series'), c.localName)
                            if obj != None:
                                obj.unpackFromXMLNode(c, seriesFactory)
                                self.Waypoints.append(obj)
                elif e.localName == "TransferMode" and len(e.childNodes) > 0 :
                    self.TransferMode = WaypointTransferMode.get_WaypointTransferMode_str(e.childNodes[0].nodeValue)

        return

    def unpackFromDict(self, d, seriesFactory):
        LMCPObject.LMCPObject.unpackFromDict(self, d, seriesFactory)
        for key in d:
            if key == "EntityID":
                self.EntityID = d[key]
            elif key == "Waypoints":
                self.Waypoints = []
                for c in d[key]:
                    obj = seriesFactory.unpackFromDict(c)
                    if obj != None:
                        self.Waypoints.append(obj)
            elif key == "TransferMode":
                self.TransferMode = d[key]

        return

    def get_EntityID(self):
        return self.EntityID

    def set_EntityID(self, value):
        self.EntityID = int( value )

    def get_Waypoints(self):
        return self.Waypoints

    def get_TransferMode(self):
        return self.TransferMode

    def set_TransferMode(self, value):
        self.TransferMode = value 



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From WaypointTransfer:\n"
        buf +=    "EntityID = " + str( self.EntityID ) + "\n" 
        buf +=    "Waypoints = " + str( self.Waypoints ) + "\n" 
        buf +=    "TransferMode = " + str( self.TransferMode ) + "\n" 

        return buf;

    def toDict(self):
        m = {}
        self.toDictMembers(m)
        d = {}
        if ("CMASI" is None) or ("CMASI" is ""): # this should never happen
            # need to fill this with error message
            d["datatype"] = str("DEBUG_PROBLEM_HERE" + "/WaypointTransfer")
            d["datastring"] = str(m)
        else:
            d['datatype'] = str("CMASI" + "/WaypointTransfer")
            d['datastring'] = str(m)
        return d

    def toDictMembers(self, d):
        LMCPObject.LMCPObject.toDictMembers(self, d)
        d['EntityID'] = self.EntityID
        d['Waypoints'] = []
        for x in self.Waypoints:
            if x == None:
                d['Waypoints'].append(None)
            else:
                d['Waypoints'].append(x.toDict())
        d['TransferMode'] = self.TransferMode

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
        str = ws + '<WaypointTransfer Series="CMASI" >\n';
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</WaypointTransfer>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<EntityID>" + str(self.EntityID) + "</EntityID>\n"
        buf += ws + "<Waypoints>\n"
        for x in self.Waypoints:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</Waypoints>\n"
        buf += ws + "<TransferMode>" + WaypointTransferMode.get_WaypointTransferMode_int(self.TransferMode) + "</TransferMode>\n"

        return buf
        
