import axios from "axios";

const BASE_URL = "https://recippe-sg.herokuapp.com/"

export default {
  login: function(User) {
    return axios.post(BASE_URL+'login/', User);
  },
  firstcheck: function(info) {
    return axios.post(BASE_URL+'firstcheck/', info);
  },
  secondcheck: function(info) {
    return axios.post(BASE_URL+'secondcheck/', info);
  },
  signup: function(info) {
    return axios.post(BASE_URL+'signup/', info);
  },
  changeNN: function(info) {
    return axios.post(BASE_URL+'changenickname/', info);
  },
  changePW: function(info) {
    return axios.post(BASE_URL+'changepw/', info);
  },
  recipeList: function(page) {
    return axios.get(BASE_URL+'recipeboard/'+page+'/');
  },
  recipeLookup: function(post_id) {
    return axios.get(BASE_URL+'recipe/'+post_id+'/');
  },
  recipeAdd: function(info) {
    return axios.post(BASE_URL+'uploadrecipe/', info);
  },
  recipeEdit: function(info) {
    return axios.post(BASE_URL+'updaterecipe/', info);
  },
  recipeDelete: function(info) {
    return axios.post(BASE_URL+'deleterecipe/', info);
  },
  recipeLike: function(info) {
    return axios.post(BASE_URL+'likerecipe/', info);
  }
}