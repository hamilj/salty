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

from afrl.cmasi import AutomationRequest
from uxas.messages.task import PlanningState


class TaskAutomationRequest(LMCPObject.LMCPObject):

    def __init__(self):

        self.LMCP_TYPE = 6
        self.SERIES_NAME = "UXTASK"
        self.FULL_LMCP_TYPE_NAME = "uxas.messages.task.TaskAutomationRequest"
        #Series Name turned into a long for quick comparisons.
        self.SERIES_NAME_ID = 6149757930721443840
        self.SERIES_VERSION = 7

        #Define message fields
        self.RequestID = 0   #int64
        self.OriginalRequest = AutomationRequest.AutomationRequest()   #AutomationRequest
        self.SandBoxRequest = False   #bool
        self.PlanningStates = []   #PlanningState


    def pack(self):
        """
        Packs the object data and returns a string that contains all of the serialized
        members.
        """
        buffer = bytearray()
        buffer.extend(LMCPObject.LMCPObject.pack(self))
        buffer.extend(struct.pack(">q", self.RequestID))
        buffer.extend(struct.pack("B", self.OriginalRequest != None ))
        if self.OriginalRequest != None:
            buffer.extend(struct.pack(">q", self.OriginalRequest.SERIES_NAME_ID))
            buffer.extend(struct.pack(">I", self.OriginalRequest.LMCP_TYPE))
            buffer.extend(struct.pack(">H", self.OriginalRequest.SERIES_VERSION))
            buffer.extend(self.OriginalRequest.pack())
        boolChar = 1 if self.SandBoxRequest == True else 0
        buffer.extend(struct.pack(">B",boolChar))
        buffer.extend(struct.pack(">H", len(self.PlanningStates) ))
        for x in self.PlanningStates:
           buffer.extend(struct.pack("B", x != None ))
           if x != None:
               buffer.extend(struct.pack(">q", x.SERIES_NAME_ID))
               buffer.extend(struct.pack(">I", x.LMCP_TYPE))
               buffer.extend(struct.pack(">H", x.SERIES_VERSION))
               buffer.extend(x.pack())

        return buffer

    def unpack(self, buffer, _pos):
        """
        Unpacks data from a bytearray and sets class members
        """
        _pos = LMCPObject.LMCPObject.unpack(self, buffer, _pos)
        self.RequestID = struct.unpack_from(">q", buffer, _pos)[0]
        _pos += 8
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
            self.OriginalRequest = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
            _pos = self.OriginalRequest.unpack(buffer, _pos)
        else:
            self.OriginalRequest = None
        boolChar = struct.unpack_from(">B", buffer, _pos)[0]
        self.SandBoxRequest = True if boolChar == 1 else False
        _pos += 1
        _arraylen = struct.unpack_from(">H", buffer, _pos )[0]
        _pos += 2
        self.PlanningStates = [None] * _arraylen
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
                self.PlanningStates[x] = LMCPFactory.LMCPFactory().createObject(_series, _version, _type )
                _pos = self.PlanningStates[x].unpack(buffer, _pos)
            else:
                self.PlanningStates[x] = None
        return _pos


    def unpackFromXMLNode(self, el, seriesFactory):
        LMCPObject.LMCPObject.unpackFromXMLNode(self, el, seriesFactory)
        for e in el.childNodes:
            if e.nodeType == xml.dom.Node.ELEMENT_NODE:
                if e.localName == "RequestID" and len(e.childNodes) > 0 :
                    self.RequestID = int(e.childNodes[0].nodeValue)
                elif e.localName == "OriginalRequest" and len(e.childNodes) > 0 :
                    for n in e.childNodes:
                        if n.nodeType == xml.dom.Node.ELEMENT_NODE:
                            self.OriginalRequest = seriesFactory.createObjectByName(n.getAttribute('Series'), n.localName)
                            if self.OriginalRequest != None:
                                self.OriginalRequest.unpackFromXMLNode(n, seriesFactory)
                elif e.localName == "SandBoxRequest" and len(e.childNodes) > 0 :
                    self.SandBoxRequest = e.childNodes[0].nodeValue.lower() == 'true'
                elif e.localName == "PlanningStates" and len(e.childNodes) > 0 :
                    self.PlanningStates = []
                    for c in e.childNodes:
                        if c.nodeType == xml.dom.Node.ELEMENT_NODE:
                            obj = seriesFactory.createObjectByName(c.getAttribute('Series'), c.localName)
                            if obj != None:
                                obj.unpackFromXMLNode(c, seriesFactory)
                                self.PlanningStates.append(obj)

        return

    def unpackFromDict(self, d, seriesFactory):
        LMCPObject.LMCPObject.unpackFromDict(self, d, seriesFactory)
        for key in d:
            if key == "RequestID":
                self.RequestID = d[key]
            elif key == "OriginalRequest":
                self.OriginalRequest = seriesFactory.unpackFromDict(d[key])
            elif key == "SandBoxRequest":
                self.SandBoxRequest = d[key]
            elif key == "PlanningStates":
                self.PlanningStates = []
                for c in d[key]:
                    obj = seriesFactory.unpackFromDict(c)
                    if obj != None:
                        self.PlanningStates.append(obj)

        return

    def get_RequestID(self):
        return self.RequestID

    def set_RequestID(self, value):
        self.RequestID = int( value )

    def get_OriginalRequest(self):
        return self.OriginalRequest

    def set_OriginalRequest(self, value):
        self.OriginalRequest = value 

    def get_SandBoxRequest(self):
        return self.SandBoxRequest

    def set_SandBoxRequest(self, value):
        self.SandBoxRequest = bool( value )

    def get_PlanningStates(self):
        return self.PlanningStates



    def toString(self):
        """
        Returns a string representation of all variables
        """
        buf = LMCPObject.LMCPObject.toString(self)
        buf += "From TaskAutomationRequest:\n"
        buf +=    "RequestID = " + str( self.RequestID ) + "\n" 
        buf +=    "OriginalRequest = " + str( self.OriginalRequest ) + "\n" 
        buf +=    "SandBoxRequest = " + str( self.SandBoxRequest ) + "\n" 
        buf +=    "PlanningStates = " + str( self.PlanningStates ) + "\n" 

        return buf;

    def toDict(self):
        m = {}
        self.toDictMembers(m)
        d = {}
        if ("UXTASK" is None) or ("UXTASK" is ""): # this should never happen
            # need to fill this with error message
            d["datatype"] = str("DEBUG_PROBLEM_HERE" + "/TaskAutomationRequest")
            d["datastring"] = str(m)
        else:
            d['datatype'] = str("UXTASK" + "/TaskAutomationRequest")
            d['datastring'] = str(m)
        return d

    def toDictMembers(self, d):
        LMCPObject.LMCPObject.toDictMembers(self, d)
        d['RequestID'] = self.RequestID
        if self.OriginalRequest == None:
            d['OriginalRequest'] = None
        else:
            d['OriginalRequest'] = self.OriginalRequest.toDict()
        d['SandBoxRequest'] = self.SandBoxRequest
        d['PlanningStates'] = []
        for x in self.PlanningStates:
            if x == None:
                d['PlanningStates'].append(None)
            else:
                d['PlanningStates'].append(x.toDict())

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
        str = ws + '<TaskAutomationRequest Series="UXTASK" >\n';
        #str +=LMCPObject.LMCPObject.toXMLMembersStr(self, ws + "  ")
        str += self.toXMLMembersStr(ws + "  ")
        str += ws + "</TaskAutomationRequest>\n";
        return str

    def toXMLMembersStr(self, ws):
        buf = ""
        buf += LMCPObject.LMCPObject.toXMLMembersStr(self, ws)
        buf += ws + "<RequestID>" + str(self.RequestID) + "</RequestID>\n"
        buf += ws + "<OriginalRequest>\n"
        if self.OriginalRequest == None:
            buf += ws + "    <null/>\n"
        else:
            buf += ws + self.OriginalRequest.toXMLStr(ws + "    ") 
        buf += ws + "</OriginalRequest>\n"
        buf += ws + "<SandBoxRequest>" + ('True' if self.SandBoxRequest else 'False') + "</SandBoxRequest>\n"
        buf += ws + "<PlanningStates>\n"
        for x in self.PlanningStates:
            if x == None:
                buf += ws + "    <null/>\n"
            else:
                buf += x.toXMLStr(ws + "    ") 
        buf += ws + "</PlanningStates>\n"

        return buf
        
