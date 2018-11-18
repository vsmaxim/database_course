<template>
    <form
            id="breeds"
            @submit.prevent="handleForm"
    >
        <p v-if="errors.length">
            <ul>
                <li v-for="error in errors" v-bind:key="errors.indexOf(error)">{{ error }}</li>
            </ul>
        </p>
        <div class="form-group">
            <label for="name">Name:</label>
            <input
                    type="text"
                    class="form-control"
                    name="name"
                    id="name"
                    placeholder="Enter breed name"
                    v-model="form.name"
            >
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
    import axios from "axios";
    import login_required from "./mixins/login_required";

    export default {
        name: "BreedAdd",
        mixins: [login_required],
        data: function () {
            return {
                errors: [],
                form: {
                    name: "",
                }
            }
        },
        methods: {
        handleForm: function (e) {
            if (this.form.name) {
                return this.sendForm({
                    name: this.form.name,
                });
            }

            this.errors = [];

            if (!this.form.name) {
                this.errors.push("Name is required");
            }

            e.preventDefault();
        },
        sendForm: function (payload) {
            this.$http.post("breeds", payload)
                .then((response) => this.$router.back())
                .catch((error) => console.log(error));
        }
    }
    }
</script>

<style scoped>
    form {
        margin-top: 20px;
        margin-left: 120px;
        margin-right: 120px;
    }
</style>