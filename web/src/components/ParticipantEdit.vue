<template>
    <form @submit.prevent="submitForm">
        <div class="form-group">
            <label for="club">Club: </label>
            <select v-model="form.club" id="club" name="club" class="form-control">
                <option v-for="club in clubs" :key="club.id" :value="club.id">
                    {{ club.name }}
                </option>
            </select>
        </div>
        <button class="btn btn-primary">Save</button>
    </form>
</template>

<script>
    import axios from 'axios';
    import login_required from "./mixins/login_required";

    export default {
        name: "ParticipantEdit",
        mixins: [login_required],
        data() {
            return {
                clubs: [],
                form: {
                    club: null,
                }
            }
        },
        mounted() {
            this.$http.get("clubs")
                .then((response) => this.clubs = response.data);
        },
        methods: {
            submitForm() {
                this.$http.put(`participants/${this.$route.params.id}`, {"club_id": this.form.club})
                    .then((response) => this.$router.back());
            }
        }
    }
</script>

<style scoped>

</style>