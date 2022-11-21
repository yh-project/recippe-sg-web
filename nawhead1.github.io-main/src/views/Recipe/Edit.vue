<template>
  <v-container>
    수정
	<v-btn @click="editRecipe" style="width: 100%">게시글 수정</v-btn>
  </v-container>
</template>

<script>
import herokuAPI from '@/api/heroku.js';

export default {
  data () {},
  methods: {
    editRecipe() {
      const recipe = JSON.stringify (
        {
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
			        "id": 54,
			        "name": "yangpa",
			        "post_id": 53,
			        "unit": "T",
			        "amount": 100.0
		        },
		        {
			        "id": 55,
			        "name": "asparagus",
			        "post_id": 53,
			        "unit": "Kg",
			        "amount": 200.0
		        }
	        ],
	        "comments": [
	        ]
        }
      );
      herokuAPI.recipeEdit(recipe) 
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