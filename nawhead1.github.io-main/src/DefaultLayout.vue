<template>
  <v-card class="overflow-hidden">
    <v-app-bar
      color="#f5efe6"
      app dense fixed
    >
      <v-spacer />

      <v-toolbar-title>레쉽피</v-toolbar-title>

      <v-spacer />
      <v-spacer />
      <v-spacer />
      <v-spacer />

      <v-btn @click="logout">로그아웃</v-btn>

      <v-spacer />

      <template v-slot:extension>
        <v-row>
          <v-spacer />
          <v-col>
            <v-btn to="/recipe" style="width: 100%">레시피 게시판</v-btn>
          </v-col>
          <v-col>
            <v-btn to="/photo" style="width: 100%">요리 사진 게시판</v-btn>
          </v-col>
          <v-col>
            <v-btn to="/mypage" style="width: 100%">마이페이지</v-btn>
          </v-col>
          <v-spacer />
        </v-row>
      </template>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>

    <v-footer
    color="#f5efe6"
    app
    >
      <div>푸터 위치입니다아</div>
    </v-footer>
  </v-card>
</template>

<script>
import router from '@/router/index.js';

export default {
  methods: {
    logout() {
      localStorage.removeItem("UserInfo");
      router.push({name: 'login'});
    }
  }
}
</script>