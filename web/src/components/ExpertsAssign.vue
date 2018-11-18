<template>
    <form @submit.prevent="submitForm">
        <div class="form-group">
            <label for="ring">Expert ring (may be empty):</label>
            <select v-model="form.ring_id" name="ring" id="ring" class="form-control" >
                <option v-for="ring in rings" :value="ring">
                    {{ ring }}
                </option>
            </select>
        </div>
        <button class="btn btn-primary" @click.prevent="submitForm">Save</button>
    </form>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "ExpertsAssign",
        data() {
          return {
              rings: [],
              form: {
                  ring_id: null,
              }
          }
        },
        mounted() {
            this.$http.get("rings/unused")
                .then((response) => {
                    let data = Array.from(response.data);
                    data.unshift('');
                    this.rings = data;

                });
            this.$http.get(`experts/${this.$route.params.id}`)
                .then((response) => this.form.ring_id = response.data.ring_id)
                .then(() => console.log(this.form.ring_id))
        },
        methods: {
            submitForm(e) {
                this.$http.put(`experts/${this.$route.params.id}`, {"ring_id": this.form.ring_id})
                    .then(() => this.$router.back())
                    .catch((e) => console.log(e));
            }
        }
    }
</script>

<style scoped>
    #ring {
        width: 100
    }
    .btn {
        margin-top: 10px;
    }
</style>