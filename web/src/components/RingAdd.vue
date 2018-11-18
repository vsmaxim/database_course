<template>
    <form @submit.prevent="handleForm" id="ring">
        <p>
        <ul>
            <li v-for="error in errors" :key="errors.indexOf(error)">{{error}}</li>
        </ul>
        </p>
        <div class="form-group">
            <label for="breed">Breed:</label>
            <select class="form-control" name="breed" id="breed" v-model="form.breed">
                <option v-for="breed in breeds" :key="breed.id" :value="breed.id">
                    {{ breed.name }}
                </option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
    import axios from 'axios';
    import login_required from "./mixins/login_required";

    export default {
        name: "RingAdd",
        mixins: [login_required],
        data: function () {
            return {
                errors: [],
                breeds: [],
                form: {
                    breed: null,
                }
            }
        },
        mounted: function () {
            this.$http.get("breeds")
                .then((response) => this.breeds = response.data)
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
                        breed_id: this.form.breed,
                    });
                }
            },
            submitForm(payload) {
                this.$http.post("rings", payload)
                    .then((response) => this.$router.back())
                    .catch((error) => console.log(error));
            }
        }
    }
</script>

<style scoped>

</style>