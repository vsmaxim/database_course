<template>
    <div>
        <div class="page-header">
            <h2>Dog list</h2>
            <router-link to="/dogs/add" class="btn btn-dark">Add dog</router-link>
        </div>
        <table class="table">
            <thead class="thead-dark">
            <tr>
                <th scope="col">id</th>
                <th scope="col">Fancy Name</th>
                <th scope="col">Age</th>
                <th scope="col">Father's Breed</th>
                <th scope="col">Mother's Breed</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="dog in dogs" :key="dog.id">
                <td>{{ dog.id }}</td>
                <td>{{ dog.fancy_name }}</td>
                <td>{{ dog.age }}</td>
                <td>{{ dog.fathers_breed }}</td>
                <td>{{ dog.mothers_breed }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import axios from "axios";
    export default {
        name: "DogList",
        data: function () {
            return {
                dogs: [],
                breeds: {},
            }
        },
        mounted() {
           axios.get("http://localhost:5000/breeds")
               .then((response) => {
                   Array.forEach(response.data, (i) => this.breeds[i.id] = i.name);
               });
            axios.get("http://localhost:5000/dogs")
                .then((response) => {
                    this.dogs = Array.map(response.data, (i) => {
                       i.fathers_breed = this.breeds[i.fathers_breed];
                       i.mothers_breed = this.breeds[i.mothers_breed];
                       return i;
                    });
                });
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