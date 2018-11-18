<template>
    <form @submit.prevent="submitForm" >
        <div class="form-group">
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="username" placeholder="Username">
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" v-model="password" placeholder="Password">
        </div>
        <button class="btn btn-primary">Login</button>
    </form>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                username: null,
                password: null
            }
        },
        methods: {
            submitForm() {
                this.$http.post('login', {"username": this.username, "password": this.password})
                    .then((response) => {
                        console.log(response.data.group);
                        this.$store.commit('setGroup', response.data.group);
                        this.$router.push('/');
                    })
                    .catch((err) => console.log(err));
            }
        }
    }
</script>

<style scoped>

</style>