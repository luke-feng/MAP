<template>
  <div class='howto'>
    <section name='head' class=' slidefromleft'>
    <md-card style='text-align: center;'  md-with-hover>
            <md-card-header :data-background-color='dataBackgroundColor' >
                <h1 class="md-title" > Join SHINE </h1>
                <p >Create your account</p>
            </md-card-header>
    </md-card>
    </section>
    <section name='basic' class=' slidefromleft'>
    <md-card md-alignment='center' md-with-hover>
        <span class='center-span'>
            <md-card-header :data-background-color='dataBackgroundColor'>
                <h2 class='title' > Basic Information </h2>
                <p>Basic information, such as your name and photo, that you use on Our services</p>
            </md-card-header>

            <md-card-content>
                <div class='md-layout'>
                <!--<div class='md-layout-item md-small-size-100 md-size-100'>-->
                    <!--<md-field>-->
                    <!--<label>Company</label>-->
                    <!--<md-input  v-model='company' type='text'></md-input>-->
                    <!--</md-field>-->
                <!--</div>-->
                <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>First Name</label>
                    <md-input v-model='firstname' type='text'></md-input>
                    </md-field>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-100'>
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

                    <!--<md-field :class="getValidationClass('email')">-->
                    <!--<label for="email">Email</label>-->
                    <!--<md-input type="email" name="email" id="email" autocomplete="email" v-model="form.email" :disabled="sending" />-->
                    <!--<span class="md-error" v-if="!$v.form.email.required">The email is required</span>-->
                    <!--<span class="md-error" v-else-if="!$v.form.email.email">Invalid email</span>-->
          <!--</md-field>-->
                </div>
                <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>Password</label>
                    <md-input v-model='password' type='password'></md-input>
                    <!--<Icon type="ios-checkmark-circle" v-if="changeFlag == 1" color="#35B449"/>-->
                    <!--<Icon type="md-close-circle" v-else-if="changeFlag == 2" color="#f00"/>-->
                    </md-field>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>Confirm Password</label>
                    <md-input v-model='confirmpassword' type='password'></md-input>
                    <!--<Icon type="ios-checkmark-circle" v-if="changeAgainFlag == 1" color="#35B449"/>-->
                    <!--<Icon type="md-close-circle" v-else-if="changeAgainFlag == 2" color="#f00"/>-->
                    </md-field>
                </div>
                <!--<div class='md-layout-item md-small-size-100 md-size-33'>-->
                    <!--<md-field>-->
                    <!--<label>City</label>-->
                    <!--<md-input v-model='city' type='text'></md-input>-->
                    <!--</md-field>-->
                <!--</div>-->
                <!--<div class='md-layout-item md-small-size-100 md-size-66'>-->
                    <!--<md-field>-->
                    <!--<label>Country</label>-->
                    <!--<md-input v-model='country' type='text'></md-input>-->
                    <!--</md-field>-->
                <!--</div>-->
               <template>
                  <el-select v-model="country" @change="selectCityByCountryId($event)" filterable placeholder="Country">
                    <el-option v-for="item in CountryOptions" :key="item.countryid" :label="item.countryname" :value="item.countryid">
                      {{item.countryname}}
                    </el-option>
                  </el-select>
                  <el-select v-model="city" clearable placeholder="City" filterable>
                    <el-option v-for="item in CityOption" :label="item.cityname" :key="item.cityid" :value="item.cityid">
                      {{item.cityname}}
                    </el-option>
                  </el-select>
                </template>
                <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>Post Code</label>
                    <md-input v-model='postalcode' type='text'></md-input>
                    </md-field>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-100'>
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
    <md-card md-alignment='center' class='md-layout-item md-small-size-100 md-size-100' md-with-hover>
    </md-card>
        <md-card md-alignment='center' class='md-layout-item md-small-size-100 md-size-100' md-with-hover>
        <span class='center-span'>
            <md-card-header :data-background-color='dataBackgroundColor'>
                <h2 class='title' > Business Profile </h2>
                <p>Business information, such as your business sector and user scale </p>
            </md-card-header>

            <md-card-content>
                <div class='md-layout'>
                <!--<div class='md-layout-item md-small-size-100 md-size-100'>-->
                    <!--<md-field>-->
                    <!--<label>Business Sector</label>-->
                    <!--<md-input  v-model='sector' type='text'></md-input>-->
                    <!--</md-field>-->
                <!--</div>-->
                <!--<div class='md-layout-item md-small-size-100 md-size-100'>-->
                    <!--<md-field>-->
                    <!--<label>Company</label>-->
                    <!--<md-input  v-model='company' type='text'></md-input>-->
                    <!--</md-field>-->
                <!--</div>-->

                 <template>
                  <el-select v-model="sector" @change="selectOrganizationBySectorId($event)" filterable placeholder="Business Sector">
                    <el-option v-for="item in SectorOptions" :key="item.sectorid" :label="item.sector_name" :value="item.sectorid">
                      {{item.sector_name}}
                    </el-option>
                  </el-select>
                  <el-select v-model="company" allow-create clearable placeholder="Company" filterable>
                    <el-option v-for="item in CompanyOption" :label="item.organization_name" :key="item.organization_id" :value="item.organization_id">
                      {{item.organization_name}}
                    </el-option>
                  </el-select>
                </template>

                <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>User scale</label>
                    <md-input v-model='userscale' type='text'></md-input>
                    </md-field>
                </div>
                <div class='md-layout-item md-small-size-100 md-size-100'>
                    <md-field>
                    <label>Revenue</label>
                    <md-input v-model='revenue' type='text'></md-input>
                    </md-field>
                </div>
                <div class='md-layout-item md-size-100 text-right' style='text-align:center;'>
                    <md-button class='md-raised md-fab-bottom-right md-success md-primary' @click="addApplication()">Request access</md-button>
                </div>
                <!--<template>-->
                  <!--<el-checkbox v-model="cannot" label="1">I cannot find my organization</el-checkbox>-->
                <!--</template>-->
                </div>

            </md-card-content>
        </span>
    </md-card>
    </section>
  </div>
</template>
<script>
// import { validationMixin } from 'vuelidate'
// import {
//   required,
//   email,
//   minLength
// } from 'vuelidate/lib/validators'

export default {
  name: 'create-account-form',
  // mixins: [validationMixin],
  props: {
    dataBackgroundColor: {
      type: String,
      default: ''
    }
  },
  mounted () {
    this.getCountry()
    this.getSector()
  },
  data () {
    return {
      firstname: null,
      lastname: null,
      company: null,
      emailadress: null,
      password: null,
      confirmpassword: null,
      city: null,
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
      cannot: false
      // changeFlag: 0,
      // changeAgainFlag: 0,
      // ruleValidate: {
      //     password: [
      //         { required: true, validator: pwdCheck, trigger: 'blur' }
      //     ],
      //     againPassword: [
      //         { required: true, validator: pwdAgainCheck, trigger: 'blur' }
      //     ]
      // }
    }
  },

  // validations: {
  //   firstname: {
  //     required,
  //     minLength: minLength(3)
  //   },
  //   lastname: {
  //     required,
  //     minLength: minLength(3)
  //   },
  //   emailadress: {
  //     required,
  //     email
  //   }
  // },

  methods: {
    addApplication () {
      let data = {
        first_name: this.firstname,
        last_name: this.lastname,
        organization_id: this.company,
        email_address: this.emailadress,
        password: this.password,
        country_id: this.country,
        city_id: this.city,
        postal_code: this.postalcode,
        address: this.address,
        sector_id: this.sector,
        user_scale: this.userscale,
        revenue: this.Revenue
        // is_valid: this.valid
      }
      this.$axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/application/api/add_application/',
        data: this.$qs.stringify(data) }
      )
        .then((res) => {
          // console.log(res)
          this.$message.success('success!')
          this.dialogFormEdit = false
          this.firstname = null
          this.lastname = null
          this.company = null
          this.emailadress = null
          this.password = null
          this.confirmpassword = null
          this.city = null
          this.country = null
          this.postalcode = null
          this.address = null
          this.sector = null
          this.userscale = null
          this.Revenue = null
        })
        .catch(function (error) {
          console.log(error)
        })
    },

    getCountry () {
      // let data={};
      this.$axios.get('http://127.0.0.1:8000/city_country/api/country_list/')
        .then((res) => {
          // console.log(res)
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
        this.$axios.get('http://127.0.0.1:8000/city_country/api/city_list/?countryid=' + event)
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
      this.$axios.get('http://127.0.0.1:8000/sector/api/sector_list/?is_valid=true')
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
        this.$axios.get('http://127.0.0.1:8000/organization/api/org_list/?is_valid=true&sector=' + event)
          .then(response => {
            // console.log(response)
            this.CompanyOption = response.data
          }).catch(function (error) {
            console.log(error)
          })
      }
    }

    // getValidationClass (fieldName) {
    //   const field = this.$v.form[fieldName]
    //   if (field) {
    //     return {
    //       'md-invalid': field.$invalid && field.$dirty
    //     }
    //   }
    // }

    // // 密码验证
    // const:pwdCheck = async(rule, value, callback) => {
    //   let reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[~@#$%\*-\+=:,\\?\[\]\{}]).{6,16}$/
    //   if (value.length < 6) {
    //     this.changeFlag = 2;
    //     return callback(new Error('密码不能少于6位！'));
    //   } else if (value.length > 16) {
    //     this.changeFlag = 2;
    //     return callback(new Error('密码最长不能超过16位！'));
    //   } else if (!reg.test(value)) {
    //     this.changeFlag = 2;
    //     return callback(new Error('密码输入有误，请检查格式是否正确！'));
    //   } else {
    //     this.changeFlag = 1;
    //     callback()
    //   }
    // },
    // // 重复密码验证
    // const:pwdAgainCheck = async(rule, value, callback) => {
    //   if (value.length < 1) {
    //     this.changeAgainFlag = 2;
    //     return callback(new Error('重复密码不能为空！'));
    //   } else if(this.password !== this.confirmpassword){
    //     this.changeAgainFlag = 2;
    //     return callback(new Error('两次输入密码不一致！'));
    //   }else{
    //     this.changeAgainFlag = 1;
    //     callback()
    //   }
    // }
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
