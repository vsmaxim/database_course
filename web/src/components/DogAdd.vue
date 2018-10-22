<template>
    <form @submit.prevent="handleForm" id="dog">
        <p>
            <ul>
                <li v-for="error in errors" :key="errors.indexOf(error)">{{error}}</li>
            </ul>
        </p>
        <div class="form-group">
            <label for="name">Fancy name:</label>
            <input type="text" name="fancy_name" id="name" v-model="form.fancy_name" class="form-control"/>
        </div>
        <div class="form-group">
            <label for="age">Age: </label>
            <input type="number" id="age" v-model="form.age" name="age" min="0" class="form-control"/>
        </div>
        <div class="form-group">
            <label for="breed_id">Breed:</label>
            <select class="form-control" name="breed_id" id="breed_id" v-model="form.breed_id">
                <option v-for="breed in breeds" :key="breed.id" :value="breed.id">
                    {{ breed.name }}
                </option>
            </select>
        </div>
        <div class="form-group">
            <label for="mothers_breed_id">Mothers breed:</label>
            <select class="form-control" name="mothers_breed_id" id="mothers_breed_id" v-model="form.mothers_breed_id">
                <option v-for="breed in breeds" :key="breed.id" :value="breed.id">
                    {{ breed.name }}
                </option>
            </select>
        </div>
        <div class="form-group">
            <label for="fathers_breed_id">Fathers breed:</label>
            <select class="form-control" name="fathers_breed_id" id="fathers_breed_id" v-model="form.fathers_breed_id">
                <option v-for="breed in breeds" :key="breed.id" :value="breed.id">
                    {{ breed.name }}
                </option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
    import axios from "axios";

    export default {
        name: "DogAdd",
        data: function () {
            return {
                errors: [],
                breeds: [],
                form: {
                    fancy_name: null,
                    age: null,
                    breed_id: null,
                    fathers_breed_id: null,
                    mothers_breed_id: null,
                }
            }
        },
        mounted() {
            axios.get("http://localhost:5000/breeds")
                .then((response) => this.breeds = response.data)
                .catch((error) => console.log(error));
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
                        fancy_name: this.form.fancy_name,
                        age: this.form.age,
                        breed_id: this.form.breed_id,
                        fathers_breed_id: this.form.fathers_breed_id,
                        mothers_breed_id: this.form.mothers_breed_id
                    })
                }
            },
            submitForm(payload) {
                axios.post("http://localhost:5000/dogs", payload)
                    .then((response) => this.$router.back())
                    .catch((error) => console.log(error));
            }
        }
    }
</script>

<style scoped>

</style>