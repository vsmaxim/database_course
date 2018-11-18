<template>
    <TableComponent :keys="keys" title="Dog" :data="fetchedData"></TableComponent>
</template>

<script>
    import axios from "axios";
    import TableComponent from "./TableComponent";

    export default {
        name: "DogList",
        components: {TableComponent},
        data: function () {
            return {
                keys: ["id", "fancy_name", "age", "breed_id", "fathers_breed_id", "mothers_breed_id"],
                fetchedData: [],
                breeds: {},
            }
        },
        mounted() {
           this.$http.get("breeds")
               .then((response) => {
                   Array.forEach(response.data, (i) => this.breeds[i.id] = i.name);
               });
            this.$http.get("dogs")
                .then((response) => {
                    this.fetchedData = Array.map(response.data, (i) => {
                       i.fathers_breed_id = this.breeds[i.fathers_breed_id];
                       i.mothers_breed_id = this.breeds[i.mothers_breed_id];
                       i.breed_id = this.breeds[i.breed_id];
                       return i;
                    });
                });
        }
    }
</script>

<style scoped>
</style>