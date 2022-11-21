<template>
  <v-container>
    <v-layout>
      <!-- 바깥쪽 살구색 배경 -->
      <v-row justify="center">
        <v-col cols="8"> 
          <v-card color="#f5efe6" height="800">
            <v-card color='#f5efe6' height="100" flat></v-card>
            <!-- 안쪽 하얀 배경 -->
            <v-row justify="center">
              <v-col xl12 md10 cols="4" align-content="center">
                <v-card color='#fefefe' height="600" rounded="xl">
          
                  <v-card-title class="justify-center">닉네임 변경</v-card-title>
                  <v-card-title class="pl-15">현재 닉네임</v-card-title>

                  <v-card-title class="justify-center pb-15">{{ nickname }}</v-card-title>
                  <v-card-title class="pt-15 pl-15">새로운 닉네임</v-card-title>
                  
                  <v-col offset="2" cols="8">
                    <v-text-field filled v-model="info.nick" label="새 닉네임" placeholder="새로운 닉네임 입력." class="pb-10"></v-text-field>
                  </v-col>

          
                  <v-row justify="center">
                    
                    <v-card-actions>
                      <v-btn outlined width="120" to="/mypage">취소</v-btn>
                    </v-card-actions>

                    <v-card-actions>
                      <v-btn outlined width="120" @click="NNchange()">확인</v-btn>
                    </v-card-actions>
                  

                  </v-row>

                  

                </v-card>
              </v-col>
            </v-row>
            

  
          </v-card>
        </v-col>
      </v-row>
    </v-layout>
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
      },
      nickname: null
    }
  },
  created() {
    console.log("크리에이티드 들어가지나요")
    const UserInfo = JSON.parse(localStorage.getItem("UserInfo"));
    this.info.nick = UserInfo.nickname
    this.info.id = UserInfo.uid
    this.info.pw = UserInfo.password
    this.info.email = UserInfo.email
    console.log("로컬스토리지에서 유저 정보 받아오기", this.info);
    this.nickname = this.info.nick;
    console.log("현재 닉네임 nickname에 저장", this.nickname);
  },
  methods: {
    NNchange() {
      const userInfo = JSON.stringify({
        "nickname": this.info.nick,
        "uid": this.info.id,
        "password": this.info.pw,
        "email": this.info.email,
        "auto_login": false,
      });
      console.log(userInfo);
      JSON.parse(userInfo);
      herokuAPI.changeNN(userInfo)
        .then(function (response) {
          console.log("nnChange", response)
          if(response.status == 200) {
            console.log("닉넴변경 성공")
            router.push({name: 'mypage'});
          }
        }) 
        .catch(function (e) {
          console.log(e);
        });
    }
  }
}