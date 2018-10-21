<template>
    <div>
        <div class="page-header">
            <h2>Ring list</h2>
            <router-link to="/rings/add" class="btn btn-dark">Add Ring</router-link>
        </div>
        <table class="table">
            <thead class="thead-dark">
            <tr>
                <th scope="col">id</th>
                <th scope="col">Breed</th>
                <th scope="col">Numbers range</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="ring in rings" :key="ring.id">
                <td>{{ ring.id }}</td>
                <td>{{ ring.breed}}</td>
                <td>Not implemented</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "RingList",
        data: function () {
            return {
                rings: [{id: 1, breed: "Jopa"}],
                breeds: {},
            }
        },
        mounted() {
            axios.get('http://localhost:5000/breeds')
                .then((response) => Array.forEach(response.data,(i) => this.breeds[i.id] = i.name))
                .catch((e) => console.log(e));
            axios.get('http://localhost:5000/rings')
                .then((response) => this.rings = Array.map(response.data, (i) => {
                    i.breed = this.breeds[i.breed_id];
                    return i;
            }));
            console.log(this.rings);
        }
    }
</script>

<style scoped>

</style>