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

from afrl.cmasi import VehicleAction


class PayloadAction(VehicleAction.VehicleAction):

    def __init__(self):
        VehicleAction.VehicleAction.__init__(self)
        self.LMCP_TYPE = 4
        self.SERIES_NAME = "CMASI"
        self.FULL_LMCP_TYPE_NAME = "afrl.cmasi.PayloadAction"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 3

        #Define message fields
        self.PayloadID = 0   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = bytearray()
        buffer.extend(VehicleAction.VehicleAction.pack(self))
        buffer.extend(struct.pack(">q", self.PayloadID))

        return buffer

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a bytearray and sets class members
        """
        _pos = VehicleAction.VehicleAction.unpack(self, buffer, _pos)
        self.PayloadID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
        return _pos


    def unpackFromXMLNode(self, el, seriesFactory):
        VehicleAction.VehicleAction.unpackFromXMLNode(self, el, seriesFactory)
        for e in el.childNodes:
            if e.nodeType == xml.dom.Node.ELEMENT_NODE:
                if e.localName == "PayloadID" and len(e.childNodes) > 0 :
                    self.PayloadID = int(e.childNodes[0].nodeValue)

        return

    def unpackFromDict(self, d, seriesFactory):
        VehicleAction.VehicleAction.unpackFromDict(self, d, seriesFactory)
        for key in d:
            if key == "PayloadID":
                self.PayloadID = d[key]

        return

    def get_PayloadID(self):
        return self.PayloadID

    def set_PayloadID(self, value):
        self.PayloadID = int( value )



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = VehicleAction.VehicleAction.toString(self)
        buf += "From PayloadAction:\n"
        buf +=    "PayloadID = " + str( self.PayloadID ) + "\n" 

        return buf;

    def toDict(self):
        m = {}
        self.toDictMembers(m)
        d = {}
        if ("CMASI" is None) or ("CMASI" is ""): # this should never happen
            # need to fill this with error message
            d["datatype"] = str("DEBUG_PROBLEM_HERE" + "/PayloadAction")
            d["datastring"] = str(m)
        else:
            d['datatype'] = str("CMASI" + "/PayloadAction")
            d['datastring'] = str(m)
        return d

    def toDictMembers(self, d):
        VehicleAction.VehicleAction.toDictMembers(self, d)
        d['PayloadID'] = self.PayloadID

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
        str = ws + '<PayloadAction Series="CMASI" >\n';
        #str +=VehicleAction.VehicleAction.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</PayloadAction>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += VehicleAction.VehicleAction.toXMLMembersStr(self, ws)
        buf += ws + "<PayloadID>" + str(self.PayloadID) + "</PayloadID>\n"

        return buf
        
