<template lang="html">
  <el-form ref="form" :model="form" >
    <div class="list">
      <md-list :md-expand-single=true>
        <md-list-item md-expand >
          <h4 class="md-list-item-text">Basic Information</h4>
            <md-list slot="md-expand">
            <md-list-item>
              <el-select v-model="sector" @change="selectOrganizationBySectorId($event)" filterable placeholder="Business Sector">
                <el-option v-for="item in SectorOptions" :key="item.sectorid" :label="item.sector_name" :value="item.sectorid">
                  {{item.sector_name}}
                </el-option>
              </el-select>
              <el-select v-model="organisation" clearable placeholder="Organization" filterable>
                <el-option v-for="item in CompanyOption" :label="item.organization_name" :key="item.organization_id" :value="item.organization_id">
                  {{item.organization_name}}
                </el-option>
              </el-select>
             </md-list-item>
          </md-list>
        </md-list-item>
        <md-list-item md-expand :md-expand-single=true>
          <h4 class="md-list-item-text">Incident Information</h4>
          <md-list slot="md-expand">
            <md-list :md-expand-single=true>
              <md-list-item md-expand >
                <span class="md-list-item-text">Impact information</span>
                <md-list slot="md-expand">
          <md-list-item>
            <el-select v-model="impactRating" clearable placeholder="Impact Rating" filterable>
              <!-- todo impact ration options -->
              <el-option v-for="item in ImpactRatingOption" :label="item.impact_rating" :key="item.impact_rating_id" :value="item.impact_rating_id">
                {{item.impact_rating}}
              </el-option>
            </el-select>
            <el-select v-model="incidentEffect"  clearable placeholder="Incident Effect" filterable multiple>
              <el-option v-for="item in IncidentEffectOption" :label="item.incident_effect" :key="item.incident_effect_id" :value="item.incident_effect_id">
                {{item.incident_effect}}
              </el-option>
            </el-select>
           </md-list-item>
          <md-list-item>
            <el-select v-model="securityCompromise" clearable placeholder="Security Compromise" filterable>
              <el-option v-for="item in SecurityCompromiseOption" :label="item.security_compromise" :key="item.security_compromise_id" :value="item.security_compromise_id">
                {{item.security_compromise}}
              </el-option>
            </el-select>
            <el-select v-model="lossProperty" clearable  placeholder="Loss Property"  filterable multiple>
              <el-option v-for="item in LossPropertyOption" :label="item.loss_property" :key="item.loss_property_id" :value="item.loss_property_id">
                {{item.loss_property}}
              </el-option>
            </el-select>
           </md-list-item>
          <md-list-item>
             <el-select v-model="lossDuration" clearable  placeholder="Loss Duration"  filterable>
              <el-option v-for="item in LossDurationOption" :label="item.loss_duration" :key="item.loss_duration_id" :value="item.loss_duration_id">
                {{item.loss_duration}}
              </el-option>
            </el-select>
          </md-list-item>
          </md-list>
            </md-list-item>
          </md-list>
            <md-list :md-expand-single=true>
              <md-list-item md-expand >
                <span class="md-list-item-text">Adversary Description</span>
                  <md-list slot="md-expand">
                    <md-list-item>
              <el-select v-model="attackerInfrastructure" clearable placeholder="Attacker Infrastructure" filterable multiple>
                <el-option v-for="item in AttackerInfrastructureOption" :label="item.attacker_infrastructure" :key="item.attacker_infrastructure_id" :value="item.attacker_infrastructure_id">
                  {{item.attacker_infrastructure}}
                </el-option>
              </el-select>
              <el-select v-model="threatActorType" clearable  placeholder="Threat Actor Type"  filterable multiple>
                <el-option v-for="item in ThreatActorTypeOption" :label="item.threat_actor_type" :key="item.threat_actor_type_id" :value="item.threat_actor_type_id">
                  {{item.threat_actor_type}}
                </el-option>
              </el-select>
             </md-list-item>
             <md-list-item>
              <el-select v-model="attackerTool" clearable placeholder="Attacker Tool" filterable multiple>
                <el-option v-for="item in AttackerToolOption" :label="item.attacker_tool" :key="item.attacker_tool_id" :value="item.attacker_tool_id">
                  {{item.attacker_tool}}
                </el-option>
              </el-select>
              <el-select v-model="malwareType" clearable  placeholder="Malware Type"  filterable multiple>
                <el-option v-for="item in MalwareTypeOption" :label="item.malware_type" :key="item.malware_type_id" :value="item.malware_type_id">
                  {{item.malware_type}}
                </el-option>
              </el-select>
             </md-list-item>
                </md-list>
          </md-list-item>
          </md-list>
          <md-list :md-expand-single=true>
            <md-list-item md-expand >
              <span class="md-list-item-text">Attack Description </span>
                <md-list slot="md-expand">
                <md-list-item>
              <el-select v-model="incidentCategory" clearable placeholder="Incident Category" filterable>
            <el-option v-for="item in IncidentCategoryOption" :label="item.incident_category" :key="item.incident_category_id" :value="item.incident_category_id">
              {{item.incident_category}}
            </el-option>
          </el-select>
          <el-select v-model="maliciousEmail" clearable placeholder="Malicious Email" filterable multiple allow-create>
            <el-option v-for="item in MaliciousEmailOption" :label="item.organization_name" :key="item.organization_id" :value="item.organization_id">
              {{item.organization_name}}
            </el-option>
          </el-select>
        </md-list-item>
        <md-list-item>
          <el-select v-model="fileHashWatchlist" clearable  placeholder="FileHash Watchlist"  filterable multiple allow-create>
            <el-option v-for="item in FileHashWatchlistOption" :label="item.organization_name" :key="item.organization_id" :value="item.organization_id">
              {{item.organization_name}}
            </el-option>
          </el-select>
          <el-select v-model="domainWatchlist" clearable placeholder="Domain Watchlist" filterable multiple allow-create>
            <el-option v-for="item in DomainWatchlistOption" :label="item.organization_name" :key="item.organization_id" :value="item.organization_id">
              {{item.organization_name}}
            </el-option>
          </el-select>
        </md-list-item>
        <md-list-item>
          <el-select v-model="uRLWatchlist" clearable  placeholder="URL Watchlist"  filterable multiple allow-create>
            <el-option v-for="item in URLWatchlistOption" :label="item.organization_name" :key="item.organization_id" :value="item.organization_id">
              {{item.organization_name}}
            </el-option>
          </el-select>
         </md-list-item>
              </md-list>
          </md-list-item>
        </md-list>
        <md-list :md-expand-single=true>
            <md-list-item md-expand >
              <span class="md-list-item-text">Asset Description </span>
                <md-list slot="md-expand">
                <md-list-item>
              <el-select v-model="systemType" clearable placeholder="System Type" filterable multiple allow-create>
            <el-option v-for="item in SystemTypeOption" :label="item.system_type" :key="item.system_type_id" :value="item.system_type_id">
              {{item.system_type}}
            </el-option>
          </el-select>
          <el-select v-model="assetType" clearable placeholder="Asset Type" filterable multiple allow-create>
            <el-option v-for="item in AssetTypeOption" :label="item.asset_type" :key="item.asset_type_id" :value="item.asset_type_id">
              {{item.asset_type}}
            </el-option>
          </el-select>
        </md-list-item>
              </md-list>
          </md-list-item>
        </md-list>
        <md-list :md-expand-single=true>
            <md-list-item md-expand >
              <span class="md-list-item-text">Discovery Method </span>
                <md-list slot="md-expand">
                <md-list-item>
              <el-select v-model="discoveryMethod" clearable placeholder="Discovery Method" filterable multiple allow-create>
            <el-option v-for="item in DiscoveryMethodOption" :label="item.discovery_method" :key="item.discovery_method_id" :value="item.discovery_method_id">
              {{item.discovery_method}}
            </el-option>
          </el-select>
        </md-list-item>
              </md-list>
          </md-list-item>
        </md-list>
      </md-list>
     </md-list-item>
      <md-list-item md-expand>
        <h4 class="md-list-item-text">Economic Impacts</h4>
        <md-list slot="md-expand">
      <md-list-item>
            <md-field>
              <label>Cost of Equipment Replacement</label>
                <md-textarea v-model="costofEquipmentReplacement" @keyup.ctrl.enter="Cost_of_Equipment_Replacement" md-autogrow></md-textarea>
            </md-field>
            <md-field>
              <label>Cost of Repair</label>
                <md-textarea v-model="costofRepair" @keyup.ctrl.enter="Cost_of_Repair" md-autogrow></md-textarea>
            </md-field>
            </md-list-item>
        <md-list-item>
            <md-field>
              <label>Corporate Income Loss</label>
                <md-textarea v-model="corporateIncomeLoss" @keyup.ctrl.enter="Corporate_Income_Loss" md-autogrow></md-textarea>
            </md-field>
            <md-field>
              <label>Organization Productive Loss</label>
                <md-textarea v-model="organizationProductiveLoss" @keyup.ctrl.enter="Organization_Productive_Loss" md-autogrow></md-textarea>
            </md-field>
            </md-list-item>
        <md-list-item>
            <md-field>
              <label>SLA Loss</label>
                <md-textarea v-model="sLALoss" @keyup.ctrl.enter="SLA_Loss" md-autogrow></md-textarea>
            </md-field>
            <md-field>
              <label>Indirect Loss</label>
                <md-textarea v-model="indirectLoss" @keyup.ctrl.enter="Indirect_Loss" md-autogrow></md-textarea>
            </md-field>
          </md-list-item>
        </md-list>
      </md-list-item>
    </md-list>
    <div class="share-btn-wrapper" style='text-align:center;'>
      <md-button class="md-raised md-primary" @click="shareInformation" :disabled="!isDefined">
        Save
      </md-button>
  </div>
  </div>
  </el-form>
</template>

<script>
import { apibaseurl, shinebaseurl } from '@/config/variables.js'

export default {
  name: 'ListExpansion',
  props: ['dataset', 'showFileShare'],
  data () {
    return {
      user: null,
      organisation: '',
      sector: '',
      costofEquipmentReplacement: 0,
      costofRepair: 0,
      corporateIncomeLoss: 0,
      organizationProductiveLoss: 0,
      sLALoss: 0,
      indirectLoss: 0,
      impactRating: '',
      incidentEffect: [],
      securityCompromise: '',
      lossDuration: '',
      lossProperty: [],
      attackerInfrastructure: [],
      threatActorType: [],
      attackerTool: [],
      malwareType: [],
      maliciousEmail: '',
      iPWatchlist: '',
      fileHashWatchlist: '',
      domainWatchlist: '',
      uRLWatchlist: '',
      incidentCategory: '',
      systemType: [],
      assetType: [],
      discoveryMethod: [],
      attactId: '',
      attactName: '',
      start: 0,
      end: 0,
      duration: null,
      nrOfIPpackets: null,
      attackSizeInBytes: null,
      attackBandwidthInBps: null,
      avgPacketSize: null,
      nrOfIPv4Packets: null,
      nrOfIPv6Packets: null,
      nrOfSrcIps: null,
      nrOfDstIps: null,
      nrOfSrcPorts: null,
      nrOfDstPorts: null,
      nrOfUDPPackets: null,
      nrOfTCPPackets: null,
      udpToTcpRatio: null,
      nrOfHTTP: null,
      nrOfICMP: null,
      featureUrl: null,
      informationUrl: null,
      SectorOptions: null,
      CompanyOption: null,
      ImpactRatingOption: null,
      IncidentEffectOption: null,
      SecurityCompromiseOption: null,
      LossPropertyOption: null,
      LossDurationOption: null,
      AttackerInfrastructureOption: null,
      ThreatActorTypeOption: null,
      AttackerToolOption: null,
      MalwareTypeOption: null,
      IncidentCategoryOption: null,
      MaliciousEmailOption: null,
      FileHashWatchlistOption: null,
      DomainWatchlistOption: null,
      URLWatchlistOption: null,
      SystemTypeOption: null,
      AssetTypeOption: null,
      DiscoveryMethodOption: null,
      showSuccess: false
    }
  },
  mounted: function () {
    this.getSector()
    this.getImpactRatingOption()
    this.getIncidentEffectOption()
    this.getSecurityCompromiseOption()
    this.getLossPropertyOption()
    this.getLossDurationOption()
    this.getAttackerInfrastructureOption()
    this.getThreatActorTypeOption()
    this.getAttackerToolOption()
    this.getMalwareTypeOption()
    this.getIncidentCategoryOption()
    this.getSystemTypeOption()
    this.getAssetTypeOption()
    this.getDiscoveryMethodOption()
    // console.log(this.dataset)
    let url = `${apibaseurl}/public/${this.dataset.analysisFiles[8].file}`
    this.user = this.dataset.users[0]
    // console.log(this.user)
    this.featureUrl = `${shinebaseurl}/attackfeatures/api/AttackFeatureRecordCreate/`
    this.informationUrl = `${shinebaseurl}/attackinfo/api/AttackInformationRecordCreate/`
    this.attactId = this.dataset.md5
    this.attactName = this.dataset.name
    this.start = this.dataset.metrics.start
    this.end = this.dataset.metrics.end
    this.duration = this.dataset.metrics.duration
    // console.log(this.start)
    this.nrOfIPpackets = this.dataset.metrics.nrOfIPpackets
    this.attackSizeInBytes = this.dataset.metrics.attackSizeInBytes
    this.attackBandwidthInBps = this.dataset.metrics.attackBandwidthInBps
    this.avgPacketSize = this.dataset.metrics.avgPacketSize
    this.nrOfIPv4Packets = this.dataset.metrics.nrOfIPv4Packets
    this.nrOfIPv6Packets = this.dataset.metrics.nrOfIPv6Packets
    this.nrOfSrcIps = this.dataset.metrics.nrOfSrcIps
    this.nrOfDstIps = this.dataset.metrics.nrOfDstIps
    this.nrOfSrcPorts = this.dataset.metrics.nrOfSrcPorts
    this.nrOfDstPorts = this.dataset.metrics.nrOfDstPorts
    this.nrOfUDPPackets = this.dataset.metrics.nrOfUDPPackets
    this.nrOfTCPPackets = this.dataset.metrics.nrOfTCPPackets
    this.udpToTcpRatio = this.dataset.metrics.udpToTcpRatio
    this.nrOfHTTP = this.dataset.metrics.nrOfHTTP
    this.nrOfICMP = this.dataset.metrics.nrOfICMP
    fetch(url).then(resp => resp.json()).then(json => { this.iPWatchlist = json.piechart.labels })
    this.iPWatchlist = this.getIpwatchList(url)
    this.iPWatchlist = null
    // console.log(this.iPWatchlist)
  },
  computed: {
    isDefined: function () {
      return this.organisation && this.sector
    }
  },
  methods: {
    shareInformation () {
      // this.fetchToAttackFeature(this.featureUrl)
      this.fetchToAttackInformation(this.informationUrl)
      // this.showSuccess = true
      this.$message({
        message: 'Share Information Success.',
        type: 'success'
      })
      this.$emit('stateChanged')
    },
    clear () {
      this.organisation = null
      this.sector = null
    },
    getSector () {
      // let data={};
      let url = `${shinebaseurl}/sector/api/sector_list/?is_valid=true`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.SectorOptions = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getImpactRatingOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/ImpactratingList/`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.ImpactRatingOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getIncidentEffectOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/IncidenteffectList/?is_valid=`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.IncidentEffectOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getSecurityCompromiseOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/SecuritycompromiseList/`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.SecurityCompromiseOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getLossDurationOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/LossdurationList/`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.LossDurationOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getLossPropertyOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/LosspropertyList/?is_valid=`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.LossPropertyOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getAttackerInfrastructureOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/AttackerinfrastructureList/?is_valid=`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.AttackerInfrastructureOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getThreatActorTypeOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/ThreatactortypeList/?is_valid=`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.ThreatActorTypeOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getAttackerToolOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/AttackertoolList/?is_valid=`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.AttackerToolOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getMalwareTypeOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/MalwaretypeList/?is_valid=`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.MalwareTypeOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getIncidentCategoryOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/IncidentcategoryList/`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.IncidentCategoryOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getSystemTypeOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/SystemtypeList/?is_valid=`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.SystemTypeOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getAssetTypeOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/AssettypeList/?is_valid=`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.AssetTypeOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    getDiscoveryMethodOption () {
      // let data={};
      let url = `${shinebaseurl}/info_share/api/DiscoverymethodList/?is_valid=`
      // console.log(url)
      this.$axios.get(url)
        .then((res) => {
          // console.log(res)
          this.DiscoveryMethodOption = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    selectOrganizationBySectorId (event) {
      if (event !== null && event !== '' && event !== undefined) {
        // console.log(event)
        this.$axios.get(`${shinebaseurl}/organization/api/org_list/?is_valid=true&sector=` + event)
          .then(response => {
            // console.log(response)
            this.CompanyOption = response.data
          }).catch(function (error) {
            console.log(error)
          })
      }
    },
    fetchToAttackFeature (url) {
      var data = {
        attack_id: this.attactId,
        // start_time_stamp: this.start,
        // end_time_stamp: this.end,
        start_time_stamp: 1594378800,
        end_time_stamp: 1594378810,
        duration: this.duration
      }
      // data = JSON.stringify(data)
      // console.log(data)
      // console.log(url)
      this.$axios({
        method: 'post',
        url: url,
        data: this.$qs.stringify(data) }
      )
        .then((res) => {
          // console.log(res)
        })
        .catch(function (error) {
          console.log(error)
        })
      // fetch(url, {
      //   method: 'POST',
      //   body: JSON.stringify(data),
      //   headers: new Headers({
      //     'Content-Type': 'application/json'
      //   })
      // }).then(res => res.json())
      //   .catch(error => console.error('Error:', error))
      //   .then(response => console.log('Success:', response))
    },
    getIpwatchList (url) {
      var topIp
      fetch(url).then(resp => resp.json()).then(json => { topIp = json.piechart.labels })
      console(topIp)
      return topIp
    },
    fetchToAttackInformation (url) {
      let data = {
        user_id: this.user,
        attack_id: this.attactId,
        // attactName: this.attactName,
        organization_id: this.organisation,
        start_time_stamp: this.start,
        end_time_stamp: this.end,
        // start_time_stamp: 1594378800,
        // end_time_stamp: 1594378810,
        sector_id: this.sector,
        costofequipmentreplacement: this.costofEquipmentReplacement,
        costofrepair: this.costofRepair,
        corporate_income_loss: this.corporateIncomeLoss,
        organization_productive_loss: this.organizationProductiveLoss,
        sla_loss: this.sLALoss,
        indirect_loss: this.indirectLoss,
        impact_rating: this.impactRating,
        incidentEffect: this.incidentEffect.join(';'),
        security_compromise: this.securityCompromise,
        loss_duration: this.lossDuration,
        malwareType: this.malwareType.join(';'),
        lossProperty: this.lossProperty.join(';'),
        attackerInfrastructure: this.attackerInfrastructure.join(';'),
        // attackerInfrastructure: [],
        threatActorType: this.threatActorType.join(';'),
        attackerTool: this.attackerTool.join(';'),
        // attackerTool: [],
        malicious_e_mail: this.maliciousEmail.join(';'),
        ip_watchlist: this.iPWatchlist.join(';'),
        file_hash_watchlist: this.fileHashWatchlist.join(';'),
        domain_watchlist: this.domainWatchlist.join(';'),
        url_watchlist: this.uRLWatchlist.join(';'),
        // iPWatchlist: '',
        // maliciousEmail: '',
        // fileHashWatchlist: '',
        // domainWatchlist: '',
        // uRLWatchlist: '',
        incident_category: this.incidentCategory,
        systemType: this.systemType.join(';'),
        assetType: this.assetType.join(';'),
        discoveryMethod: this.discoveryMethod.join(';')
        // start: this.start,
        // end: this.end,
        // duration: this.duration,
        // nrOfIPpackets: this.nrOfIPpackets,
        // attackSizeInBytes: this.attackSizeInBytes,
        // attackBandwidthInBps: this.attackBandwidthInBps,
        // avgPacketSize: this.avgPacketSize,
        // nrOfIPv4Packets: this.nrOfIPv4Packets,
        // nrOfIPv6Packets: this.nrOfIPv6Packets,
        // nrOfSrcIps: this.nrOfSrcIps,
        // nrOfDstIps: this.nrOfDstIps,
        // nrOfSrcPorts: this.nrOfSrcPorts,
        // nrOfDstPorts: this.nrOfDstPorts,
        // nrOfUDPPackets: this.nrOfUDPPackets,
        // nrOfTCPPackets: this.nrOfTCPPackets,
        // udpToTcpRatio: this.udpToTcpRatio,
        // nrOfHTTP: this.nrOfHTTP,
        // nrOfICMP: this.nrOfICMP
      }
      // data = JSON.stringify(data)
      // console.log(data)
      // console.log(url)
      this.$axios({
        method: 'post',
        url: url,
        data: this.$qs.stringify(data) }
      )
        .then((res) => {
          // console.log(res)
        })
        .catch(function (error) {
          console.log(error)
        })
      // this.$message({
      //   message: 'Save Measure Success.',
      //   type: 'success'
      // })
    //   fetch(url, {
    //     method: 'POST',
    //     body: JSON.stringify(data),
    //     headers: new Headers({
    //       'Content-Type': 'application/json'
    //     })
    //   }).then(res => res.json())
    //     .catch(error => console.error('Error:', error))
    //     .then(response => console.log('Success:', response))
    }
  }
}
</script>

<style lang="css">
#form {
    width: 120%;
    margin: auto;
  }
</style>
