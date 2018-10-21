<template>
    <div>
        <div class="page-header">
            <h2>Participant list</h2>
            <router-link to="/participants/add" class="btn btn-dark">Add Participant</router-link>
        </div>
        <table class="table">
            <thead class="thead-dark">
            <tr>
                <th scope="col">id</th>
                <th scope="col">Name</th>
                <th scope="col">Club</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="participant in participants" :key="participant.id">
                <td>{{ participant.id }}</td>
                <td>{{ participant.last_name}} {{participant.first_name}} {{participant.middle_name}}</td>
                <td>{{ participant.club }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "ParticipantList",
        data: function () {
            return {
                clubs: {},
                participants: [],
            }
        },
        mounted() {
            axios.get('http://localhost:5000/clubs')
                .then((response) => Array.forEach(
                        response.data,
                        (obj) => this.clubs[obj.id] = obj.name
                    )
                )
                .catch((e) => console.log(e));
            axios.get('http://localhost:5000/participants')
                .then((response) => this.participants = Array.map(response.data, (i) => {
                    i.club = this.clubs[i.club_id];
                    return i;
                }))
                .catch((e) => console.log(e));
            console.log(this.clubs);
            console.log(this.participants);
        }
    }
</script>

<style scoped>

</style>