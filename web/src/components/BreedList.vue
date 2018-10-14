<template>
    <div>
        <div class="page-header">
            <h2>Breed list</h2>
            <router-link to="/breeds/add" class="btn btn-dark">Add breed</router-link>
        </div>
        <table class="table">
            <thead class="thead-dark">
            <tr>
                <th scope="col">Id</th>
                <th scope="col">Breed</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="breed in breeds" :key="breed.id">
                <td>{{ breed.id }}</td>
                <td>{{ breed.name }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import axios from "axios";
    export default {
        name: "BreedList",
        data: function () {
            return {
                breeds: []
            }
        },
        mounted() {
            axios.get("http://localhost:5000/breeds")
                .then((response) => this.breeds = response.data)
        }
    }
</script>

<style scoped>
    .table {
        margin: 20px;
    }
    .page-header {
        margin: 20px;
    }
    .page-header > h2 {
        display: inline;
    }
    .page-header > a {
        float: right;
    }
</style>