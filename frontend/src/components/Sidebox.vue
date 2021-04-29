<template>
  <div class='sidebox'>
      <sidebar-menu
      :menu="menu"
      :theme="theme"
      :collapsed="collapsed"
      :width="width"
      @item-click="onItemClick"
      @collapse="onCollapse"
      class='sidebar'/>
    </div>
</template>
<script>
export default {
  name: 'sidebox',
  data () {
    return {
      width: '12%',
      theme: 'white-theme',
      menu: [
        {
          header: true,
          title: 'SHINE',
          hiddenOnCollapse: true
        },
        {
          href: '/overview',
          title: 'Overview',
          icon: 'fa fa-list-alt'
        },
        {
          href: '/sectorview',
          title: 'Sector View',
          icon: 'fa fa-list-ul',
          child: [
            {
              href: '/sectorview#economic',
              title: 'Economic View',
              child: [
                {
                  href: '/sectorview/economic',
                  title: 'Economic Analysis'
                }
              ]
            },
            {
              href: '/sectorview#incident',
              title: 'Incident Statistics',
              child: [
                {
                  href: '/sectorview/impact',
                  title: 'Impact Analysis'
                },
                {
                  href: '/sectorview/adversary',
                  title: 'Adversary Analysis'
                },
                {
                  href: '/sectorview/attack',
                  title: 'Attack Analysis'
                },
                {
                  href: '/sectorview/asset',
                  title: 'Asset Analysis'
                },
                {
                  href: '/sectorview/discovery',
                  title: 'Discovery Method Analysis'
                }
              ]
            }
          ]
        },
        {
          href: '/userview',
          title: 'User View',
          icon: 'fa fa-list-ul',
          child: [
            {
              href: '/userview#economic',
              title: 'Economic View',
              child: [
                {
                  href: '/userview/economic',
                  title: 'Economic Analysis'
                }
              ]
            },
            {
              href: '/userview#incident',
              title: 'Incident Statistics',
              child: [
                {
                  href: '/userview/impact',
                  title: 'Impact Analysis'
                },
                {
                  href: '/userview/adversary',
                  title: 'Adversary Analysis'
                },
                {
                  href: '/userview/attack',
                  title: 'Attack Analysis'
                },
                {
                  href: '/userview/asset',
                  title: 'Asset Analysis'
                },
                {
                  href: '/userview/discovery',
                  title: 'Discovery Method Analysis'
                }
              ]
            }
          ]
        }
      ]
    }
  }
}
</script>

<style>
.sidebar.v-sidebar-menu {
  margin-top: 5em;
  background-color: #f2f2f2;
}
.sidebar.v-sidebar-menu.vsm_white-theme .vsm--link {
    color: #2b2b2b;
}
.sidebar.v-sidebar-menu .vsm--mobile-item {
  z-index: 0 !important;
}
.sidebar.v-sidebar-menu.vsm_collapsed .vsm--link_level-1:hover {
  background-color: transparent;
}
.sidebar.v-sidebar-menu .vsm-arrow:after {
  content: "\f105";
  font-family: "FontAwesome";
}
.sidebar.v-sidebar-menu .collapse-btn:after {
  content: "\f07e";
  font-family: "FontAwesome";
}
</style>
