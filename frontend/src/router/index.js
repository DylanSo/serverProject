import Vue from 'vue'
import Router from 'vue-router'
import Detect from "../components/detect";
import Reports from "../components/reports";
import TotalHistory from "../components/totalHistory";
import Help from "../components/help";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'detect',
      component: Detect,
    },
    {
      path: '/reports',
      name: 'reports',
      component: Reports
    },
    {
      path: '/totalHistory',
      name: 'totalHistory',
      component: TotalHistory
    },
    {
      path: '/help',
      name: 'help',
      component: Help
    }

  ]
})
