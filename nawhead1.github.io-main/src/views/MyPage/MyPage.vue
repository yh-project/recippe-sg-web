<template>
  <v-container>
    <v-layout>
      <v-col offset="1" cols="10">
        <v-card color="#f5efe6" class="py-2">
          <v-card-title class="pl-10">나의 활동</v-card-title>
          <v-card-text class="pl-15">내가 쓴 레시피</v-card-text>
          <v-card-text class="pl-15">좋아요 누른 레시피</v-card-text>
          <v-card-text class="pl-15">댓글 단 레시피</v-card-text>
        </v-card>
      </v-col>
    </v-layout>

    <v-layout>
      <v-col offset="1" cols="5">
        <v-card color="#f5efe6" class="py-2">
          <v-card-title class="pl-10">냉장고</v-card-title>
        </v-card>
      </v-col>


      <v-col cols="5">
        <v-card color="#f5efe6" class="py-2">
          <v-card-title class="pl-10">쪽지함</v-card-title>
        </v-card>
      </v-col>
      
    </v-layout>

    <v-layout>
      <v-col offset="1" cols="10" class="py-2">
        <v-card color="#f5efe6" class="py-2">
          <v-card-title class="ml-10">계정 관리</v-card-title>
          <v-card-actions class="ml-15">
            <v-btn @click="changeNi()">닉네임 변경</v-btn>
          </v-card-actions>
          <v-card-actions class="ml-15">
            <v-btn @click="changePW()">비밀번호 변경</v-btn>
          </v-card-actions>
          
        </v-card>
      </v-col>
    </v-layout>


    <!-- <v-btn @click="changePW">비밀번호 변경</v-btn> -->
  </v-container>
</template>

<style>

</style>

<script>
import router from '@/router/index.js';

export default {
  methods: {
    changePW() {
      router.push({
        path: "/email-auth/1",
      })
    },
    changeNi() {
      router.push({
        path: "/mypage/changeNickname",
      })
    }
  }
}
</script>