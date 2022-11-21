import Vue from 'vue';
import Router from 'vue-router';
// 레이아웃
import Empty from '@/EmptyLayout';
import Default from '@/DefaultLayout';

// 빈 레이아웃 화면
import Login from '@/views/Login';
import Signup from '@/views/Signup';
import EmailAuth from '@/views/EmailAuth';

// 기본 레이아웃 화면
import Home from '@/views/Home';
import Recipe from '@/views/Recipe';
import Photo from '@/views/Photo';
import MyPage from '@/views/MyPage';
// 레시피 게시판 관련 화면
import RecipeR from '@/views/Recipe/Recipe';
import CreateR from '@/views/Recipe/Create';
import LookupR from '@/views/Recipe/Lookup';
import EditR from '@/views/Recipe/Edit';
// 요리 사진 게시판 관련 화면
import PhotoP from '@/views/Photo/Photo';
import CreateP from '@/views/Photo/Create';
import LookupP from '@/views/Photo/Lookup';
import EditP from '@/views/Photo/Edit';
// 마이페이지 관련 화면
import MyPageM from '@/views/MyPage/MyPage';
import Refrigerator from '@/views/MyPage/Refrigerator';
import ChangeNickname from '@/views/MyPage/ChangeNickname';
import ChangePassword from '@/views/MyPage/ChangePassword';

Vue.use(Router); // vue 라우터 사용
const routes = [
  {
    path: '',
    component: Default,
    children: [
      {
        path: '',
        name: 'home',
        component: Home
      },
      {
        path: 'recipe',
        component: Recipe,
        children: [
          {
            path: '',
            name: 'recipe',
            component: RecipeR
          },
          {
            path: 'create',
            name: 'createR',
            component: CreateR
          },
          {
            path: 'lookup',
            name: 'lookupR',
            component: LookupR
          },
          {
            path: 'edit',
            name: 'editR',
            component: EditR
          },
        ]
      },
      {
        path: 'photo',
        component: Photo,
        children: [
          {
            path: '',
            name: 'photo',
            component: PhotoP
          },
          {
            path: 'create',
            name: 'createP',
            component: CreateP
          },
          {
            path: 'lookup',
            name: 'lookupP',
            component: LookupP
          },
          {
            path: 'edit',
            name: 'editP',
            component: EditP
          },
        ]
      },
      {
        path: 'mypage',
        component: MyPage,
        children: [
          {
            path: '',
            name: 'mypage',
            component: MyPageM
          },
          {
            path: 'refrigerator',
            name: 'refrigerator',
            component: Refrigerator
          },
          {
            path: 'changeNickname',
            name: 'changeNickname',
            component: ChangeNickname
          },
          {
            path: 'changePassword',
            name: 'changePassword',
            component: ChangePassword
          },
        ]
      }
    ]
  },
  {
    path: '',
    component: Empty,
    children: [
      {
        path: '/login',
        name: 'login',
        component: Login
      },
      {
        path: '/signup',
        name: 'signup',
        component: Signup
      },
      {
        path: '/email-auth/:id',
        name: 'email-auth',
        component: EmailAuth
      },
    ]
  }
]

const router = new Router({
  mode: 'history',
  routes
})

export default router