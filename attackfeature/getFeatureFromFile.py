import json
import os
import sys


class DDoSGridFeatures:
    def __init__(self, jsonPath, attackId):
        self.path = jsonPath
        self.id = attackId
        genMetrics = self.get_generic_metrics()
        self.StartTimeStamp = genMetrics['StartTimeStamp']
        self.EndTimeStamp = genMetrics['EndTimeStamp']
        self.Duration = genMetrics['Duration']
        self.NrOfIPpackets = genMetrics['NrOfIPpackets']
        self.AttackSizeInBytes = genMetrics['AttackSizeInBytes']
        self.NrOfSrcIps = genMetrics['NrOfSrcIps']
        self.NrOfDstIps = genMetrics['NrOfDstIps']
        self.NrOfSrcPort = genMetrics['NrOfSrcPort']
        self.NrOfDsPort = genMetrics['NrOfDsPort']
        self.Top5SrcIP = str(self.get_top_ip())
        self.Top20DesPort = str(self.get_top_port())
        self.TopHttpVerb = str(self.get_top_http_verb())
        self.TopHttpEndpoint = str(self.get_top_http_endpoint())
        self.TopBrowserOS = str(self.get_top_BrowserOS())
        self.TopDevice = str(self.get_top_Device())

    def get_generic_metrics(self):
        '''
        extract the generic metrics from json file
        :param path: string format, which is the direction of local files(the analysis direction) 
        :param id: string format, which is the attact id, generated from miner module, md5 encrypted
        :return genMetrics, dict formated, including the StartTimeStamp, EndTimeStamp, Duration, NrOfIPpackets, AttackSizeInBytes, NrOfSrcIps, NrOfDstIps, NrOfSrcPort, NrOfDsPort
        '''
        fname = self.id+'.pcap-generic-metrics.json'
        fpath = self.path + self.id + '/' + fname
        genMetrics = dict()
        with open(fpath, 'r') as f:
            j = json.load(f)
            genMetrics['StartTimeStamp'] = j['start']
            genMetrics['EndTimeStamp'] = j['end']
            genMetrics['Duration'] = j['duration']
            genMetrics['NrOfIPpackets'] = j['nrOfIPpackets']
            genMetrics['AttackSizeInBytes'] = j['attackSizeInBytes']
            genMetrics['NrOfSrcIps'] = j['nrOfSrcIps']
            genMetrics['NrOfDstIps'] = j['nrOfDstIps']
            genMetrics['NrOfSrcPort'] = j['nrOfSrcPorts']
            genMetrics['NrOfDsPort'] = j['nrOfDstPorts']
        return genMetrics

    def get_top_ip(self):
        '''
        extract the top 5 source ips from json file
        :param path: string format, which is the direction of local files(the analysis direction) 
        :param id: string format, which is the attact id, generated from miner module, md5 encrypted
        :return Top5SrcIP, list format, including the top 5 source ip of attack
        '''
        fname = self.id+'.pcap-top-5-source-hosts-by-traffic.json'
        fpath = self.path + self.id + '/' + fname
        Top5SrcIP = None
        with open(fpath, 'r') as f:
            j = json.load(f)
            Top5SrcIP = j['piechart']['labels']
        return Top5SrcIP

    def get_top_port(self):
        '''
        extract the top 20 destination ports from json file
        :param path: string format, which is the direction of local files(the analysis direction) 
        :param id: string format, which is the attact id, generated from miner module, md5 encrypted
        :return Top20DesPort, list format, including the 20 destination ports of attack
        '''
        fname = self.id+'.pcap-top20Services.json'
        fpath = self.path + self.id + '/' + fname
        Top20DesPort = None
        with open(fpath, 'r') as f:
            j = json.load(f)
            Top20DesPort = j['barchart']['datasets'][0]['data']
        return Top20DesPort

    def get_top_http_verb(self):
        '''
        extract the top http verb from json file
        :param path: string format, which is the direction of local files(the analysis direction) 
        :param id: string format, which is the attact id, generated from miner module, md5 encrypted
        :return TopHttpVerb, list format, including the number of packet for different http verb ["GET","POST","HEAD","PUT","DELETE","CONNECT","OPTIONS","TRACE","PATCH"]
        '''
        fname = self.id+'.pcap-most-used-http-verbs.json'
        fpath = self.path + self.id + '/' + fname
        TopHttpVerb = None
        with open(fpath, 'r') as f:
            j = json.load(f)
            TopHttpVerb = j['piechart']['datasets'][0]['data']
        return TopHttpVerb

    def get_top_http_endpoint(self):
        '''
        extract the Top HttpEndpoint from json file
        :param path: string format, which is the direction of local files(the analysis direction) 
        :param id: string format, which is the attact id, generated from miner module, md5 encrypted
        :return TopHttpEndpoint, list format, including the top listed http endpoints
        '''
        fname = self.id+'.pcap-most-used-http-endpoints.json'
        fpath = self.path + self.id + '/' + fname
        TopHttpEndpoint = None
        with open(fpath, 'r') as f:
            j = json.load(f)
            TopHttpEndpoint = j['piechart']['labels']
        return TopHttpEndpoint

    def get_top_BrowserOS(self):
        '''
        extract the Top Browser and OS conmbination from json file
        :param path: string format, which is the direction of local files(the analysis direction) 
        :param id: string format, which is the attact id, generated from miner module, md5 encrypted
        :return TopHttpEndpoint, list format, including the top listed Browser and OS conmbination
        '''
        fname = self.id+'.pcap-most-used-browser-and-os-combinations.json'
        fpath = self.path + self.id + '/' + fname
        TopBrowserOS = None
        with open(fpath, 'r') as f:
            j = json.load(f)
            TopBrowserOS = j['piechart']['labels']
        return TopBrowserOS

    def get_top_Device(self):
        '''
        extract the Top device from json file
        :param path: string format, which is the direction of local files(the analysis direction) 
        :param id: string format, which is the attact id, generated from miner module, md5 encrypted
        :return TopHttpEndpoint, list format, including the top listed device
        '''
        fname = self.id+'.pcap-most-used-vendor-and-type-combinations.json'
        fpath = self.path + self.id + '/' + fname
        TopDevice = None
        with open(fpath, 'r') as f:
            j = json.load(f)
            TopDevice = j['piechart']['labels']
        return TopDevice


        
jsonPath = 'D:/vsproject/secgrid/data/analysis/'
attackId = '7bcb9e6b370349eb573dde4457f8a0b3a0ac6436322d3e235a5b8fa62e8c28c3'
r = ['get_top_Device(jsonPath, attackId)']
print(str(r))
