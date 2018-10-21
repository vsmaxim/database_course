<template>
    <div>
        <div class="page-header">
            <h2>Club list</h2>
            <router-link to="/clubs/add" class="btn btn-dark">Add club</router-link>
        </div>
        <table class="table">
            <thead class="thead-dark">
            <tr>
                <th scope="col">Id</th>
                <th scope="col">Club</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="club in clubs" :key="club.id">
                <td>{{ club.id }}</td>
                <td>{{ club.name }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "ClubList",
        data: function () {
            return {
                clubs: [],
            }
        },
        mounted() {
            axios.get('http://localhost:5000/clubs')
                .then((response) => (this.clubs = response.data));
        }
    }
</script>

<style scoped>
</style>