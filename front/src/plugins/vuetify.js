import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import SvgIcon from '@jamescoyle/vue-icon'
import '@jamescoyle/svg-icon'
import { mdiAccount } from '@mdi/js'
//import 'vuetify/src/stylus/app.styl'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'

Vue.component('font-awesome-icon', FontAwesomeIcon) // Register component globally
library.add(fas) // Include needed icons


Vue.use(Vuetify, {
    iconfont: 'faSvg',
    svgPath: mdiAccount,
    customIconSvgPath: 'M14.989,9.491L6.071,0.537C5.78,0.246,5.308,0.244,5.017,0.535c-0.294,0.29-0.294,0.763-0.003,1.054l8.394,8.428L5.014,18.41c-0.291,0.291-0.291,0.763,0,1.054c0.146,0.146,0.335,0.218,0.527,0.218c0.19,0,0.382-0.073,0.527-0.218l8.918-8.919C15.277,10.254,15.277,9.784,14.989,9.491z',
    theme:  {
    primary : "#9652ff",
    info: '#ff8000',
    lakers: '#ffd700'
    }

})

export default new Vuetify({
  
    


});
/* to continue for transition
const zoom = Vue.component('zoom', {
    template: '#page',
      methods: {
          enter(el, done) {
              const tl = new TimelineMax({
                  onComplete: done
              })
              
              tl.set(el, {
                  autoAlpha: 0,
                  scale: 2,
                  transformOrigin: '50% 50%'
              })
              
              tl.to(el, 1, {
                  autoAlpha: 1,
                  scale: 1,
                  ease: Power4.easeOut
              })
          },
          leave(el, done) {
              TweenMax.to(el, 1, {
                  scale: 0,
                  ease: Power4.easeOut,
                  onComplete: done
              });
          }	
      }
  })
  */