const AbstractPCAPAnalyser = require('./AbstractPCAPAnalyser')

class PortScanAnalyser extends AbstractPCAPAnalyser {
  constructor (parser, outPath) {
    super(parser, outPath)
    this.results = {
    }
  }

  async setUp () {
    this.portNumbers = require('port-numbers')
    this.pcapParser.on('tcpPacket', this.countPort.bind(this))
    this.pcapParser.on('udpPacket', this.countPort.bind(this))
  }

  countPort (transportPacket) {
    if (!transportPacket) {
      return
    }
    var port = transportPacket.dport
    try {
      if (hasProp(this.results, 'port')) {
        this.results[port].count++
      } else {
        this.results[port] = {
          count: 1,
          port: port,
          servicename: 'TBD'
        }
      }
    } catch (e) {
      console.error('Unable to analyse packet', transportPacket)
    }
  }

  getName () {
    return 'Top 10 UDP/TCP ports by number of segments'
  }

  async postParsingAnalysis () {
    var ports = Object.values(this.results)
    ports.sort((a, b) => {
      if (a.count > b.count) { return -1 }
      if (a.count < b.count) { return 1 }
      return 0
    })
    var topTenServices = ports.slice(0, 10)

    var totalNrOfDestinationPorts = ports.length
    var shortResult = {
      topTen: topTenServices,
      total_dst_port: totalNrOfDestinationPorts
    }
    var longResult = ports

    return new Promise((resolve, reject) => {
      const fs = require('fs')
      var fileName = `${this.baseOutPath}-portscan.json`

      var dumpfileName = `${this.baseOutPath}-portscan-dump.json`
      fs.writeFile(fileName, JSON.stringify(shortResult), function (err) {
        if (err) {
          console.err(`Error writing summary file ${fileName}.`)
          reject(err)
        }
        fs.writeFile(dumpfileName, JSON.stringify(longResult), function (err) {
          if (err) {
            console.err(`Error writing dump file ${fileName}.`)
            reject(err)
          }
          resolve({
            attackCategory: 'Transport Layer',
            supportedDiagrams: ['Barchart'],
            summaryFile: fileName,
            dumpFile: dumpfileName
          })
        })
      })
    })
  }
}

function hasProp (targetObject, prop) {
  return Object.prototype.hasOwnProperty.call(targetObject, prop)
}

module.exports = PortScanAnalyser
