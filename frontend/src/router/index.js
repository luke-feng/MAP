import Vue from 'vue'
import NotFound from '../views/404page'
import VueRouter from 'vue-router'
import LandingPage from '../views/LandingPage'
import store from '../store/index'
import UserProfile from '../views/UserProfile'
import Register from '../views/Register'
import Overview from '../views/SHINE/Overview'
import UserView from '../views/SHINE/UserView'
import SectorView from '../views/SHINE/SectorView'
import Login from '../views/Login'
import DashBoard from '../views/DashBoard'
import DataSets from '../views/DataSets'
import SectorAttackAnalysis from '../views/SHINE/sectorview/SectorAttackAnalysis'
import SectorAssetAnalysis from '../views/SHINE/sectorview/SectorAssetAnalysis'
import SectorDiscoveryMethodAnalysis from '../views/SHINE/sectorview/SectorDiscoveryMethodAnalysis'
import SectorImpactAnalysis from '../views/SHINE/sectorview/SectorImpactAnalysis'
import SectorAdversaryAnalysis from '../views/SHINE/sectorview/SectorAdversaryAnalysis'
import SectorEconomicAnalysis from '../views/SHINE/sectorview/SectorEconomicAnalysis'
import UserAttackAnalysis from '../views/SHINE/userview/UserAttackAnalysis'
import UserAssetAnalysis from '../views/SHINE/userview/UserAssetAnalysis'
import UserDiscoveryMethodAnalysis from '../views/SHINE/userview/UserDiscoveryMethodAnalysis'
import UserImpactAnalysis from '../views/SHINE/userview/UserImpactAnalysis'
import UserAdversaryAnalysis from '../views/SHINE/userview/UserAdversaryAnalysis'
import UserEconomicImpact from '../views/SHINE/userview/UserEconomicImpact'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: DashBoard,
    beforeEnter: authRequired
  },
  {
    path: '/datasets',
    name: 'datasets',
    component: DataSets
    // beforeEnter: authRequired
  },
  {
    path: '/user',
    name: 'user',
    component: UserProfile
  },
  {
    path: '/join',
    name: 'join',
    component: Register
  },
  {
    path: '/overview',
    name: 'overview',
    component: Overview
  },
  {
    path: '*',
    component: NotFound
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/sectorview',
    name: 'sectorview',
    component: SectorView
  },
  {
    path: '/userview',
    name: 'userview',
    component: UserView
  },
  {
    path: '/userview/economic',
    name: 'UserEconomicImpact',
    component: UserEconomicImpact
  },
  {
    path: '/userview/impact',
    name: 'UserImpactAnalysis',
    component: UserImpactAnalysis
  },
  {
    path: '/userview/adversary',
    name: 'UserAdversaryAnalysis',
    component: UserAdversaryAnalysis
  },
  {
    path: '/userview/attack',
    name: 'UserAttackAnalysis',
    component: UserAttackAnalysis
  },
  {
    path: '/userview/asset',
    name: 'UserAssetAnalysis',
    component: UserAssetAnalysis
  },
  {
    path: '/userview/discovery',
    name: 'UserDiscoveryMethodAnalysis',
    component: UserDiscoveryMethodAnalysis
  },
  {
    path: '/sectorview/economic',
    name: 'SectorEconomicAnalysis',
    component: SectorEconomicAnalysis
  },
  {
    path: '/sectorview/impact',
    name: 'SectorImpactAnalysis',
    component: SectorImpactAnalysis
  },
  {
    path: '/sectorview/adversary',
    name: 'SectorAdversaryAnalysis',
    component: SectorAdversaryAnalysis
  },
  {
    path: '/sectorview/attack',
    name: 'SectorAttackAnalysis',
    component: SectorAttackAnalysis
  },
  {
    path: '/sectorview/asset',
    name: 'SectorAssetAnalysis',
    component: SectorAssetAnalysis
  },
  {
    path: '/sectorview/discovery',
    name: 'SectorDiscoveryMethodAnalysis',
    component: SectorDiscoveryMethodAnalysis
  }
]

function authRequired (to, from, next) {
  if (store.state.authenticated) {
    next()
  } else {
    // Store the desired URL in session storage for when
    // the user 'comes back' authenticated
    sessionStorage.setItem('intercepted', to.fullPath)
    next('/?authprevented')
  }
}

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
