<template>
    <!--<div>-->
        <!--<div class="page-header">-->
            <!--<h2>Expert list</h2>-->
            <!--<router-link to="/experts/add" class="btn btn-dark">Add Expert</router-link>-->
        <!--</div>-->
        <!--<table class="table">-->
            <!--<thead class="thead-dark">-->
            <!--<tr>-->
                <!--<th scope="col">ID</th>-->
                <!--<th scope="col">Name</th>-->
                <!--<th scope="col">Breed</th>-->
                <!--<th scope="col">Dog</th>-->
            <!--</tr>-->
            <!--</thead>-->
            <!--<tbody>-->
            <!--<tr v-for="expert in experts" :key="expert.id">-->
                <!--<td>{{ expert.id }}</td>-->
                <!--<td>{{ expert.participant }}</td>-->
                <!--<td>{{ expert.breed_id }}</td>-->
                <!--<td>{{ expert.dog }}</td>-->
            <!--</tr>-->
            <!--</tbody>-->
        <!--</table>-->
    <!--</div>-->
    <TableComponent title="Expert" :keys="keys" :data="fetchedData"></TableComponent>
</template>

<script>
    import axios from 'axios';
    import TableComponent from "./TableComponent";
    export default {
        name: "ExpertList",
        components: {TableComponent},
        data: function () {
            return {
                keys: ["id", "participant", "breed_id", "dog_id"],
                fetchedData: [],
            }
        },
        mounted() {
            axios.get('http://localhost:5000/experts')
                .then((response) => this.fetchedData = response.data)
                .then((_) => this.fetchParticipants())
                .then((_) => this.fetchRings())
                .catch((e) => console.log(e));
        },
        methods: {
            fetchParticipants: function () {
              axios.get('http://localhost:5000/participants')
                  .then((response) => {
                      let participants = {};
                      response.data.forEach(
                          (item) => participants[item.id] = `${item.last_name} ${item.first_name} ${item.middle_name}`
                      );
                      this.fetchedData.forEach((item, index) => {
                          item.participant = participants[item.participant_id];
                          this.$set(this.fetchedData, index, item);
                      })
                  });
            },
            fetchRings: function () {
                axios.get('http://localhost:5000/rings')
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