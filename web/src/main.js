import Vue from 'vue'
import VueRouter from 'vue-router';
import App from './App.vue'
import axios from 'axios';
import DogList from './components/DogList.vue';
import DogAdd from './components/DogAdd.vue';
import ClubList from './components/ClubList.vue';
import ClubAdd from './components/ClubAdd.vue';
import BreedAdd from './components/BreedAdd.vue';
import BreedList from './components/BreedList.vue';
import ParticipantList from './components/ParticipantList.vue';
import ParticipantAdd from './components/ParticipantAdd.vue';
import RingList from './components/RingList.vue';
import RingAdd from './components/RingAdd.vue';
import ExpertList from './components/ExpertList.vue';
import ExpertAdd from './components/ExpertAdd';

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
    {path: '/participants', component: ParticipantList},
    {path: '/participants/add', component: ParticipantAdd},
    {path: '/rings', component: RingList},
    {path: '/rings/add', component: RingAdd},
    {path: '/experts', component: ExpertList},
    {path: '/experts/add', component: ExpertAdd},
];

const router = new VueRouter({
    routes,
});

new Vue({
    router,
    render: h => h(App),
}).$mount('#app');
