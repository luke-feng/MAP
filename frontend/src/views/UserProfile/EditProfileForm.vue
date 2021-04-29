<template>
  <div class='howto'>
    <section name='head' class=' slidefromleft'>
    <md-card style='text-align: center;'  md-with-hover>
            <md-card-header :data-background-color='dataBackgroundColor' >
                <h1 class="md-title" > Profile </h1>
                <p >About me</p>
            </md-card-header>
    </md-card>
    </section>
    <section name='basic' class=' slidefromleft'>
    <md-card md-alignment="center" md-with-hover>
        <span class="center-span">
            <md-card-header :data-background-color='dataBackgroundColor'>
                <h2 class='title' > Basic Information </h2>
                <p>Basic information, such as your name and photo, that you use on Our services</p>
            </md-card-header>

            <md-card-content>
                <div class='md-layout'>
                <div class='md-layout-item md-small-size-100 md-size-50'>
                    <md-field>
                    <label>First Name</label>
                    <md-input v-model='firstname' type='text'></md-input>
                    </md-field>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-50'>
                    <md-field>
                    <label>Last Name</label>
                    <md-input v-model='lastname' type='text'></md-input>
                    </md-field>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>Email Address</label>
                    <md-input v-model='emailadress' type='email'></md-input>
                    </md-field>
                </div>
                <!-- <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>Password</label>
                    <md-input v-model='password' type='password'></md-input>
                    </md-field>
                </div> -->
                <div class='md-layout-item md-small-size-100 md-size-50'>
                    <label>Country: </label>
                    <el-select v-model="country" @change="selectCityByCountryId($event)" filterable placeholder="Country">
                    <el-option v-for="item in CountryOptions" :key="item.countryid" :label="item.countryname" :value="item.countryid">
                      {{item.countryname}}
                    </el-option>
                  </el-select>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-50'>
                    <label>City: </label>
                    <el-select v-model="city" clearable placeholder="City" filterable>
                    <el-option v-for="item in CityOption" :label="item.cityname" :key="item.cityid" :value="item.cityid">
                      {{item.cityname}}
                    </el-option>
                  </el-select>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>Post Code</label>
                    <md-input v-model='postalcode' type='text'></md-input>
                    </md-field>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-10s0'>
                    <md-field>
                    <label>Adress</label>
                    <md-input v-model='address' type='text'></md-input>
                    </md-field>
                </div>
                </div>
            </md-card-content>
        </span>
    </md-card>
    </section>
    <section name='business' class=' slidefromleft'>
        <md-card md-alignment="center" class='md-layout-item md-small-size-100 md-size-100' md-with-hover>
        <span class="center-span">
            <md-card-header :data-background-color='dataBackgroundColor'>
                <h2 class='title' > Business Profile </h2>
                <p>Business information, such as your business sector and user scale </p>
            </md-card-header>

            <md-card-content>
                <div class='md-layout'>
                <div class='md-layout-item md-small-size-100 md-size-50'>
                  <label>Business Sector: </label>
                     <el-select v-model="sector" @change="selectOrganizationBySectorId($event)" filterable placeholder="Business Sector">
                    <el-option v-for="item in SectorOptions" :key="item.sectorid" :label="item.sector_name" :value="item.sectorid">
                      {{item.sector_name}}
                    </el-option>
                  </el-select>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-50'>
                  <label>Company: </label>
                    <el-select v-model="company" clearable allow-create placeholder="company" filterable>
                    <el-option v-for="item in CompanyOption" :label="item.organization_name" :key="item.organization_id" :value="item.organization_id">
                      {{item.organization_name}}
                    </el-option>
                  </el-select>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>User scale</label>
                    <md-input v-model='userscale' type='text'></md-input>
                    </md-field>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>Revenue</label>
                    <md-input v-model='Revenue' type='email'></md-input>
                    </md-field>
                </div>
                <div class='md-layout-item md-size-100 text-right' style='text-align:center;'>
                    <el-button type="primary" @click="changeProfile()">Change Profile</el-button >
                </div>
                </div>
            </md-card-content>
          </span>
      </md-card>
    </section>
    <section name='measure' class='measureCard slidefromleft'>
        <md-card md-alignment="center" class='md-layout-item md-small-size-100 md-size-100' md-with-hover>
        <span class="center-span">
            <md-card-header :data-background-color='dataBackgroundColor'>
                <h2 class='title' > Cybersecurity Measures </h2>
                <p>Countemeasures for different type of cyberattacks </p>
            </md-card-header>
            <md-card-content>
              <div class='md-layout'>
                  <div v-for="measure in measures" :key="measure.measure_id" class="dataset">
                    <measure-list-item :measure="measure" @deleted="refresh">
                    </measure-list-item>
                  </div>
                </div>
              <div class='md-layout-item md-size-100 text-right' style='text-align:center;'>
                  <el-button type="primary" plain @click="showMeasureAdd = true" icon="el-icon-edit">Add Measure</el-button>
                </div>
                <md-dialog :md-active.sync="showMeasureAdd">
                  <md-dialog-title>Add a Measure</md-dialog-title>
                  <add-measure-form @done="closeMeasureForm" v-on:stateChanged="updateAddMeasure">
                  </add-measure-form>
                  <md-dialog-actions>
                    <md-button class="md-primary" @click="showMeasureAdd = false">
                      <md-icon>close</md-icon>
                    </md-button>
                  </md-dialog-actions>
                </md-dialog>
            </md-card-content>
          </span>
      </md-card>
    </section>
  </div>
</template>
<script>
import { shinebaseurl } from '@/config/variables.js'
import AddMeasureForm from '@/views/UserProfile/AddMeasureForm'
import MeasureListItem from '@/views/UserProfile/MeasureListItem'
export default {
  name: 'edit-profile-form',
  props: {
    dataBackgroundColor: {
      type: String,
      default: ''
    }
  },
  components: {
    'add-measure-form': AddMeasureForm,
    'measure-list-item': MeasureListItem
  },
  data () {
    return {
      userId: null,
      firstname: null,
      lastname: null,
      company: null,
      emailadress: null,
      organizationid: null,
      sectorid: null,
      city: null,
      password: null,
      country: null,
      postalcode: null,
      address: null,
      sector: null,
      userscale: null,
      Revenue: null,
      CountryOptions: [],
      CityOption: [],
      SectorOptions: [],
      CompanyOption: [],
      cannot: false,
      measures: [],
      showMeasureAdd: false
    }
  },
  mounted: async function () {
    let userurl = `${shinebaseurl}:8080/auth/info`
    var res = await fetch(userurl, { credentials: 'include' })
    var info = await res.json()
    this.userId = info.id
    let sectorurl = `${shinebaseurl}/userinfo/api/UserDetail/` + this.userId
    var res1 = await fetch(sectorurl)
    var info1 = await res1.json()
    this.firstname = info1.userfirstname
    this.lastname = info1.userlastname
    this.company = info1.organization_name
    this.sector = info1.sector_name
    this.organizationid = info1.organizationid
    this.sectorid = info1.sectorid
    this.emailadress = info1.useremail
    this.city = info1.city_name
    this.password = info1.password
    this.country = info1.country_name
    this.postalcode = info1.postal_code
    this.address = info1.address
    this.userscale = info1.userscale
    this.Revenue = info1.revenue
    this.getCountry()
    this.getSector()
    this.fetchDataSets()
  },
  methods: {
    updateAddMeasure: function () {
      this.closeMeasureForm()
      return this.showFileShare
    },
    closeMeasureForm: function () {
      this.showMeasureAdd = false
    },
    changeProfile () {
      let data = {
        userid: this.userId,
        userfirstname: this.firstname,
        userlastname: this.lastname,
        organizationid: this.organizationid,
        organization_name: this.company,
        useremail: this.emailadress,
        password: this.password,
        country_name: this.country,
        city_name: this.city,
        postal_code: this.postalcode,
        address: this.address,
        sector_name: this.sector,
        sectorid: this.sectorid,
        userscale: this.userscale,
        revenue: this.Revenue
        // is_valid: this.valid
      }
      this.$axios({
        method: 'put',
        url: `${shinebaseurl}/userinfo/api/UserDetail/` + this.userId,
        data: this.$qs.stringify(data) }
      )
        .then((res) => {
          this.$message.success('success!')
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getCountry () {
      this.$axios.get(`${shinebaseurl}/city_country/api/country_list/`)
        .then((res) => {
          this.CountryOptions = res.data
        }).catch(function (error) {
          console.log(error)
        })
    },
    selectCityByCountryId (event) {
      // let A = event.target.value
      // console.log(event)
      if (event !== null && event !== '' && event !== undefined) {
        // console.log(event)
        this.$axios.get(`${shinebaseurl}/city_country/api/city_list/?countryid=` + event)
          .then(response => {
            // console.log(response)
            this.CityOption = response.data
          }).catch(function (error) {
            console.log(error)
          })
      }
    },
    getSector () {
      // let data={};
      this.$axios.get(`${shinebaseurl}/sector/api/sector_list/?is_valid=true`)
        .then((res) => {
          // console.log(res)
          this.SectorOptions = res.data
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
    refresh: function () {
      this.fetchDataSets()
    },
    fetchDataSets: async function fetchDataSets () {
      // todo
      try {
        let url = `${shinebaseurl}/measures/api/MeasureRecordListByUser/` + this.userId
        // console.log(url)
        await this.$axios.get(url)
          .then(response => {
            this.measures = response.data
            // console.log(this.measures)
          }).catch(function (error) {
            console.log(error)
          })
      } catch (e) {
        console.log(e)
      }
    }
  },
  watch: {
    showMeasureAdd: async function (newVal, oldVal) {
      if (!newVal) {
        // refresh list
        this.fetchDataSets()
      }
    }
  }
}
</script>
<style scoped>
.howto {
  max-width: 960px;
  margin-left: 30em;
  display: flex;
  flex-direction: column;
}
.about-item {
  padding: 32px 24px 0px 24px;
  box-sizing: border-box;
  order: 1;
}
.higherorder {
  order: 0;
}
.howto:last-child {
  padding-bottom: 32px;
}
section {
  display: block;
}
.icon {
  height: 22px !important;
  filter: invert(100%);
  padding-right: 5px;
}
#chart-icon {
  height: 200px !important;
  float: right;
  shape-outside: polygon(
    372px 218px,
    373px 5px,
    2px 1px,
    4px 428px,
    2px 576px,
    456px 581px,
    457px 398px,
    457px 216px
  );
}
#github-icon {
  height: 80px !important;
  shape-outside: circle(55px at 42px 33px);
  margin: 0 20px 20px 0px;
}
#analysis-icon {
  float: left;
  height: 600px !important;
  margin: 0 20px 20px 0px;
  shape-outside: polygon(
    375px 222px,
    372px 0px,
    2px 1px,
    8px 582px,
    458px 580px,
    453px 265px,
    375px 263px
  );
}
.main-icon-wrapper {
  height: 200px;
  text-align: center;
}
#measureCard {
  padding-top: 20px;
  margin-top: 20px
}
.md-dialog {
  width: 80%;
  max-width: 800px;
}
.main-icon {
  height: 100% !important;
  margin: auto;
}
.left {
  float: left !important;
}
.github-link-wrapper {
  text-align: center;
}
.slidefromleft {
  animation-duration: 1s;
  animation-name: slideinfromleft;
}
.slidefromright {
  animation-duration: 1s;
  animation-name: slideinfromright;
}
@keyframes slideinfromright {
  from {
    transform: translate(-15%, 0);
  }

  to {
    transform: translate(0, 0);
    margin-left: 0%;
  }
}

@keyframes slideinfromleft {
  from {
    transform: translate(15%, 0);
  }

  to {
    transform: translate(0, 0);
    margin-left: 0%;
  }
}
.logo-wrapper {
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
}
.logo {
  height: 3em;
}
ul {
}
.no-list-style {
  list-style: none;
  padding-left: 0px;
}
.no-list-style > li {
  margin-bottom: 10px;
}
@media only screen and (max-width: 600px) {
  #analysis-icon,
  #chart-icon {
    float: none;
    display: block;
    margin: 0 auto;
  }
}
.authActions {
  text-align: center;
  margin-bottom: 20px;
}
.authActions span {
  margin: 0 5px;
}
</style>
