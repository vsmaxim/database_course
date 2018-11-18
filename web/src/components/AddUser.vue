<template>
    <form
            id="user"
            @submit.prevent="handleForm"
    >
        <p v-if="errors.length">
        <ul>
            <li v-for="error in errors" v-bind:key="errors.indexOf(error)">{{ error }}</li>
        </ul>
        </p>
        <div class="form-group">
            <label for="username">Username:</label>
            <input
                    type="text"
                    class="form-control"
                    name="username"
                    id="username"
                    placeholder="Enter username"
                    v-model="form.username"
            >
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input
                    type="password"
                    class="form-control"
                    name="password"
                    id="password"
                    placeholder="Enter password"
                    v-model="form.password"
            >
        </div>
        <div class="form-group">
            <label for="participant">Participant:</label>
            <select class="form-control"
                    v-model="form.participant"
                    id="participant"
                    name="participant"
            >
                <option
                        v-for="participant in participants"
                        :value="participant.id"
                >
                    {{ participant.first_name }} {{ participant.second_name }} {{ participant.last_name }}
                </option>
            </select>

        </div>
        <div class="form-group">
            <label for="participant">Group:</label>
            <select class="form-control"
                    v-model="form.group"
                    id="group"
                    name="group"
            >
                <option
                        v-for="group in groups"
                        :value="group.id"
                >
                    {{ group.name }}
                </option>
            </select>

        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
    export default {
        name: "AddUser",
        data() {
            return {
                form: {
                    participant: null,
                    username: null,
                    password: null,
                    group: null,
                },
                errors: [],
                participants: [],
                groups: [],
            }
        },
        mounted() {
          this.$http.get('participants')
              .then((response) => this.participants = response.data)
              .catch((err) => console.log(err));
          this.$http.get('groups')
              .then((response) => this.groups = response.data);
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
                        participant_id: this.form.participant,
                        group_id: this.form.group,
                        username: this.form.username,
                        password: this.form.password,
                    });
                }
            },
            submitForm(payload) {
                this.$http.post("users", payload)
                    .then((response) => this.$router.back())
                    .catch((error) => console.log(error));
            }
        }
    }
</script>

<style scoped>

</style>