<template>
    <div>
        <div class="diploma" v-if="place">
            <h1>Diploma</h1>
            <p>
                The certificate approves that {{ name }} was participant of DogExpo 2018
                and got the {{ place }} place.
            </p>
        </div>
        <div class="consoling-diploma" v-else>
            <h1>Consoling letter</h1>
            <p>This certificate approves that {{ name }} was participant of DogExpo 2018</p>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "ParticipantInfo",
        data() {
            return {
                participant_id: this.$route.params.id,
                place: null,
            }
        },
        mounted() {
            this.$http.get(`participants/${this.participant_id}/report`)
                .then((response) => this.place = response.data.place
                )
        }
    }
</script>

<style scoped>

</style>