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



class RemoveTasks(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 44
        self.SERIES_NAME = "CMASI"
        self.FULL_LMCP_TYPE_NAME = "afrl.cmasi.RemoveTasks"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 4849604199710720000
        self.SERIES_VERSION = 3

        #Define message fields
        self.TaskList = []   #int64


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = bytearray()
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.extend(struct.pack(">H", len(self.TaskList) ))
        for x in self.TaskList:
            buffer.extend(struct.pack(">q", x ))

        return buffer

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a bytearray and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        self.TaskList = [None] * _arraylen
        if _arraylen > 0:
            self.TaskList = struct.unpack_from(">" + repr(_arraylen) + "q", buffer, _pos )
            _pos += 8 * _arraylen
        return _pos


    def unpackFromXMLNode(self, el, seriesFactory):
        LMCPObject.LMCPObject.unpackFromXMLNode(self, el, seriesFactory)
        for e in el.childNodes:
            if e.nodeType == xml.dom.Node.ELEMENT_NODE:
                if e.localName == "TaskList" and len(e.childNodes) > 0 :
                    self.TaskList = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            self.TaskList.append( int(c.childNodes[0].nodeValue) )

        return

    def unpackFromDict(self, d, seriesFactory):
        LMCPObject.LMCPObject.unpackFromDict(self, d, seriesFactory)
        for key in d:
            if key == "TaskList":
                self.TaskList = []
                for c in d[key]:
                    self.TaskList.append( c )

        return

    def get_TaskList(self):
        return self.TaskList



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From RemoveTasks:\n"
        buf +=    "TaskList = " + str( self.TaskList ) + "\n" 

        return buf;

    def toDict(self):
        m = {}
        self.toDictMembers(m)
        d = {}
        if ("CMASI" is None) or ("CMASI" is ""): # this should never happen
            # need to fill this with error message
            d["datatype"] = str("DEBUG_PROBLEM_HERE" + "/RemoveTasks")
            d["datastring"] = str(m)
        else:
            d['datatype'] = str("CMASI" + "/RemoveTasks")
            d['datastring'] = str(m)
        return d

    def toDictMembers(self, d):
        LMCPObject.LMCPObject.toDictMembers(self, d)
        d['TaskList'] = []
        for x in self.TaskList:
            d['TaskList'].append(x)

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
        str = ws + '<RemoveTasks Series="CMASI" >\n';
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</RemoveTasks>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<TaskList>\n"
        for x in self.TaskList:
            buf += ws + "<int64>" + str(x) + "</int64>\n"
        buf += ws + "</TaskList>\n"

        return buf
        
