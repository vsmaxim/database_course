<template>
    <TableComponent :keys="keys" :data="fetchedData" title="Prize"></TableComponent>
</template>

<script>
    import axios from 'axios';
    import TableComponent from "./TableComponent";

    export default {
        name: "PrizesList",
        components: {TableComponent},
        data: function () {
            return {
                keys: ["id", "place", "dog", "ring_id"],
                fetchedData: [],
            }
        },
        mounted() {
            this.$http.get("prizes")
                .then((response) => this.fetchedData = response.data)
                .then(this.fetchDogs)
        },
        methods: {
            fetchDogs() {
                this.$http.get("dogs")
                    .then((response) => {
                        let dogNames = {};
                        response.data.forEach((item) => dogNames[item.id] = item.fancy_name);
                        this.fetchedData.forEach((item, index) => {
                            item.dog = dogNames[item.id];
                            this.$set(this.fetchedData, index, item);
                        })
                    })
            }
        }
    }
</script>

<style scoped>

</style>