<template>
  <div class="content">
    <div class="md-layout">
      <div class="md-layout-item  md-size-66">
        <edit-profile-form> </edit-profile-form>
      </div>
      <div class="md-layout-item  md-size-33">
        <user-card> </user-card>
      </div>
    </div>
  </div>
</template>

<script>
import { shinebaseurl } from '@/config/variables.js'
import EditProfileForm from '../views/UserProfile/EditProfileForm'
import UserCard from '../views/UserProfile/UserCard'
export default {
  data () {
    return {
      userId: null,
      allUsers: [],
      firstname: null,
      lastname: null,
      organization: null,
      sector: null,
      email: null
    }
  },
  mounted: async function () {
    this.$store.dispatch('determineAuthState')
    setInterval(() => { this.$store.dispatch('pollAnalyses') }, 10000)
    let userurl = `${shinebaseurl}:8080/auth/info`
    var res = await fetch(userurl, { credentials: 'include' })
    var info = await res.json()
    this.userId = info.id
    this.firstname = info.firstname
    this.lastname = info.lastname
    this.email = info.email
    this.findThisUser()
  },
  methods: {
    async findThisUser () {
      let allUsersUrl = `${shinebaseurl}/userinfo/api/UserList/`
      await this.$axios.get(allUsersUrl)
        .then((res) => {
          this.allUsers = res.data
        })
        .catch(error => {
          console.log(error)
        })
      var found = this.allUsers.find(element => element === this.userId)
      let data = {
        userid: this.userId,
        userfirstname: this.firstname,
        userlastname: this.lastname,
        useremail: this.email
      }
      if (found !== this.userId) {
        this.$axios({
          method: 'post',
          url: `${shinebaseurl}/userinfo/api/UserCreate/`,
          data: this.$qs.stringify(data) }
        )
          .then((res) => {
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    }
  },
  components: {
    EditProfileForm,
    UserCard
  }
}
</script>
