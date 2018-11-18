<template>
    <TableComponent title="Ring" :keys="keys" :data="fetchedData"></TableComponent>
</template>

<script>
    import axios from 'axios';
    import TableComponent from "./TableComponent";
    import login_required from "./mixins/login_required";

    export default {
        name: "RingList",
        components: {TableComponent},
        mixins: [login_required],
        data() {
            return {
                fetchedData: [],
                keys: ["id", "breed",],
                breeds: {},
            }
        },
        mounted() {
            this.$http.get('breeds')
                .then((response) => Array.forEach(response.data,(i) => this.breeds[i.id] = i.name))
                .catch((e) => console.log(e));
            this.$http.get('rings')
                .then((response) => this.fetchedData = response.data)
                .then((rings) => this.fetchBreeds());
        },
        methods: {
            fetchBreeds() {
                this.$http.get('breeds')
                    .then((response) => {
                        let breeds = {};
                        response.data.forEach((i) => breeds[i.id] = i.name);
                        this.fetchedData.forEach((item, index) => {
                            item.breed = breeds[item.breed_id];
                            this.$set(this.fetchedData, index, item);
                        })
                    })
            },
        }
    }
</script>

<style scoped>

</style>