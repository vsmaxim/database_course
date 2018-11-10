<template>
    <TableComponent :keys="keys" title="Club" :data="fetchedData"></TableComponent>
</template>

<script>
    import axios from 'axios';
    import TableComponent from "./TableComponent";

    export default {
        name: "ClubList",
        components: {TableComponent},
        data: function () {
            return {
                clubs: [],
                keys: ["id", "name", "breeds", "first_places", "second_places", "third_places",],
                fetchedData: [],
            }
        },
        mounted() {
            axios.get('http://localhost:5000/clubs')
                .then((response) => this.fetchedData = response.data)
                .then((clubs) => Array.forEach(clubs, (item, index) => {
                    axios.get(`http://localhost:5000/clubs/${item.id}/breeds`)
                        .then((response) => response.data.join(', '))
                        .then((breeds) => {
                            item.breeds = breeds;
                            this.$set(this.fetchedData, index, item);
                        });
                    axios.get(`http://localhost:5000/clubs/${item.id}/prizes`)
                        .then((response) => {
                            item.first_places = response.data.first;
                            item.second_places = response.data.second;
                            item.third_places = response.data.third;
                            this.$set(this.fetchedData, index, item);
                        })
                }));
        }
    }
</script>

<style scoped>
</style>