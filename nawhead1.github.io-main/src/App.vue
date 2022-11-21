<template>
  <v-app>
    <router-view />
  </v-app>
</template>

<script>
import router from '@/router/index.js';

export default {
  name: 'App',

  data: () => ({
    
  }),

  created() {
    const UserInfo = JSON.parse(localStorage.getItem("UserInfo"));
    console.log("App.vue created");
    if(UserInfo == null) {
      router.push({name: 'login'});
    } else if(UserInfo.auto_login == false) {
      console.log("오토 로그인 미선택 - 로그인 화면 이동");
      localStorage.removeItem("UserInfo");
      router.push({name: 'login'});
    }
  }
};
</script>
