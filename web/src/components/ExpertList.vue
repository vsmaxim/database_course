<template>
    <div>
        <div class="page-header">
            <h2>Expert list</h2>
            <router-link to="/experts/add" class="btn btn-dark">Add Expert</router-link>
        </div>
        <table class="table">
            <thead class="thead-dark">
            <tr>
                <th scope="col">Name</th>
                <th scope="col">Ring</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="expert in experts" :key="expert.ring_id">
                <td>{{ expert.participant }}</td>
                <td>{{ expert.ring_id }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import axios from 'axios';
    export default {
        name: "ExpertList",
        data: function () {
            return {
                participants: {},
                rings: {},
                experts: [],
            }
        },
        mounted() {
            axios.get('http://localhost:5000/participants')
                .then((response) => Array.forEach(
                    response.data,
                    (obj) => this.participants[obj.id] = `${obj.last_name} ${obj.first_name} ${obj.middle_name}`
                    )
                )
                .catch((e) => console.log(e));
            axios.get('http://localhost:5000/rings')
                .then((response) => Array.forEach(
                    response.data,
                    (obj) => this.rings[obj.id] = obj.breed_id
                    )
                )
                .catch((e) => console.log(e));
            axios.get('http://localhost:5000/experts')
                .then((response) => this.experts = Array.map(response.data, (i) => {
                    console.log(i);
                    i.participant = this.participants[i.participant_id];
                    i.ring_id = this.rings[i.ring_id];
                    return i;
                }))
                .catch((e) => console.log(e));
            console.log(this.rings);
        }
    }
</script>

<style scoped>

</style>