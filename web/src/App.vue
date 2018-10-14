<template>
    <div id="app">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">DogExpo</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">

                    <li class="nav-item"><router-link to="/home" class="nav-link">Home</router-link></li>
                    <li class="nav-item"><router-link to="/dogs" class="nav-link">Dogs</router-link></li>
                    <li class="nav-item"><router-link to="/participants" class="nav-link">Participants</router-link></li>
                    <li class="nav-item"><router-link to="/clubs" class="nav-link">Clubs</router-link></li>
                    <li class="nav-item"><router-link to="/rings" class="nav-link">Rings</router-link></li>
                    <li class="nav-item"><router-link to="/breeds" class="nav-link">Breeds</router-link></li>
                </ul>
            </div>
        </nav>
        <router-view></router-view>
    </div>
</template>

<script>

    export default {
        name: 'app',
        components: {
        }
    }
</script>

<style>
    /*#app {*/
    /*font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
    /*-webkit-font-smoothing: antialiased;*/
    /*-moz-osx-font-smoothing: grayscale;*/
    /*text-align: center;*/
    /*color: #2c3e50;*/
    /*margin-top: 60px;*/
    /*}*/
</style>
