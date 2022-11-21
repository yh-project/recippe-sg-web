<template>
  <v-container>
    레시피 게시글 작성 화면
    <v-btn @click="addRecipe" style="width: 100%">게시글 등록</v-btn>
  </v-container>
</template>

<script>
import herokuAPI from '@/api/heroku.js';

export default {
  data () {},
  methods: {
    addRecipe() {
      const recipe = JSON.stringify (
        {
	        "post_id": 0,
	        "nickname": "test",
	        "title": "heroku_test",
	        "category": "heroku_test",
	        "degree_of_spicy": 1,
	        "description": "heroku_test",
	        "views": 0,
	        "like_count": 0,
	        "comment_count": 0,
	        "upload_time": "",
	        "Recipe_Ingredients": [
		        {
			        "id": 100,
			        "name": "yangpa",
			        "post_id": 0,
			        "unit": "T",
			        "amount": 50.0
		        },
		        {
			        "id": 100,
			        "name": "asparagus",
			        "post_id": 0,
			        "unit": "Kg",
			        "amount": 10.0
		        }
	        ],
	        "comments": [
	        ]
        }
      );
      herokuAPI.recipeAdd(recipe) 
        .then(function (response) {
          console.log("전송 정보",  recipe);
          if(response.status == 200) {
            console.log("응답 정보", response.data);
          }
        })
    }
  }
}
</script>