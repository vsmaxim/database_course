<template>
    <div id="app">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">DogExpo</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto" v-if="loggedIn">

                    <li class="nav-item"><router-link to="/home" class="nav-link">Home</router-link></li>
                    <li class="nav-item"><router-link to="/dogs" class="nav-link">Dogs</router-link></li>
                    <li class="nav-item"><router-link to="/participants" class="nav-link">Participants</router-link></li>
                    <li class="nav-item"><router-link to="/clubs" class="nav-link">Clubs</router-link></li>
                    <li class="nav-item"><router-link to="/rings" class="nav-link">Rings</router-link></li>
                    <li class="nav-item"><router-link to="/breeds" class="nav-link">Breeds</router-link></li>
                    <li class="nav-item"><router-link to="/experts" class="nav-link">Experts</router-link></li>
                    <li class="nav-item"><router-link to="/prizes" class="nav-link">Prizes</router-link></li>
                    <li class="nav-item" v-if="isAdmin"><router-link to="/users" class="nav-link">Users</router-link></li>
                </ul>
                <a @click="logout" class="nav-link" v-if="loggedIn">Logout</a>
            </div>
        </nav>
        <router-view></router-view>
    </div>
</template>

<script>

    export default {
        name: 'app',
        components: {
        },
        methods: {
            logout(e) {
                e.preventDefault();
                this.$http.post('logout')
                    .then((response) => {
                        this.$store.commit('setGroup', undefined);
                        this.$router.push({name: 'login'});
                    })
                    .catch((e) => console.log(e));
            }
        },
        computed: {
            loggedIn() {
                return this.$store.state.role;
            },
            isAdmin() {
                return this.$store.state.role === "administrator";
            }
        }
    }
</script>

<style>
    .table {
        margin: 20px;
    }
    .page-header {
        margin: 20px;
    }
    .page-header > h2 {
        display: inline;
    }
    .page-header > a {
        float: right;
    }
    form {
        margin-top: 20px;
        margin-left: 120px;
        margin-right: 120px;
    }
</style>
