<template>
    <TableComponent :keys="keys" title="Participant" :data="fetchedData"></TableComponent>
</template>

<script>
    import axios from 'axios';
    import TableComponent from "./TableComponent";
    export default {
        name: "ParticipantList",
        components: {TableComponent},
        data: function () {
            return {
                clubs: {},
                dogs: {},
                keys: ["id", "full_name", "dog", "club", "ring_id",],
                fetchedData: [],
            }
        },
        mounted() {
            axios.get('http://localhost:5000/clubs')
                .then((response) => Array.forEach(
                        response.data,
                        (obj) => this.clubs[obj.id] = obj.name
                    )
                )
                .catch((e) => console.log(e));
            axios.get('http://localhost:5000/dogs')
                .then((response) => Array.forEach(
                    response.data,
                    (obj) => this.dogs[obj.id] = obj.fancy_name
                ))
                .catch((e) => console.log(e));
            axios.get('http://localhost:5000/participants')
                .then((response) => this.fetchedData = Array.map(response.data, (i) => {
                    console.log(i);
                    i.club = this.clubs[i.club_id];
                    i.dog = this.dogs[i.dog_id];
                    i.full_name = `${i.last_name} ${i.first_name} ${i.middle_name}`;
                    return i;
                }))
                .then((participants) => participants.forEach((item, index) => {
                   axios.get(`http://localhost:5000/participants/${item.id}/ring`)
                       .then((response) => {
                           item.ring_id = response.data.ring_id;
                           if (!item.ring_id) {
                               item.ring_id = "N/A";
                           }
                           this.$set(this.fetchedData, index, item);
                       })
                       .catch((e) => console.log(e));
                }))
                .catch((e) => console.log(e));
        }
    }
</script>

<style scoped>

</style>