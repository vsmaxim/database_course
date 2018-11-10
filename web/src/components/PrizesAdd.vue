<template>
    <form @submit.prevent="handleForm" id="expert">
        <p>
        <ul>
            <li v-for="error in errors" :key="errors.indexOf(error)">{{error}}</li>
        </ul>
        </p>
        <div class="form-group">
            <label for="dog">Dog:</label>
            <select class="form-control" name="dog" id="dog" v-model="form.dog">
                <option v-for="dog in availableDogs" :key="dog.id" :value="dog.id">
                    {{ dog.fancy_name }}
                </option>
            </select>
        </div>
        <div class="form-group">
            <label for="place">Place:</label>
            <select class="form-control" name="place" id="place" v-model="form.place">
                <option v-for="place in availablePlaces" :value="place">
                    {{ place }}
                </option>
            </select>
        </div>
        <div class="form-group">
            <label for="ring">Ring: </label>
            <select class="form-control" name="ring" id="ring" v-model="form.ring" @change="constructRingDependentData">
                <option v-for="ring in rings" :value="ring.id">
                    {{ ring.id }}
                </option>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "PrizesAdd",
        data: function () {
            return {
                form: {
                    dog: undefined,
                    place: undefined,
                    ring: undefined,
                },
                definedPrizes: {},
                availablePlaces: [],
                availableDogs: [],
                errors: [],
                dogs: [],
                rings: [],
                prizes: [],
            }
        },
        mounted() {
            this.fetchDogs();
            this.fetchRings();
            this.fetchDefinedPrizes();
        },
        methods: {
            fetchDefinedPrizes() {
                axios.get('http://localhost:5000/prizes')
                    .then((response) => this.prizes = response.data)
                    .then((prizes) => prizes.forEach((item) => this.definedPrizes.hasOwnProperty(item.ring_id) ?
                        this.definedPrizes[item.ring_id].shift(item.place) :
                        this.definedPrizes[item.ring_id] = [item.place]))
            },
            fetchDogs() {
                axios.get('http://localhost:5000/dogs')
                  .then((response) => this.dogs = response.data);
            },
            fetchRings() {
                axios.get('http://localhost:5000/rings')
                    .then((response) => this.rings = response.data);
            },
            constructAvailablePrizes(ring_id) {
                this.place = null;
                const allPrizes = [1, 2, 3];
                this.availablePlaces = this.definedPrizes.hasOwnProperty(ring_id) ?
                    allPrizes.filter((item) => !this.definedPrizes[ring_id].includes(item)) :
                    allPrizes;
            },
            constructAvailableDogs(ring_id) {
                this.dog = null;
                let breedsOfRing = {};
                let awardedDogs = this.prizes.map((item) => item.dog_id);
                this.rings.forEach((item) => breedsOfRing[item.breed_id] = item.id);
                this.availableDogs = this.dogs.filter(
                    (item) => breedsOfRing[item.breed_id] === ring_id && !awardedDogs.includes(item.id)
                );
            },
            constructRingDependentData(_) {
                this.constructAvailableDogs(this.form.ring);
                this.constructAvailablePrizes(this.form.ring);
            },
            formValid() {
                this.errors = [];
                for (let key in this.form) {
                    if (!this.form[key]) {
                        this.errors.push(`${key} must not be empty.`);
                    }
                }
                return !this.errors.length;
            },
            handleForm(e) {
                if (this.formValid()) {
                    this.submitForm({
                        dog_id: this.form.dog,
                        place: this.form.place,
                        ring_id: this.form.ring,
                    });
                } else {
                    e.preventDefault();
                }
            },
            submitForm(payload) {
                axios.post("http://localhost:5000/prizes", payload)
                    .then((response) => this.$router.back())
                    .catch((error) => console.log(error));
            }
        }

    }
</script>

<style scoped>

</style>