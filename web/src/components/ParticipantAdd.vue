<template>
    <form @submit.prevent="handleForm" id="participant">
        <p>
            <ul>
                <li v-for="error in errors" :key="errors.indexOf(error)">{{error}}</li>
            </ul>
        </p>
        <div class="form-group">
            <label for="first_name">First name:</label>
            <input type="text" name="first_name" id="first_name" v-model="form.first_name" class="form-control"/>
        </div>
        <div class="form-group">
            <label for="middle_name">Middle name:</label>
            <input type="text" name="first_name" id="middle_name" v-model="form.middle_name" class="form-control"/>
        </div>
        <div class="form-group">
            <label for="last_name">Last name:</label>
            <input type="text" name="last_name" id="last_name" v-model="form.last_name" class="form-control"/>
        </div>
        <div class="form-group">
            <label for="dog">Dog:</label>
            <select class="form-control" name="dog" id="dog" v-model="form.dog">
                <option v-for="dog in dogs" :key="dog.id" :value="dog.id">
                    {{ dog.fancy_name }}
                </option>
            </select>
        </div>
        <div class="form-group">
            <label for="club">Club:</label>
            <select class="form-control" name="club" id="club" v-model="form.club">
                <option v-for="club in clubs" :key="club.id" :value="club.id">
                    {{ club.name }}
                </option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "ParticipantAdd",
        data: function () {
            return {
                errors: [],
                clubs: [],
                dogs: [],
                form: {
                    first_name: null,
                    last_name: null,
                    middle_name: null,
                    club: null,
                    dog: null
                }
            }
        },
        mounted: function () {
            axios.get("http://localhost:5000/clubs")
                .then((response) => this.clubs = response.data)
                .catch((e) => console.log(e));
            axios.get("http://localhost:5000/dogs")
                .then((response) => this.dogs = response.data)
                .catch((e) => console.log(e));
        },
        methods: {
            handleForm: function (e) {
                this.errors = [];
                for (let key in this.form) {
                    if (!this.form[key]) {
                        this.errors.push(`${key} must not be empty.`)
                    }
                }

                if (this.errors.length) {
                    e.preventDefault();
                } else {
                    this.submitForm({
                        first_name: this.form.first_name,
                        middle_name: this.form.middle_name,
                        last_name: this.form.last_name,
                        club_id: this.form.club,
                        dog_id: this.form.dog,
                    });
                }
            },
            submitForm(payload) {
                axios.post("http://localhost:5000/participants", payload)
                    .then((response) => this.$router.back())
                    .catch((error) => console.log(error));
            }
        }
    }
</script>

<style scoped>

</style>