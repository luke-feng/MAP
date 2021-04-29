<template>
<div class='howto'>
  <md-card class="md-card-profile" md-with-hover>
    <div class='md-card-avatar' >
      <img class='img' :src='cardUserImage' />
    </div>
    <section class=' md-small-size-50 md-size-60'>
    <md-card-content>
      <h2>About me</h2>
      <div class='md-layout'>
        <div class='md-layout-item md-small-size-50 md-size-60'>
          <md-field>
            <label>Name: {{ userName }}</label>
          </md-field>
        </div>
        <div class='md-layout-item md-small-size-50 md-size-60'>
          <md-field>
            <label>Business Sector: {{ sector }}</label>
          </md-field>
        </div>
        <div class='md-layout-item md-small-size-50 md-size-60'>
          <md-field>
            <label>Company: {{ organization }} </label>
          </md-field>
        </div>
      </div>
  </md-card-content>
    </section>
  </md-card>
</div>
</template>
<script>
import { shinebaseurl } from '@/config/variables.js'
export default {
  name: 'user-card',
  props: {
    cardUserImage: {
      type: String,
      default: require('@/assets/photo/user.png')
    }
  },
  data () {
    return {
      userId: null,
      userName: null,
      sector: null,
      organization: null
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
    this.userName = info1.userfirstname
    this.organization = info1.organization_name
    this.sector = info1.sector_name
  }
}
</script>
<style scoped>
.howto {
  max-width: 60%;
  display: flex;
  flex-direction: column;
  animation-duration: 1s;
  animation-name: slideinfromleft;
}
.slidefromleft {
  animation-duration: 1s;
  animation-name: slideinfromleft;
}
@keyframes slideinfromleft {
  from {
    transform: translate(15%, 0);
  }

  to {
    transform: translate(0, 0);
  }
}
</style>
