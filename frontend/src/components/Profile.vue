<template>
  <md-card>
    <md-card-header>
      <div v-if="this.$store.state.authenticated">
        <div class="md-title">Welcome back, {{ firstname }} {{ lastname }}</div>
        <div class="md-subhead">{{ email }}</div>
      </div>
      <div v-else>
        <div class="md-title">You are not logged in</div>
      </div>

      <md-card-media>
        <img src="https://ddosdb.org/static/ddosdb/img/logo-new.svg" alt="People">
      </md-card-media>
    </md-card-header>

    <md-card-content v-if="this.$store.state.authenticated">
      You are logged in with your DDoSDB account as <code>{{ name }}</code> and can get started using DDoSGrid.
    </md-card-content>
    <md-card-content v-else>
        Please login using your DDoSDB account. If you don't have such an account you can request access on DDoSDB.
    </md-card-content>

    <md-card-actions>
      <md-button v-if="this.$store.state.authenticated" class="md-primary" href="datasets">
        <md-icon>arrow_right_alt</md-icon><span>Get Started</span>
      </md-button>
      <md-card-content v-else>
        <md-button class="md-accent shakebtn"  :href="authurl">
        <md-icon>login</md-icon> <span> Log In</span>
      </md-button>
      <span class="md-title"> or </span>
      <md-button class="md-primary shakebtn"  :href="joinurl">
        <md-icon>create</md-icon> <span> Sign Up</span>
      </md-button>
      </md-card-content>
      <!-- TODO: implement logout endpoint  -->
      <!--md-button>Logout</md-button-->
    </md-card-actions>
  </md-card>
</template>

<script>
import { apibaseurl } from '@/config/variables.js'

export default {
  data: function () {
    return {
      authurl: `${apibaseurl}/auth/provider/`,
      infourl: `${apibaseurl}/auth/info`,
      joinurl: '/join',
      name: '',
      email: '',
      firstname: '',
      lastname: '',
      id: ''
    }
  },
  mounted: async function () {
    var res = await fetch(this.infourl, { credentials: 'include' })
    var info = await res.json()
    this.name = info.name
    this.email = info.email
    this.firstname = info.firstname
    this.lastname = info.lastname
    this.id = info.id
  },
  name: 'Profile'
}
</script>

<style scoped>
.md-card-media {
  right: 0;
  position: absolute;
  top: 2em;
  right: 2em;
}
.md-card-actions {
  justify-content: center !important;
}
.shakebtn {
  -webkit-animation-name: wiggle;
  -ms-animation-name: wiggle;
  -ms-animation-duration: 500ms;
  -webkit-animation-duration: 500ms;
  -webkit-animation-iteration-count: 1;
  -ms-animation-iteration-count: 1;
  -webkit-animation-timing-function: ease-in-out;
  -ms-animation-timing-function: ease-in-out;
}

@-webkit-keyframes wiggle {
  0% {-webkit-transform: rotate(10deg);}
  25% {-webkit-transform: rotate(-10deg);}
  50% {-webkit-transform: rotate(20deg);}
  75% {-webkit-transform: rotate(-5deg);}
  100% {-webkit-transform: rotate(0deg);}
}

@-ms-keyframes wiggle {
  0% {-ms-transform: rotate(1deg);}
  25% {-ms-transform: rotate(-1deg);}
  50% {-ms-transform: rotate(1.5deg);}
  75% {-ms-transform: rotate(-5deg);}
  100% {-ms-transform: rotate(0deg);}
}

@keyframes wiggle {
  0% {transform: rotate(5deg);}
  25% {transform: rotate(-5deg);}
  50% {transform: rotate(10deg);}
  75% {transform: rotate(-2deg);}
  100% {transform: rotate(0deg);}
}
code {
  display: inline;
  padding: 0.2em .4em;
  margin: 0;
  background-color: rgba(27,31,35,.05);
  border-radius: 6px;
}
</style>
