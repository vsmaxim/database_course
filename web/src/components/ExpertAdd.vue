<template>
    <form @submit.prevent="handleForm" id="expert">
        <p>
        <ul>
            <li v-for="error in errors" :key="errors.indexOf(error)">{{error}}</li>
        </ul>
        </p>
        <div class="form-group">
            <label for="participant">Participant:</label>
            <select class="form-control" name="participant" id="participant" v-model="form.participant">
                <option v-for="participant in participants" :key="participant.id" :value="participant.id">
                    {{ participant.name }}
                </option>
            </select>
        </div>
        <div class="form-group">
            <label for="ring">Ring:</label>
            <select class="form-control" name="ring" id="ring" v-model="form.ring">
                <option v-for="ring in rings" :key="ring.id" :value="ring.id">
                    {{ ring.id }}
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
        name: "ExpertAdd",
        mixins: [login_required],
        data: function () {
            return {
                errors: [],
                participants: [],
                rings: [],
                form: {
                    participant: null,
                    ring: null,
                }
            }
        },
        mounted: function () {
            this.$http.get("rings")
                .then((response) => this.rings = response.data)
                .catch((e) => console.log(e));
            this.$http.get("participants")
                .then((response) => this.participants = Array.map((response.data), (i) => {
                    return {
                        name: `${i.last_name} ${i.first_name} ${i.middle_name}`,
                        id: i.id,
                    }
            }))
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
                        participant_id: this.form.participant,
                        ring_id: this.form.ring,
                    });
                }
            },
            submitForm(payload) {
                this.$http.post("experts", payload)
                    .then((response) => this.$router.back())
                    .catch((error) => console.log(error));
            }
        }
    }
</script>

<style scoped>

</style>