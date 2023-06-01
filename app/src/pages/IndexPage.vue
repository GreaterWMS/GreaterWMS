<template>
  <q-page class="flex flex-center">
    <div v-show="!fab1 && !fab2 && !fab3 && !fab4" style="margin-top: -7%;" class="vc-tigger" @click="toggleVc">
      <div class="q-mb-xl" style="color: #4C5875;text-align: center;">
        <div style="font-weight: bold;font-size: 50px;letter-spacing: 10px;">WELCOME</div>
        <div style="font-size: 18px;letter-spacing: 2px;">
          {{ $t('index.index_title') }}
        </div>
      </div>
      <div class="flex flex-center">
        <div id="lottie" style="width: 80%; max-width: 90%"></div>
      </div>
    </div>
    <div v-show="!fab1 && !fab2 && !fab3 && !fab4" style="position: absolute;right: 3%;bottom: 150px;font-family:SourceHanSansCN; font-size: 16px;color: #4C5875;">—— &nbsp;&nbsp;
      {{ slogan }} &nbsp; &nbsp;——</div>
  </q-page>
</template>

<script>
import { ref, computed, defineComponent, onMounted } from 'vue'
import { useStore } from "vuex";
import lottie from 'lottie-web'
import welcome from '../components/welcome.json'

export default defineComponent({
  name: 'IndexPage',
  setup () {
    const $store = useStore()
    const slogan = computed({
      get: () => $store.state.settings.slogan,
      set: val => {
        $store.commit('settings/Slogan', val)
      }
    })
    const fab1 = computed({
      get: () => $store.state.fabchange.fab1,
    })
    const fab2 = computed({
      get: () => $store.state.fabchange.fab2,
    })
    const fab3 = computed({
      get: () => $store.state.fabchange.fab3,
    })
    const fab4 = computed({
      get: () => $store.state.fabchange.fab4,
    })
    const animation = ref(null)

    function initLottie () {
      animation.value = lottie.loadAnimation({
        container: document.getElementById("lottie"),
        renderer: "svg",
        loop: true,
        autoplay: true,
        animationData: welcome
      });
      lottie.setSpeed(3)
    }

    onMounted (() => {
      initLottie()
    })

    return {
      fab1,
      fab2,
      fab3,
      fab4,
      slogan,
      hasClass(obj, cls) {
        return obj.className.match(new RegExp('(\\s|^)' + cls + '(\\s|$)'));
      },
      addClass(obj, cls) {
        if (!this.hasClass(obj, cls)) obj.className += " " + cls;
      },
      toggleClass(obj,cls){
        if(this.hasClass(obj,cls)){
          this.removeClass(obj, cls);
        }else{
          this.addClass(obj, cls);
        }
      },
      removeClass(obj, cls) {
        if (this.hasClass(obj, cls)) {
          var reg = new RegExp('(\\s|^)' + cls + '(\\s|$)');
          obj.className = obj.className.replace(reg, ' ');
        }
      },
      toggleVc(){
        const nowTime = new Date().getTime();
        if(nowTime - this.lastClickTime < 3000){
          this.count ++;
        } else {
          this.count = 0;
        }
        this.lastClickTime = nowTime;
        if(this.count >= 10) {
          let vconDom = document.getElementById('__vconsole');
          this.toggleClass(vconDom,'show')
          this.count = 0;
        }
      }
    }
  }
})
</script>
