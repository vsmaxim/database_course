<template>

    <TableComponent title="Expert" :keys="keys" :data="fetchedData" :editable="true" edit-route="experts-edit"></TableComponent>
</template>

<script>
    import axios from 'axios';
    import TableComponent from "./TableComponent";
    import Vue from 'vue';
    export default {
        name: "ExpertList",
        components: {TableComponent},
        data: function () {
            return {
                keys: ["id", "participant", "breed_id", "dog_id", "ring_id"],
                fetchedData: [],
            }
        },
        mounted() {
            this.$http.get('experts')
                .then((response) => this.fetchedData = response.data)
                .then((_) => this.fetchParticipants())
                .then((_) => this.fetchRings())
                .catch((e) => console.log(e));
        },
        methods: {
            fetchParticipants: function () {
                this.$http.get('participants')
                  .then((response) => {
                      let participants = {};
                      let dogs = {};
                      response.data.forEach(
                          (item) => {
                              participants[item.id] = `${item.last_name} ${item.first_name} ${item.middle_name}`;
                              dogs[item.id] = item.dog_id;
                          }
                      );
                      this.fetchedData.forEach((item, index) => {
                          item.participant = participants[item.participant_id];
                          item.dog_id = dogs[item.participant_id];
                          this.$set(this.fetchedData, index, item);
                      })
                  });
            },
            fetchRings: function () {
                this.$http.get('rings')
                    .then((response) => {
                        let rings = {};
                        response.data.forEach((item) => rings[item.id] = item.breed_id);
                        this.fetchedData.forEach((item, index) => {
                            item.breed_id = rings[item.ring_id];
                            this.$set(this.fetchedData, index, item);
                        });
                    });
            },
        }
    }
</script>

<style scoped>

</style>