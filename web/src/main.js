import Vue from 'vue'
import VueRouter from 'vue-router';
import App from './App.vue'
import DogList from './components/DogList.vue';
import DogAdd from './components/DogAdd.vue';
import ClubList from './components/ClubList.vue';
import ClubAdd from './components/ClubAdd.vue';
import BreedAdd from './components/BreedAdd.vue';
import BreedList from './components/BreedList.vue';

require("../node_modules/bootstrap/dist/css/bootstrap.min.css");

Vue.use(VueRouter)
Vue.config.productionTip = false;

const routes = [
    {path: '/clubs', component: ClubList},
    {path: '/clubs/add', component: ClubAdd},
    {path: '/breeds', component: BreedList},
    {path: '/breeds/add', component: BreedAdd},
    {path: '/dogs', component: DogList},
    {path: '/dogs/add', component: DogAdd},
];

const router = new VueRouter({
    routes,
});

new Vue({
    router,
    render: h => h(App),
}).$mount('#app');
