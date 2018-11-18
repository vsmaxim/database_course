<template>
    <form
        id="clubs"
        @submit.prevent="handleForm"
        action="http://localhost:5000/clubs"
        method="post"
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
                    placeholder="Enter club name"
                    v-model="form.name"
            >
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "ClubAdd",
        data: function () {
            return {
                errors: [],
                form: {
                    name: null,
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
                this.$http.post("clubs", payload)
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