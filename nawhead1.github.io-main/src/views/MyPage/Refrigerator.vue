<template>
  <v-container>
    <v-layout>
      <v-row justify="center">
        <v-col cols="8">
          <v-card min-height="800" color="#f5efe6">
            <v-card-title id="title1" class="pt-16 pl-16 pb-10">
              냉장고
            </v-card-title>
            <v-layout>
              <v-row justify="center">
                <v-col cols="10">
                  <v-card height="500">
                    <v-row justify="space-between">
                      <v-card-title id="title2" class="pl-10">
                        보유 재료
                      </v-card-title>
                      <v-btn round color="#7895b2" dark class="mt-4 mr-10">재료추가</v-btn>
                    </v-row>
                    
                    <!-- 여기서부턴 vfor 문법을 사용해서 무한 리스트를 만들어야 합니다. -->
                    
                  </v-card>
                </v-col>
              </v-row>  
            </v-layout>
          </v-card>
        </v-col>
      </v-row>
    </v-layout>
  </v-container>
</template>

// Pagination

<style>
  #title1{
    font-size: 2em;
    color: #7895b2;
  }
  #title2{
    font-size: 1.4em;
    color: #7895b2;
  }
</style>