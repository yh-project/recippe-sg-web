<template>
  <v-container>
    <v-form ref="form">
      <v-row>
        <v-col cols="4" offset="4">
          <v-card-title style="justify-content: center">로그인</v-card-title>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="6" offset="3">
          <v-divider></v-divider>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="4" offset="4">
          <v-text-field v-model="info.id" label="id"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="4" offset="4">
          <v-text-field v-model="info.pw" label="password"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="3" offset="4">
          <v-checkbox v-model="info.al" label="자동 로그인"></v-checkbox>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="auto">
          <v-btn @click="signup">회원가입</v-btn>
        </v-col>
        <v-col cols="2">
          <v-btn @click="login" style="width: 100%">login</v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="6" offset="3">
          <v-divider></v-divider>
        </v-col>
      </v-row>

    </v-form>
  </v-container>
</template>

<script>
import herokuAPI from '@/api/heroku.js';
import router from '@/router/index.js';

export default {
  data() {
    return {
      info: {
        id: null,
        pw: null,
        al: false
      }
    }
  },
  methods: {
    login() {
      const loginInfo = JSON.stringify({
        "nickname": null,
        "uid": this.info.id,
        "password": this.info.pw,
        "email": null,
        "auto_login": this.info.al,
      });
      const auto_login = this.info.al;
      console.log(loginInfo);
      herokuAPI.login(loginInfo)
        .then(function (response) {
          console.log("response.status", response.status);
          if(response.status == 200) {
            console.log("로그인 성공")
            const dataString = JSON.stringify({
              "nickname": response.data.nickname,
              "uid": response.data.uid,
              "password": response.data.password,
              "email": response.data.email,
              "auto_login": auto_login,
            });
            console.log(dataString);
            localStorage.setItem("UserInfo", dataString);
            router.push({name: 'home'});
          }
        }) 
        .catch(function (e) {
          console.log(e);
        });
    },
    signup() {
      router.push({
        path: "/email-auth/0",
      })
    }
  }
}
</script>