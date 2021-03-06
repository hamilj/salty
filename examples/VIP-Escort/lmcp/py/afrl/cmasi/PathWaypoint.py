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


class PathWaypoint(Waypoint.Waypoint):

    def __init__(self):
        Waypoint.Waypoint.__init__(self)
        self.LMCP_TYPE = 57
        self.SERIES_NAME = "CMASI"
        self.FULL_LMCP_TYPE_NAME = "afrl.cmasi.PathWaypoint"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 3

        #Define message fields
        self.PauseTime = 0   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = bytearray()
        buffer.extend(Waypoint.Waypoint.pack(self))
        buffer.extend(struct.pack(">q", self.PauseTime))

        return buffer

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a bytearray and sets class members
        """
        _pos = Waypoint.Waypoint.unpack(self, buffer, _pos)
        self.PauseTime = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        return _pos


    def unpackFromXMLNode(self, el, seriesFactory):
        Waypoint.Waypoint.unpackFromXMLNode(self, el, seriesFactory)
        for e in el.childNodes:
            if e.nodeType == xml.dom.Node.ELEMENT_NODE:
                if e.localName == "PauseTime" and len(e.childNodes) > 0 :
                    self.PauseTime = int(e.childNodes[0].nodeValue)

        return

    def unpackFromDict(self, d, seriesFactory):
        Waypoint.Waypoint.unpackFromDict(self, d, seriesFactory)
        for key in d:
            if key == "PauseTime":
                self.PauseTime = d[key]

        return

    def get_PauseTime(self):
        return self.PauseTime

    def set_PauseTime(self, value):
        self.PauseTime = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = Waypoint.Waypoint.toString(self)
        buf += "From PathWaypoint:\n"
        buf +=    "PauseTime = " + str( self.PauseTime ) + "\n" 

        return buf;

    def toDict(self):
        m = {}
        self.toDictMembers(m)
        d = {}
        if ("CMASI" is None) or ("CMASI" is ""): # this should never happen
            # need to fill this with error message
            d["datatype"] = str("DEBUG_PROBLEM_HERE" + "/PathWaypoint")
            d["datastring"] = str(m)
        else:
            d['datatype'] = str("CMASI" + "/PathWaypoint")
            d['datastring'] = str(m)
        return d

    def toDictMembers(self, d):
        Waypoint.Waypoint.toDictMembers(self, d)
        d['PauseTime'] = self.PauseTime

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
        str = ws + '<PathWaypoint Series="CMASI" >\n';
        #str +=Waypoint.Waypoint.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</PathWaypoint>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += Waypoint.Waypoint.toXMLMembersStr(self, ws)
        buf += ws + "<PauseTime>" + str(self.PauseTime) + "</PauseTime>\n"

        return buf
        
