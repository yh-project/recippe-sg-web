<template>
  <v-container >
    <v-form ref="form">
      <v-row>
        <v-col cols="4" offset="4">
          <v-card-title style="justify-content: center">레쉽피 회원가입</v-card-title>
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
          <v-text-field v-model="info.nick" label="nickname"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="4" offset="4">
          <v-text-field v-model="info.pw" label="password"></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="4" offset="4">
          <v-text-field v-model="info.pwcheck" label="check password"></v-text-field>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="auto">
          <v-btn to="/login">돌아가기</v-btn>
        </v-col>
        <v-col cols="2">
          <v-btn @click="signup" style="width: 100%">회원가입</v-btn>
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
        email: null,
        id: null,
        nick: null,
        pw: null,
        pwcheck: null
      }
    }
  },
  created() {
    this.info.email = localStorage.getItem("email");
    console.log("로컬스토리지에서 이메일 받아오기", this.info.email);
    localStorage.removeItem("email");
  },
  methods: {
    signup() {
      const signupInfo = JSON.stringify({
        "nickname": this.info.nick,
        "uid": this.info.id,
        "password": this.info.pw,
        "email": this.info.email,
        "auto_login": false,
      });
      console.log(signupInfo);
      JSON.parse(signupInfo);
      herokuAPI.signup(signupInfo)
        .then(function (response) {
          console.log("login", response)
          if(response.status == 200) {
            console.log("회원가입 성공")
            router.push({name: 'login'});
          }
        }) 
        .catch(function (e) {
          console.log(e);
        });
    },
  }
}
</script>