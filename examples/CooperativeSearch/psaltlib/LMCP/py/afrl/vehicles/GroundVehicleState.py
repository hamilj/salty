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

from afrl.cmasi import EntityState


class GroundVehicleState(EntityState.EntityState):

    def __init__(self):
        EntityState.EntityState.__init__(self)
        self.LMCP_TYPE = 2
        self.SERIES_NAME = "VEHICLES"
        self.FULL_LMCP_TYPE_NAME = "afrl.vehicles.GroundVehicleState"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6216454340153722195
        self.SERIES_VERSION = 1

        #Define message fields


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = bytearray()
        buffer.extend(EntityState.EntityState.pack(self))

        return buffer

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a bytearray and sets class members
        """
        _pos = EntityState.EntityState.unpack(self, buffer, _pos)
        return _pos


    def unpackFromXMLNode(self, el, seriesFactory):
        EntityState.EntityState.unpackFromXMLNode(self, el, seriesFactory)

        return

    def unpackFromDict(self, d, seriesFactory):
        EntityState.EntityState.unpackFromDict(self, d, seriesFactory)

        return



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = EntityState.EntityState.toString(self)
        buf += "From GroundVehicleState:\n"

        return buf;

    def toDict(self):
        m = {}
        self.toDictMembers(m)
        d = {}
        if ("VEHICLES" is None) or ("VEHICLES" is ""): # this should never happen
            # need to fill this with error message
            d["datatype"] = str("DEBUG_PROBLEM_HERE" + "/GroundVehicleState")
            d["datastring"] = str(m)
        else:
            d['datatype'] = str("VEHICLES" + "/GroundVehicleState")
            d['datastring'] = str(m)
        return d

    def toDictMembers(self, d):
        EntityState.EntityState.toDictMembers(self, d)

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
        str = ws + '<GroundVehicleState Series="VEHICLES" >\n';
        #str +=EntityState.EntityState.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</GroundVehicleState>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += EntityState.EntityState.toXMLMembersStr(self, ws)

        return buf
        
