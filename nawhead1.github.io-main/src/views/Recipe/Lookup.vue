<template>
  <v-container>
    <v-row>
      <v-col>
        lookup page
        <v-btn @click="deleteRecipe" style="width: 100%">게시글 삭제</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import herokuAPI from '@/api/heroku.js';

export default {
  data () {
    let requestRecipe = {};
    return requestRecipe;
  },
  mounted() {
    let recipe;
    herokuAPI.recipeLookup(3)
      .then(function(response) {
        console.log("응답 온거", response);
        if(response.status == 200) {
            console.log("조회 성공");
            recipe = response.data;
          }
      })
    this.requestRecipe = recipe;
  },
  methods: {
    deleteRecipe() {
      const deleteTarget = JSON.stringify({
        "post_id": 53,
	      "nickname": "test",
	      "title": "heroku_test2",
	      "category": "heroku_test2",
	      "degree_of_spicy": 5,
        "description": "heroku_test2",
        "views": 0,
        "like_count": 0,
        "comment_count": 0,
        "upload_time": "2022-11-21T15:10:03.102840+09:00",
        "Recipe_Ingredients": [
	        {
		        "id": 56,
		        "name": "yangpa",
		        "post_id": 53,
		        "unit": "T",
		        "amount": 100.0
	        },
	        {
		        "id": 57,
		        "name": "asparagus",
		        "post_id": 53,
		        "unit": "Kg",
		        "amount": 200.0
	        }
        ],
        "comments": [
        ]
      });
      herokuAPI.recipeDelete(deleteTarget)
        .then(function (response){
          if(response.status == 200) {
            console.log("삭제 성공");
          }
        }) 
    },
    
  }
}
</script>