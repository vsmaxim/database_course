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
import ExpertsAssign from './components/ExpertsAssign';
import PrizesList from './components/PrizesList';
import PrizesAdd from './components/PrizesAdd';
import ParticipantEdit from './components/ParticipantEdit';
import ParticipantInfo from './components/ParticipantInfo';
import Login from './components/Login';

require("../node_modules/bootstrap/dist/css/bootstrap.min.css");

Vue.use(VueRouter);
Vue.config.productionTip = false;
Vue.prototype.$http = axios.create({
    baseURL: 'http://localhost:5000/',
    withCredentials: true,
});

const routes = [
    {path: '/clubs', component: ClubList},
    {path: '/clubs/add', component: ClubAdd},
    {path: '/breeds', component: BreedList},
    {path: '/breeds/add', component: BreedAdd},
    {path: '/dogs', component: DogList},
    {path: '/dogs/add', component: DogAdd},
    {path: '/participants', component: ParticipantList},
    {path: '/participants/add', component: ParticipantAdd},
    {path: '/participants/:id/edit', component: ParticipantEdit, name:'participant-edit'},
    {path: '/participants/:id/info', component: ParticipantInfo, name:'participant-info'},
    {path: '/rings', component: RingList},
    {path: '/rings/add', component: RingAdd},
    {path: '/experts', component: ExpertList},
    {path: '/experts/add', component: ExpertAdd},
    {path: '/experts/:id/edit', component: ExpertsAssign, name: "experts-edit"},
    {path: '/prizes', component: PrizesList},
    {path: '/prizes/add', component: PrizesAdd},
    {path: '/login', component: Login, name: 'login'},
];

const router = new VueRouter({
    routes,
});

axios.interceptors.response.use((config) => config, (error) => router.push({name: 'login'}));
// axios.interceptors.request.use((config) => {
//     config.withCredentials = true;
//     config.crossdomain = true;
//     return config;
// }, (error) => Promise.reject(error));

new Vue({
    router,
    render: h => h(App),
}).$mount('#app');

router.push({name: 'login'});