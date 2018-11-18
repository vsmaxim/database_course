<template>
    <div>
        <TableComponent :keys="keys" title="Breed" :data="fetchedData"></TableComponent>
    </div>
</template>

<script>
    import TableComponent from "./TableComponent";

    export default {
        name: "BreedList",
        components: {TableComponent},
        data: function () {
            return {
                breeds: [],
                keys: ["id", "name", "expert"],
                fetchedData: [],
            }
        },
        mounted() {
            this.$http.get('breeds')
                .then((response) => this.fetchedData = response.data)
                .then((breeds) => breeds.forEach((item, index) => {
                    this.$http.get(`breeds/${item.id}/experts`)
                        .then((response) => {
                            const expert_id = response.data.expert_id;
                            item.expert = expert_id ? expert_id : "N/A";
                            this.$set(this.fetchedData, index, item);
                        })
                }));
        }
    }
</script>

<style scoped>
</style>