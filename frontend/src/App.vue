<template>
  <div id="app">
    <div class="md-layout">
      <div class="md-layout-item">
        <md-tabs md-sync-route  >
          <md-tab id="tab-home" md-label="home" to="/" md-icon="home" exact></md-tab>
          <md-tab id="tab-dashboard" md-label="dashboard" to="/dashboard" md-icon="dashboard" exact :md-disabled="!this.$store.state.authenticated"></md-tab>
          <md-tab id="tab-data-sets" md-label="datasets" to="/datasets" md-icon="view_list" exact :md-disabled="!this.$store.state.authenticated"></md-tab>
          <md-tab id="tab-SHINE" md-label="SHINE" to="/overview" md-icon="batch_prediction" exact :md-disabled="!this.$store.state.authenticated"></md-tab>
        </md-tabs>
      </div>
      <div class="md-layout-item md-size-10">
        <md-tabs md-sync-route  >
          <md-tab id="tab-user" md-label="user" to="/user" md-icon="account_circle" exact :md-disabled="!this.$store.state.authenticated"></md-tab>
        </md-tabs>
      </div>
    </div>
    <router-view id="main" />
  </div>
</template>

<script>
export default {
  mounted: async function () {
    this.$store.dispatch('determineAuthState')
    setInterval(() => { this.$store.dispatch('pollAnalyses') }, 10000)
  }
}
</script>
<style>
  #app {
    display: flex;
    flex-flow: column;
    height: 100%;
    width: 100%;
    position: absolute;
    overflow: hidden;
    -webkit-animation: fadein 0.5s; /* Safari, Chrome and Opera > 12.1 */
       -moz-animation: fadein 0.5s; /* Firefox < 16 */
        -ms-animation: fadein 0.5s; /* Internet Explorer */
         -o-animation: fadein 0.5s; /* Opera < 12.1 */
            animation: fadein 0.5s;
  }
  .nav {
    flex: 0 1 auto;
    z-index: 1;
  }
  @keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
  /* Firefox < 16 */
  @-moz-keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
  /* Safari, Chrome and Opera > 12.1 */
  @-webkit-keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
  /* Internet Explorer */
  @-ms-keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
  /* Opera < 12.1 */
  @-o-keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
  }
  #main {
    flex: 1 1 auto;
    max-width: 1900px;
    padding-right: 20px;
    padding-left: 20px;
    padding-top: 20px;
    overflow-y: scroll;
    scrollbar-width: none;
  }
  ::-webkit-scrollbar {
    display: none !important;
  }
  .dropdown {
    position: relative;
    display: inline-block;
    }
    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #f9f9f9;
        min-width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    }
    .dropdown-content a {
        color: black;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
    }
    .dropdown:hover .dropdown-content {
        display: block;
    }
    .dropdown:hover .dropbtn {
        background-color: #3e8e41;
    }
    .dropdown-content a:hover {background-color: #f1f1f1}
  @media print {
    .no-print, .no-print * {
      display: none !important;
    }
      }
  .md-button[disabled="disabled"] md-icon { color: var(--md-theme-default-text-primary-on-background,rgba(0,0,0,.38))  }
</style>
